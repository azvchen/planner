from django.core.management.base import BaseCommand
from django.db import transaction

from viewer.models import Department, Instructor, Course, Section

import urllib.request
from html.parser import HTMLParser


class Command(BaseCommand):
    help = 'Imports course data from a text file into the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            action='store_true',
            dest='file_name',
            default=None,
            help='Name of file (optional)',
        )

    def handle(self, *args, **options):
        if not options['file_name']:
            self.remote()
        else:
            with open(options['file_name']) as f:
                self.import_file(f.read())

    def remote(self):
        parser = Lou1110Parser()
        with urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/') as response:
            parser.feed(response.read().decode("utf-8"))
        for dept in parser.dept_ids[5:]:
            with urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/louslist/' + dept) as response:
                self.import_file(response.read().decode("utf-8"))

    @transaction.atomic
    def import_file(self, text):
        courses = [line.split('|') for line in text.split('\n')]
        for course_data in courses:
            if len(course_data) != 17:
                continue
            try:
                instructor_name = course_data[4].split('+')[0]
            except IndexError:
                instructor_name = ''
            for i in range(7, 12):
                course_data[i] = course_data[i] == 'true'

            dept = Department(dept_id=course_data[0], name=course_data[0])
            dept.save()

            instructor = Instructor.add_if_missing(dept, instructor_name)
            instructor.save()

            course = Course.add_if_missing(dept, course_data[1], course_data[3], course_data[6])
            course.save()

            section = Section.add_if_missing(course_data[2], course, Section.FALL, 2017, instructor, course_data[5],
                                             course_data[7:12], course_data[12], course_data[13],
                                             course_data[14], course_data[15], course_data[16])
            section.save()


class Lou1110Parser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.dept_ids = []

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href':
                    self.dept_ids.append(val)

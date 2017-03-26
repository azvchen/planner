from django.core.management.base import BaseCommand
from viewer.models import Department, Instructor, Course, Section

from datetime import time


class Command(BaseCommand):
    help = 'Imports course data from a text file into the database'

    def add_arguments(self, parser):
        parser.add_argument('file_name')

    def handle(self, *args, **options):
        with open(options['file_name']) as f:
            courses = [line.split('|') for line in f]
        for course_data in courses:
            for i in range(7, 12):
                course_data[i] = course_data[i] == 'true'

            dept = Department(dept_id=course_data[0], name='Computer Science')
            dept.save()

            instructor = Instructor(name=course_data[4].split('+')[0])
            instructor.dept = dept
            instructor.save()

            course = Course(number=course_data[1], title=course_data[3], hours=course_data[6])
            course.dept = dept
            course.save()

            section = Section(section_id=course_data[2], format=course_data[5],
                              monday=course_data[7], tuesday=course_data[8],
                              wednesday=course_data[9], thursday=course_data[10], friday=course_data[11],
                              location=course_data[14], enrollment=course_data[15], max_enrollment=course_data[16])
            section.course = course
            section.instructor = instructor
            section.start_time = time(hour=int(course_data[12][:-2]), minute=int(course_data[12][-2:]))
            section.end_time = time(hour=int(course_data[13][:-2]), minute=int(course_data[13][-2:]))
            section.save()

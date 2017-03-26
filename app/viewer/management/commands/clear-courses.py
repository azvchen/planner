from django.core.management.base import BaseCommand
from viewer.models import Department, Instructor, Course, Section


class Command(BaseCommand):
    help = 'Clears all course data from the database'

    def handle(self, *args, **options):
        Section.objects.all().delete()
        Course.objects.all().delete()
        Instructor.objects.all().delete()
        Department.objects.all().delete()

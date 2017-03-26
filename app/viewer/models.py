from django.db import models


class Department(models.Model):
    dept_id = models.CharField(max_length=4)
    name = models.CharField(max_length=50)


class Instructor(models.Model):
    name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.PROTECT)


class Course(models.Model):
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    number = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    hours = models.IntegerField()


class Section(models.Model):
    LECTURE = 'Lec'
    DISCUSSION = 'Dis'
    LABORATORY = 'Lab'

    FORMAT_CHOICES = (
        (LECTURE, 'Lecture'),
        (DISCUSSION, 'Discussion'),
        (LABORATORY, 'Laboratory')
    )

    section_id = models.CharField(max_length=3)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.PROTECT)
    format = models.CharField(max_length=3, choices=FORMAT_CHOICES, default=LECTURE)
    monday = models.BooleanField()
    tuesday = models.BooleanField()
    wednesday = models.BooleanField()
    thursday = models.BooleanField()
    friday = models.BooleanField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=50)
    enrollment = models.IntegerField()
    max_enrollment = models.IntegerField()

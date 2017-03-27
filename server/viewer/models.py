from django.db import models

from datetime import time


class Department(models.Model):
    dept_id = models.CharField(max_length=4, primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    class Meta:
        unique_together = (('name', 'dept'),)

    name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department, on_delete=models.PROTECT)

    @staticmethod
    def add_if_missing(dept, name):
        instructor = Instructor.objects.filter(dept=dept, name=name).first()
        if not instructor:
            instructor = Instructor(name=name)
            instructor.dept = dept
        return instructor

    def __str__(self):
        return self.name + '(' + self.dept.dept_id + ')'


class Course(models.Model):
    class Meta:
        unique_together = (('dept', 'number'),)

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    number = models.CharField(max_length=4)
    title = models.CharField(max_length=100)
    hours = models.DecimalField(max_digits=3, decimal_places=1)

    @staticmethod
    def add_if_missing(dept, number, title, hours):
        course = Course.objects.filter(dept=dept, number=number).first()
        if not course:
            course = Course(number=number, title=title, hours=hours)
            course.dept = dept
        return course

    def __str__(self):
        return self.dept.dept_id + ' ' + self.number


class Section(models.Model):
    class Meta:
        unique_together = (('section_id', 'course', 'semester', 'year'),)

    FALL = 'Fall'
    WINTER = 'Winter'
    SPRING = 'Spring'
    SUMMER = 'Summer'

    SEMESTER_CHOICES = (
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
        (SPRING, 'Spring'),
        (SUMMER, 'Summer')
    )

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
    semester = models.CharField(max_length=6, choices=SEMESTER_CHOICES)
    year = models.IntegerField()

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

    enrollment = models.IntegerField(default=0)
    max_enrollment = models.IntegerField()

    @staticmethod
    def add_if_missing(section_id, course, semester, year, instructor, format, days,
                       start_time, end_time, location, enrollment, max_enrollment):
        section = Section.objects.filter(section_id=section_id, course=course, semester=semester, year=year).first()
        if not section:
            section = Section(section_id=section_id, format=format, semester=semester, year=year,
                              monday=days[0], tuesday=days[1], wednesday=days[2], thursday=days[3], friday=days[4],
                              location=location, enrollment=enrollment, max_enrollment=max_enrollment)
            section.course = course
            section.instructor = instructor
            section.start_time = time(hour=int(start_time[:-2]), minute=int(start_time[-2:]))
            section.end_time = time(hour=int(end_time[:-2]), minute=int(end_time[-2:]))
        return section

    def __str__(self):
        return str(self.course) + '-' + self.section_id


class RequirementSet(models.Model):
    pass


class Degree(RequirementSet):
    class Meta:
        unique_together = (('dept', 'degree_type'),)

    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    degree_type = models.CharField(max_length=10)

    def __str__(self):
        return self.degree_type + ' ' + self.dept.dept_id


class SchoolArea(RequirementSet):
    school = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.school


class CourseSet(models.Model):
    req_set = models.ForeignKey(RequirementSet, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    choices = models.IntegerField(default=1)

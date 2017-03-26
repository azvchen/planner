from django.contrib import admin

from viewer.models import Department, Course, RequirementSet, Degree, SchoolArea, CourseSet


class CourseInline(admin.TabularInline):
    model = Course
    extra = 3


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('dept_id', 'name')
    inlines = [CourseInline]


class CourseSetInline(admin.TabularInline):
    filter_horizontal = ('courses',)
    model = CourseSet
    extra = 0


class DegreeAdmin(admin.ModelAdmin):
    inlines = [CourseSetInline]


class SchoolAreaAdmin(admin.ModelAdmin):
    inlines = [CourseSetInline]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Degree, DegreeAdmin)
admin.site.register(SchoolArea, SchoolAreaAdmin)

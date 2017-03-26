from django.contrib import admin

from viewer.models import Department, Course, RequirementSet, Degree, SchoolArea, CourseSet


class CourseInline(admin.TabularInline):
    model = Course
    extra = 3
    ordering = ('number',)


class DepartmentAdmin(admin.ModelAdmin):
    inlines = [CourseInline]
    list_display = ('dept_id', 'name')
    list_editable = ('name',)
    ordering = ('dept_id',)
    search_fields = ('dept_id', 'name')


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

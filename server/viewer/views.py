from django.shortcuts import render

from viewer.models import Section


def index(request):
    return sections(request)


def sections(request):
    section_list = Section.objects.all()
    return render(request, 'viewer/sections.html', {'section_list': section_list})


def requirements(request):
    return sections(request)

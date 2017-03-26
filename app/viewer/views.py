from django.shortcuts import render

from viewer.models import Section


def index(request):
    section_list = Section.objects.all()
    return render(request, 'viewer/index.html', {'section_list': section_list})
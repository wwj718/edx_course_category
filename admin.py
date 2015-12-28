#!/usr/bin/env python
# encoding: utf-8

from django.contrib import admin
from .models import HomeCourse ,  HomeCourseCategory

class HomeCourseAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'category','course_id')
    list_display = ('name', 'category', 'course_id')

admin.site.register(HomeCourse,HomeCourseAdmin)

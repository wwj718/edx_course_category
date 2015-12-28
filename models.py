#!/usr/bin/env python
# encoding: utf-8

from django.db import models
from django.contrib.auth.models import User

#idea：使用tag？

class HomeCourseCategory(models.Model):
    pass

class HomeCourse(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'课程名称')
    course_id = models.CharField(max_length=100, verbose_name=u'课程id') #增加一个验证规则
    #url = models.URLField(verbose_name=u"课程链接") #使用course_id呢还是直接只用连接
    category =  models.ForeignKey(HomeCourseCategory,blank=True,null=True, verbose_name=u'学科分类') #更多的分类应该是HomeCourseCategory与其他类别的归属关系。
    teacher_pic = models.ImageField(blank=True,upload_to='teacher_pic', verbose_name=u'老师照片')
    teacher_intro = models.CharField(max_length=100, verbose_name=u'教师简介')
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)
    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['-create_time']
        verbose_name_plural = verbose_name = u"课程"


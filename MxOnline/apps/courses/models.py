from django.db import models

from MxOnline.apps.users.models import BaseModel
from MxOnline.apps.organizations.models import Teacher, CourseOrg

# 设计表结构有几个重要的点
# 实体的具体字段
# 每个字段的类型，是否必填
"""
实体1 <关系> 实体2
课程 章节 视频 课程资源
"""


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="Teacher")
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE,
                                   verbose_name="Course Organization")
    name = models.CharField(verbose_name="Course Name", max_length=50)
    desc = models.CharField(verbose_name="Course Description", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="Learn Times (mins)")
    degree = models.CharField(verbose_name="Degree", choices=(("cj", "Easy"), ("zj", "Medium"), ("gj", "Hard")),
                              max_length=2)
    students = models.IntegerField(default=0, verbose_name='Number of Students')
    fav_nums = models.IntegerField(default=0, verbose_name='Number of Favorites')
    click_nums = models.IntegerField(default=0, verbose_name="Number of Clicks")
    notice = models.CharField(verbose_name="Course Announcement", max_length=300, default="")
    category = models.CharField(default=u"后端开发", max_length=20, verbose_name="Course Category")
    tag = models.CharField(default="", verbose_name="Course Tag", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="MUSTKNOW")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="Teacher Tell")
    is_classics = models.BooleanField(default=False, verbose_name="Classical")
    # detail = UEditorField(verbose_name="Course Details", width=600, height=300, imagePath="courses/ueditor/images/", filePath="courses/ueditor/files/", default="")
    detail = models.TextField(verbose_name="Course Details")
    is_banner = models.BooleanField(default=False, verbose_name="isBanner")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="Course Image", max_length=100)

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name

    # 返回当前课程的章节数
    def lesson_nums(self):
        return self.lesson_set.all().count()

    def __str__(self):
        return self.name


class CourseTag(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name="Course")
    tag = models.CharField(max_length=100, verbose_name="Tag Name")

    class Meta:
        verbose_name = "课程标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE,
                               verbose_name="Course")  # on_delete表示对应的外键数据被删除后，当前的数据应该怎么办
    name = models.CharField(max_length=100, verbose_name="Lesson Name")
    learn_times = models.IntegerField(default=0, verbose_name="Course Duration")

    class Meta:
        verbose_name = "课程章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="Chapter", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"Video Name")
    learn_times = models.IntegerField(default=0, verbose_name=u"Duration")
    url = models.CharField(max_length=1000, verbose_name=u"URL")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    name = models.CharField(max_length=100, verbose_name=u"Name")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="File Location", max_length=200)

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

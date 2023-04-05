from django.db import models

from django.contrib.auth import get_user_model

from MxOnline.apps.users.models import BaseModel
from MxOnline.apps.courses.models import Course

UserProfile = get_user_model()


# 用户可以不必登陆就能留言
class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="Name")
    mobile = models.CharField(max_length=11, verbose_name="Phone Number")
    course_name = models.CharField(max_length=50, verbose_name="Course Name")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


# 用户必须登陆才能评论
class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="User")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")
    comments = models.CharField(max_length=200, verbose_name="Comments")

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="User")
    fav_id = models.IntegerField(verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1,
                                   verbose_name="fav type")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="User")
    message = models.CharField(max_length=200, verbose_name="Message")
    has_read = models.BooleanField(default=False, verbose_name="Has Read")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


# 记录每个用户注册了什么课程
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="User")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Course")

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name

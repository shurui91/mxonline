from django.db import models

from MxOnline.apps.users.models import BaseModel


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u"City Name")
    desc = models.CharField(max_length=200, verbose_name=u"Description")

    class Meta:
        verbose_name = "城市"
        verbose_name_plural = "城市"

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    name = models.CharField(max_length=50, verbose_name="Organization Name")
    desc = models.TextField()
    tag = models.CharField(default="Nationwide Famous", max_length=10, verbose_name="Org Tag")
    category = models.CharField(default="pxjg", verbose_name="Organization Type", max_length=4,
                                choices=(("pxjg", "Organization"), ("gr", "Individual"), ("gx", "University")))
    click_nums = models.IntegerField(default=0, verbose_name="Number of Clicks")
    fav_nums = models.IntegerField(default=0, verbose_name="Number of Favorites")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="Organization Address")
    students = models.IntegerField(default=0, verbose_name="Number of Students")
    course_nums = models.IntegerField(default=0, verbose_name="Number of Courses")
    is_auth = models.BooleanField(default=False, verbose_name="Is this an authenticated organization?")
    is_gold = models.BooleanField(default=False, verbose_name="Is this a golden organization?")
    # 如果以后需要添加新的城市
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="City")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    # user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="用户")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="Organization")
    name = models.CharField(max_length=50, verbose_name=u"Teacher's Name")
    work_years = models.IntegerField(default=0, verbose_name="YOE")
    work_company = models.CharField(max_length=50, verbose_name="Employer")
    work_position = models.CharField(max_length=50, verbose_name="Position")
    points = models.CharField(max_length=50, verbose_name="Characters")
    click_nums = models.IntegerField(default=0, verbose_name="Clicks")
    fav_nums = models.IntegerField(default=0, verbose_name="Favorites")
    age = models.IntegerField(default=18, verbose_name="Age")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="Avatar", max_length=100)

    class Meta:
        verbose_name = "教师"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()

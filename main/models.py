

from ast import Sub
from operator import truediv
import profile
from pydoc import describe
from statistics import mode
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract=True

class Profile(models.Model):
    ROLES = [
        ('student', 'student',),
        ('teacher',  'teacher')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    role = models.CharField(max_length=20, blank=True, choices=ROLES)
    bio = models.CharField(max_length=255, blank=True, null=True)

    
    def is_student(self):
        if self.role == self.ROLES[0][0]:
            return True
        return False

    def __repr__(self) -> str:
        return "%s <%s>" % (self.user.get_full_name(), self.user.email)

    def __str__(self) -> str:
        return "%s <%s>" % (self.user.get_full_name(), self.user.email)




class Klass(TimeStampMixin):
    name = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=255, null=True, blank=True)

    # subjects = models.ManyToManyField(to=Subject, related_name='klasses')

    class Meta:
        db_table = 'classes'
        verbose_name = "class"
        verbose_name_plural = 'classes'

    def __str__(self) -> str:
        return self.name

class Teacher(TimeStampMixin):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "%s" % (self.profile.user.get_full_name())

class Subject(TimeStampMixin):
    name = models.CharField(blank=False, null=False, max_length=50)
    description = models.CharField(max_length=255, null=True, blank=True)
    klass = models.ForeignKey(to=Klass, related_name="subjects", verbose_name="class", on_delete=models.CASCADE)
    teacher = models.ForeignKey(to=Teacher, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name + " " + self.klass.name


class Student(models.Model):
    profile = models.OneToOneField(to=Profile, on_delete=models.CASCADE)
    klass = models.ForeignKey(to=Klass, related_name="students", verbose_name="class", on_delete=models.SET_NULL, null=True)
    uid = models.CharField(verbose_name="UID", max_length=12, null=False, blank=False)

    def __str__(self) -> str:
        return "%s <%s>" %(self.profile.user.get_full_name(), self.klass.name)

class Assignment(TimeStampMixin):
    subject = models.ForeignKey(to=Subject, on_delete=models.CASCADE)
    due_date = models.DateTimeField(null=True, blank=False)
    marks = models.FloatField()
    title = models.CharField(blank=False, null=False, max_length=255)
    desciption = models.TextField(blank=False, null=False)

    def __str__(self) -> str:
        return self.title
    
class Submission(TimeStampMixin):
    assignment = models.ForeignKey(to=Assignment, on_delete=models.CASCADE)
    solution = models.CharField(max_length=255, blank=False, null=False)
    student = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    marks_obtained = models.FloatField(null=True, blank=True)
    checked = models.BooleanField(default=False)
    checked_at = models.DateTimeField(null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)


# to register admin models 
ADMIN_MODELS = [Profile, Klass, Student, Subject, Teacher,  Assignment, Submission]











    
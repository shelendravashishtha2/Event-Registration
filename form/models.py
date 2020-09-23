# Create your models here.
import datetime

from django.db import models
from django.utils.timezone import now


# Event Models
class AvailableFeatures(models.Model):
    feature_name = models.CharField(max_length=50, blank=False, null=False)
    current_status = models.BooleanField(default=True)

    def __str__(self):
        return self.feature_name


class Event(models.Model):
    event_name = models.CharField(max_length=100, blank=False)
    current_status = models.BooleanField(default=True)
    event_code = models.CharField(max_length=10, blank=False)
    event_venue = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
    drive_link = models.CharField(max_length=300, blank=True)
    winner = models.CharField(max_length=250, blank=True)
    first_runner = models.CharField(max_length=250, blank=True)
    second_runner = models.CharField(max_length=250, blank=True)
    pub_date = models.DateTimeField(default=now())
    warn = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.event_name

    def was_published_recently(self):
        return self.pub_date > now - datetime.timedelta(days=1)


# Branch Model
class Branch(models.Model):
    branch_name = models.CharField(max_length=100, primary_key=True)
    abbr = models.CharField(max_length=3)

    def __str__(self):
        return self.branch_name


# Student Information Model
class Student(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200, blank=False)
    email_id = models.EmailField(max_length=70, blank=False)
    mobile_number = models.CharField(max_length=10, blank=False)
    roll_no = models.CharField(max_length=15, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return self.student_name


class Blog(models.Model):
    student_name = models.CharField(max_length=200, null=False, blank=False)
    roll_no = models.CharField(max_length=15, null=False)
    subject = models.CharField(max_length=200, null=False)
    suggestion = models.TextField(null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name

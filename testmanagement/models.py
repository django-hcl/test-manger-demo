from django.db import models
from django.contrib.auth.models import User


class test(models.Model):
    TestId =models.AutoField(primary_key=True)
    TestName = models.CharField(max_length=500)
    Description =  models.CharField(max_length=500)
    CreatedBy = models.CharField(max_length=500)
    CreatedOn = models.DateTimeField(editable=False)
    Duration  = models.DurationField(editable=False)
    SectionId  = models.IntegerField(max_length=3)

    def __str__(self):
        return str(self.TestName)

class testreports(models.Model):
    ReportId =models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    DateAttended = models.DateField(editable=False)
    AttemptsCount = models.IntegerField(max_length=3)
    StartAt	 = models.DateTimeField(editable=False)
    EndAt = models.DateTimeField(editable=False)
    Result = models.CharField(max_length=500)

    def __str__(self):
        return str(self.ReportId)

class testsection(models.Model):
    SectionId =models.AutoField(primary_key=True)
    SectionName = models.CharField(max_length=500)
    CreatedBy = models.CharField(max_length=500)
    CreatedOn = models.DateTimeField(editable=False)

    def __str__(self):
        return str(self.SectionName)

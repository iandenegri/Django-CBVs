from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    """(School description)"""

    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location=models.CharField(max_length=256)


    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"School"


    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})


class Student(models.Model):
    """(Student description)"""

    name=models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school=models.ForeignKey(School,related_name='students',on_delete=models.PROTECT)


    class Admin:
        list_display = ('',)
        search_fields = ('',)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return u"Student"

from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator

# Create your models here.
class student(models.Model):
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    slug = models.SlugField(max_length = 250, null = True, blank = True, unique=True)

    def __str__(self):
        return self.name

# To create slug url
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = student)


class studentClass(models.Model):
    YEAR_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )

    SEMESTER_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
    )

    student = models.ForeignKey(student, related_name="class_details", on_delete=models.CASCADE)
    year = models.CharField(max_length=100, choices = YEAR_CHOICES)
    semester = models.CharField(max_length=100, choices = SEMESTER_CHOICES)
    department = models.CharField(max_length=100)

# from docs

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)

class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    duration = models.IntegerField()

    class Meta:
        unique_together = ['album', 'order']
        ordering = ['order']

    def __str__(self):
        return '%d: %s' % (self.order, self.title)
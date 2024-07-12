from django.db import models
from django.contrib.auth.models import User
from datetime import datetime,timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
# from django.utils import timezone
# import datetime
# import logging

# logger = logging.getLogger(__name__)

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.IntegerField(validators=[MaxValueValidator(2147483647)])
    category = models.CharField(max_length=50)

    # def save(self, *args, **kwargs):
    #     logger.debug("Saving book: %s", self.name)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name) + " ["+str(self.isbn)+']'

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # first_name = models.CharField(max_length=200)
    # last_name = models.OneToOneField(Student, on_delete=models.CASCADE)
    id = models.PositiveIntegerField(primary_key=True)
    classroom = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="", blank=True)

    def __str__(self):
        return str(self.user) + " ["+str(self.branch)+']' + " ["+str(self.classroom)+']' + " ["+str(self.roll_no)+']'


def expiry():
    return datetime.today() + timedelta(days=14)
class IssuedBook(models.Model):
    student_id = models.CharField(max_length=100, blank=True) 
    isbn = models.IntegerField(validators=[MinValueValidator(10),MaxValueValidator(13)])
    issued_date = models.DateField(auto_now=True)
    expiry_date = models.DateField(default=expiry)

    # def save(self, *args, **kwargs):
    #     if not self.expiry_date:
    #         self.expiry_date = timezone.now().date() + datetime.timedelta(days=14)
    #     super().save(*args, **kwargs)
from email.mime import image
from statistics import mode
from django.db import models
import pywhatkit
import datetime
# Create your models here.
class Phones(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    is_send = models.BooleanField( blank=True, null=True, default=False)
    is_subscribed = models.BooleanField( blank=True, null=True, default=False)

    def __str__(self):
        return self.phone_number

class News(models.Model):
    title = models.CharField(max_length=150, blank=True, null=True)
    text = models.CharField(max_length=150, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    is_send = models.BooleanField( blank=True, null=True, default=False)
    created = models.DateTimeField(auto_now_add=True)
    image =  models.FileField(blank=True, null=True)
    def __str__(self):
        return self.title


class FAQ(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    question = models.CharField(max_length=200, blank=True, null=True)
    answer = models.CharField(max_length=200, blank=True, null=True)
    state = models.BooleanField( blank=True, null=True, default=False)
    def save(self, *args, **kwargs):
        if self.state == True:
            now = datetime.datetime.now()
            pywhatkit.sendwhatmsg(self.phone_number, self.answer, now.hour, now.minute+1,  10, True, 2)
            self.state = True
        # change1(self.userid,self.answer)
        # print(self.student,self.question,self.answer)
        super(FAQ, self).save(*args, **kwargs)
    def __str__(self):
        return self.question
    
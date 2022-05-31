from django.db import models
import datetime
import pywhatkit

# class FAQ(models.Model):
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     question = models.CharField(max_length=200, blank=True, null=True)
#     answer = models.CharField(max_length=200, blank=True, null=True)
#     state = models.BooleanField( blank=True, null=True, default=False)
#     def save(self, *args, **kwargs):
#         now = datetime.datetime.now()
#         pywhatkit.sendwhatmsg(self.phone_number, self.answer, now.hour, now.minute+1,  10, True, 2)
#         self.state = True
#         # change1(self.userid,self.answer)
#         # print(self.student,self.question,self.answer)
#         super(FAQ, self).save(*args, **kwargs)
#     def __str__(self):
#         return self.question

from django.contrib import admin
from django.shortcuts import redirect
from requests import request
from .models import *
import pywhatkit

from django.http import HttpResponse


@admin.action(description='Начать рассылку')
def rassylka_starter(modeladmin, request,queryset):
    temp = 0
    for i in queryset:
        temp = i.id
    return redirect(f'/ras/{i.id}')
    



class Filter(admin.ModelAdmin):
    list_display = ('title','text','region','city','is_send','created')
    list_filter = ('is_send','region','city','created')
    actions = [rassylka_starter]


class Filter_Phones(admin.ModelAdmin):
    list_display = ('phone_number','name','region','is_send','is_subscribed')
    list_filter = ('region','is_send','is_subscribed')
admin.site.register(News,Filter)
admin.site.register(Phones,Filter_Phones)


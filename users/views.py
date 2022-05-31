from django.http import HttpResponse
from django.shortcuts import redirect, render
import pywhatkit
from time import sleep
import pyautogui as pt
from time import sleep
import pyperclip
import random
from whats_bot.settings import MEDIA_ROOT, MEDIA_URL
from django.contrib.auth.decorators import login_required

from .models import *

    
# Create your views here.
@login_required
def rassylka(request):
    phone = Phones.objects.filter(is_send = False)
    phones = []
    for i in phone:
        phones.append(i.phone_number)
    news = News.objects.get(title = "Test")

    for phone in phones:
        pywhatkit.sendwhats_image(phone, "/Users/maagauiya/Desktop/kazareo_whats_bot/ui_ux.jpeg", news.text, 7, True, 2)
        phon1 = Phones.objects.get(phone_number = phone)
        phon1.is_send = True
        phon1.save()

@login_required
def news(request,pk):

    news = News.objects.get(id =pk)
    phone = Phones.objects.filter(is_subscribed = True)
    phones = []
    for k in phone:
        phones.append(k.phone_number)
    for phone in phones:
        pywhatkit.sendwhats_image(phone, news.image.path, news.text, 7, True, 2)

        news.is_send = True
        news.save()
    return render(request,'users/done.html')
        

def page_tort(request,exception):
    context = {}
    response = render(request, "users/error.html", context=context)
    response.status_code = 404
    return response























# def check_messages():
#     pt.moveTo(x+100, y - 50)
#     while True:
#         #Постоянно чекать зеленую точку и новые сообщения
#         try:
#             position = pt.locateOnScreen("/Users/maagauiya/Desktop/kazareo_whats_bot/whats_bot/media/green.png", confidence = .7)
#             if position is not None:
#                 pt.moveTo(position)
#                 pt.moveRel(-100, 0)
#                 pt.click()
#                 sleep(.5)

#         except(Exception):
#             print("Нет новых сообщений")

#         if pt.pixelMatchesColor(int(x+100), int(y-50), (255,255,255), tolerance=10):
#             print("Он белый")
#             processed_message = process_response(get_message())
#             post_response(processed_message)
#         else:
#             print("Нет новых сообщений покамись")
#         sleep(5)

# position1 = pt.locateOnScreen("/Users/maagauiya/Desktop/kazareo_whats_bot/whats_bot/media/smiley.png", confidence = .6)
# x = position1[0]
# y = position1[1]

# #Получать сообщения
# def get_message():
#     global x,y
#     position = pt.locateOnScreen("/Users/maagauiya/Desktop/kazareo_whats_bot/whats_bot/media/smiley.png", confidence = .6)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x, y, duration=.5)
#     pt.moveTo(x + 110, y - 60, duration=.5)
#     pt.tripleClick()
#     pt.rightClick()
#     pt.moveRel(20, -200)
#     pt.click()
#     whatsapp_message = pyperclip.paste()
#     pt.click()
#     print("Сообщение получено: " + whatsapp_message)

#     return whatsapp_message

# #Писать ответ
# def post_response(message):
#     global x,y
#     position = pt.locateOnScreen("/Users/maagauiya/Desktop/kazareo_whats_bot/whats_bot/media/smiley.png", confidence = .6)
#     x = position[0]
#     y = position[1]
#     pt.moveTo(x + 200, y+20, duration=0.5)
#     pt.click()
    
#     pyperclip.copy(message)
#     # pt.typewrite(message, interval=.01)
#     pt.hotkey('ctrl', 'v')
#     pt.typewrite("\n", interval=.01)


# #Думать про ответ
# def process_response(message):
#     random_number = random.randrange(3)

#     if "?" in str(message).lower():  
#         return "Я ничего не знаю"

#     else:
#         if random_number == 0:
#             return "Добрый день"
#         elif random_number == 1:
#             return "Доброй ночи" 
#         else:
#             return "Хай хай хай"
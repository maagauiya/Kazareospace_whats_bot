from django.shortcuts import render
from django.http import HttpResponse
import pyautogui as pt
from time import sleep
import pyperclip
import random
from users.models import *

def index(request):
    pt.moveTo(x+100, y - 50)
    while True:
        #Постоянно чекать зеленую точку и новые сообщения
        try:
            position = pt.locateOnScreen(r"C:\Users\aldyk\OneDrive\Desktop\flutter\bot\green.png", confidence = .7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("Нет новых сообщений")

        if pt.pixelMatchesColor(int(x+100), int(y-50), (255,255,255), tolerance=10):
            # print("Он белый")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("Нет новых сообщений покамись")
        sleep(2)

    return HttpResponse("Hello, world. You're at the polls index.")


sleep(3)

position1 = pt.locateOnScreen(r"C:\Users\aldyk\OneDrive\Desktop\flutter\bot\smiley.png", confidence = .6)
x = position1[0]
y = position1[1]

#Получать сообщения
def get_message():
    global x,y
    position = pt.locateOnScreen(r"C:\Users\aldyk\OneDrive\Desktop\flutter\bot\smiley.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y)
    pt.moveTo(x + 110, y - 60)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(20, -200)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Сообщение получено: " + whatsapp_message)

    return whatsapp_message

#Писать ответ
def post_response(message):
    global x,y
    position = pt.locateOnScreen(r"C:\Users\aldyk\OneDrive\Desktop\flutter\bot\smiley.png", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y+20)
    pt.click()
    
    pyperclip.copy(message)
    # pt.typewrite(message, interval=.01)
    pt.hotkey('ctrl', 'v')
    pt.typewrite("\n", interval=.01)


#Думать про ответ
def process_response(message):
    random_number = random.randrange(3)

    if "?" in str(message).lower():
        pt.moveTo(x+100, y - 770)
        pt.click()
        pt.moveRel(850, 330, duration=.2)
        pt.doubleClick()
        pt.hotkey('ctrl', 'c')
        phone_n = pyperclip.paste()
        pt.moveRel(-210, -330)
        pt.click()
        faq = FAQ.objects.create(
            phone_number = "+77719870019",
            question = message,
            answer = "",
            state = False

        )
        # faq.save()
        faq.save()
        
        return "Вам ответит наш оператор"

    else:
        if random_number == 0:
            return "Добрый день"
        elif random_number == 1:
            return "Доброй ночи" 
        else:
            return "Хай хай хай"

#Проверять сообщения
def check_messages():
    pt.moveTo(x+100, y - 50)
    while True:
        #Постоянно чекать зеленую точку и новые сообщения
        try:
            position = pt.locateOnScreen(r"C:\Users\aldyk\OneDrive\Desktop\flutter\bot\green.png", confidence = .7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)

        except(Exception):
            print("Нет новых сообщений")

        if pt.pixelMatchesColor(int(x+100), int(y-50), (255,255,255), tolerance=10):
            print("Он белый")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("Нет новых сообщений покамись")
        sleep(5)


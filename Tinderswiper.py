import pyautogui
import webbrowser
import time

input("This program will open up Tinder and do the right swiping for you\nPress enter to start Program")
a=int(input('How many people do you want to swipe?\n'))
webbrowser.open('https://www.tinder.com',new = 1,autoraise = True)
time.sleep(5)
i=0
while i<a:
    pyautogui.press('right')
    i=i+1
    time.sleep(1)
    print('swiped person number',i)
from pyautogui import typewrite, hotkey
from os import system
from time import sleep
system('start cmd')
sleep(1)
typewrite('python -m webbrowser -t "https://www.youtube.com/watch?v=a7_jS1XqvVg&t=4s"')
hotkey('enter')

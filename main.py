import pyautogui as pg
import time

messages = ["Hola", "Esto es un BOT", "Como estas?", "Tene un lindo dia", "Perdon por ser molesto :c"]

while True:
    for i in messages:
        pg.moveTo(600, 700)
        pg.click()
        pg.write(i)
        pg.moveTo(1320, 700)
        pg.click()
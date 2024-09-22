from tkinter import *
import tkinter.font as FONT
import RPi.GPIO as GPIO
from gpiozero import LED

GPIO.setmode(GPIO.BCM)

red_led = LED(17)
blue_led = LED(27)
green_led = LED(22)

win = Tk()
win.title("LED FLASHER")
win.geometry("400x300")
win.configure(bg='#f0f0f0')  
myFont = FONT.Font(family='Helvetica', size=14, weight='bold')

def redLedToggle():
    if red_led.is_lit:
        red_led.off()
        redLedButton["text"] = "RED LED ON"
    else:
        red_led.on()
        redLedButton["text"] = "RED LED OFF"
    blue_led.off()
    blueLedButton["text"] = "BLUE LED ON"
    green_led.off()
    greenLedButton["text"] = "GREEN LED ON"

def blueLedToggle():
    if blue_led.is_lit:
        blue_led.off()
        blueLedButton["text"] = "BLUE LED ON"
    else:
        blue_led.on()
        blueLedButton["text"] = "BLUE LED OFF"
    red_led.off()
    redLedButton["text"] = "RED LED ON"
    green_led.off()
    greenLedButton["text"] = "GREEN LED ON"

def greenLedToggle():
    if green_led.is_lit:
        green_led.off()
        greenLedButton["text"] = "GREEN LED ON"
    else:
        green_led.on()
        greenLedButton["text"] = "GREEN LED OFF"
    red_led.off()
    redLedButton["text"] = "RED LED ON"
    blue_led.off()
    blueLedButton["text"] = "BLUE LED ON"

def close():
    GPIO.cleanup()
    win.destroy()


redLedButton = Button(win, text="RED LED ON", font=myFont, command=redLedToggle, bg='red', fg='white', height=2, width=20)
redLedButton.grid(row=0, column=1, padx=20, pady=10)

blueLedButton = Button(win, text="BLUE LED ON", font=myFont, command=blueLedToggle, bg='blue', fg='white', height=2, width=20)
blueLedButton.grid(row=1, column=1, padx=20, pady=10)

greenLedButton = Button(win, text="GREEN LED ON", font=myFont, command=greenLedToggle, bg='green', fg='white', height=2, width=20)
greenLedButton.grid(row=2, column=1, padx=20, pady=10)

exitButton = Button(win, text="EXIT", font=myFont, command=close, bg='yellow', height=2, width=20)
exitButton.grid(row=3, column=1, padx=20, pady=10)

# Add a title label to the top
titleLabel = Label(win, text="LED Flasher Control", font=("Helvetica", 16, 'bold'), bg='#f0f0f0')
titleLabel.grid(row=0, column=0, padx=20, pady=10, sticky=W)

win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()

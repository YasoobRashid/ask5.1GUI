from tkinter import *
import tkinter.font as FONT
import RPi.GPIO as GPIO
from gpiozero import LED
# Set the GPIO pin numbering mode to BCM (Broadcom)
GPIO.setmode(GPIO.BCM)

# Initialize LED objects for each color LED on specified GPIO pins
red_led = LED(17)                         # Red LED connected to GPIO pin 17
blue_led = LED(27)                        # Blue LED connected to GPIO pin 27
green_led = LED(22)                       # Green LED connected to GPIO pin 22

# Create the main window for the GUI application
win = Tk()
win.title("LED FLASHER")                  # Set the window title
win.geometry("400x300")                   # Set the window size
win.configure(bg='#f0f0f0')               # Set the background color of the window
myFont = FONT.Font(family='Helvetica', size=14, weight='bold')  # Define a font for buttons

# Function to toggle the red LED on and off
def redLedToggle():
    if red_led.is_lit:                    # Check if the red LED is currently on
        red_led.off()                     # Turn the red LED off
        redLedButton["text"] = "RED LED ON"  # Update button text to indicate LED is off
    else:
        red_led.on()                      # Turn the red LED on
        redLedButton["text"] = "RED LED OFF" # Update button text to indicate LED is on
    blue_led.off()                        # Turn off the blue LED
    blueLedButton["text"] = "BLUE LED ON"  # Update button text for blue LED
    green_led.off()                       # Turn off the green LED
    greenLedButton["text"] = "GREEN LED ON" # Update button text for green LED

# Function to toggle the blue LED on and off
def blueLedToggle():
    if blue_led.is_lit:                   # Check if the blue LED is currently on
        blue_led.off()                    # Turn the blue LED off
        blueLedButton["text"] = "BLUE LED ON"  # Update button text to indicate LED is off
    else:
        blue_led.on()                     # Turn the blue LED on
        blueLedButton["text"] = "BLUE LED OFF" # Update button text to indicate LED is on
    red_led.off()                         # Turn off the red LED
    redLedButton["text"] = "RED LED ON"    # Update button text for red LED
    green_led.off()                       # Turn off the green LED
    greenLedButton["text"] = "GREEN LED ON" # Update button text for green LED

# Function to toggle the green LED on and off
def greenLedToggle():
    if green_led.is_lit:                  # Check if the green LED is currently on
        green_led.off()                   # Turn the green LED off
        greenLedButton["text"] = "GREEN LED ON" # Update button text to indicate LED is off
    else:
        green_led.on()                    # Turn the green LED on
        greenLedButton["text"] = "GREEN LED OFF" # Update button text to indicate LED is on
    red_led.off()                         # Turn off the red LED
    redLedButton["text"] = "RED LED ON"    # Update button text for red LED
    blue_led.off()                        # Turn off the blue LED
    blueLedButton["text"] = "BLUE LED ON"  # Update button text for blue LED

# Function to clean up GPIO and close the window
def close():
    GPIO.cleanup()                         # Clean up GPIO settings
    win.destroy()                          # Destroy the window

# Create buttons for each LED control and layout in the window
redLedButton = Button(win, text="RED LED ON", font=myFont, command=redLedToggle, bg='red', fg='white', height=2, width=20)
redLedButton.grid(row=0, column=1, padx=20, pady=10)  # Place the red LED button

blueLedButton = Button(win, text="BLUE LED ON", font=myFont, command=blueLedToggle, bg='blue', fg='white', height=2, width=20)
blueLedButton.grid(row=1, column=1, padx=20, pady=10)  # Place the blue LED button

greenLedButton = Button(win, text="GREEN LED ON", font=myFont, command=greenLedToggle, bg='green', fg='white', height=2, width=20)
greenLedButton.grid(row=2, column=1, padx=20, pady=10)  # Place the green LED button

# Create an exit button to close the application
exitButton = Button(win, text="EXIT", font=myFont, command=close, bg='yellow', height=2, width=20)
exitButton.grid(row=3, column=1, padx=20, pady=10)  # Place the exit button

# Add a title label at the top of the window
titleLabel = Label(win, text="LED Flasher Control", font=("Helvetica", 16, 'bold'), bg='#f0f0f0')
titleLabel.grid(row=0, column=0, padx=20, pady=10, sticky=W)  # Place the title label

# Set the protocol for closing the window to call the close function
win.protocol("WM_DELETE_WINDOW", close)
win.mainloop()  # Start the main loop to display the GUI and wait for user interaction

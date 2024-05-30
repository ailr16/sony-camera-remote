import RPi.GPIO as GPIO
import time
import tkinter

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

#while True:
#    GPIO.output(8, GPIO.HIGH)
#    time.sleep(1)
#    GPIO.output(8, GPIO.LOW)
#    time.sleep(1)

def led_on():
    GPIO.output( 8, GPIO.HIGH )

def led_off():
    GPIO.output( 8, GPIO.LOW )

window = tkinter.Tk()
window.title("Basic HMI")

label = tkinter.Label(window, text="Basic HMI using Raspberry Pi 4 and Yocto image")
label.pack()

button_on = tkinter.Button(window, text="LED On", command = lambda: led_on())
button_off = tkinter.Button(window, text="LED Off", command = lambda: led_off())

button_on.pack()
button_off.pack()

window.mainloop()

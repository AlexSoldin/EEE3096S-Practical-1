#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Alex Soldin
Student Number: SLDALE003
Prac: 1
Date: 23/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO

#setup GPIO
led1 = 17 #physical pin 11
led2 = 23 #physical pin 16
led3 = 24 #physical pin 18
buttonUp = 27 #physical pin 13
buttonDown = 22 #physical pin 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(buttonUp, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonDown, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# global variables
values = ["000","001","010","011","100","101","110","111"]
global count
count = 0

# methods
def increment(channel):
    global count
    if count==7:
        count=0
    else:
        count+=1
    GPIO.output(led1, int(values[count][0]))
    GPIO.output(led2, int(values[count][1]))
    GPIO.output(led3, int(values[count][2]))
    print(values[count])

def decrement(channel):
    global count
    if count==0:
        count=7
    else:
        count-=1
    GPIO.output(led1, int(values[count][0]))
    GPIO.output(led2, int(values[count][1]))
    GPIO.output(led3, int(values[count][2]))
    print(values[count])

# interrupts
GPIO.add_event_detect(buttonUp, GPIO.FALLING, callback=increment,bouncetime=100)
GPIO.add_event_detect(buttonDown, GPIO.FALLING, callback=decrement,bouncetime=100)

# Logic that you write
def main():
    x = 3
    #print("write your logic here")


# Only run the functions if
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

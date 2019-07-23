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
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(buttonUp, GPIO.IN)
GPIO.setup(buttonDown, GPIO.IN)

# Logic that you write
def main():
    print("write your logic here")


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

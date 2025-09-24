#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Set the GPIO numbering mode (BCM uses GPIO numbers, not physical pin numbers)
GPIO.setmode(GPIO.BCM)

# Define the PWM pin
pwm_pin = 18

# Set up the pin as an output
GPIO.setup(pwm_pin, GPIO.OUT)

# Create a PWM object on the pin with a frequency of 1 kHz (1000 Hz)
pwm = GPIO.PWM(pwm_pin, 1)

# Start the PWM with a 50% duty cycle (50 means 50%)
pwm.start(50)

print("PWM signal is running on GPIO 18 at 1 kHz, 75% duty cycle.")
print("Press Ctrl+C to stop.")

try:
    # Keep the script running
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO settings when Ctrl+C is pressed
    print("\nStopping PWM.")
    pwm.stop()
    GPIO.cleanup()

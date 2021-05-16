import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


def main():
    """
    This file is used to test the hall sensor using Python
    """
    GPIO.setup(14, GPIO.IN)

    while True:
        print(GPIO.input(14))
        time.sleep(0.5)


if __name__ == '__main__':
    main()
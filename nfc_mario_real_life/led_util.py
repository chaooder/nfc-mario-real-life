import RPi.GPIO as GPIO


### Configs ###
LED_PIN_NUM = 25


def prepare_led_gpio():
	GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN_NUM, GPIO.OUT)


def flash_led():
	GPIO.output(LED_PIN_NUM,1)
    time.sleep(1) #time for LED to stay lighted can be tweaked
    GPIO.output(LED_PIN_NUM,0)
    GPIO.cleanup()

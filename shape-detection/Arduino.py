import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 0.1)
p.start(1)
raw_input('blah')
p.stop()
GPIO.cleanup()

from machine import Pin
import time

# Initialisera LED på Pin 15 som utgång och knapp på Pin 13 som ingång med intern pull-up
led = Pin(15, Pin.OUT)
button = Pin(13, Pin.IN, Pin.PULL_UP)


def send_sos(num_of_sos):
    """Blinkar SOS-meddelande med LED."""
    for _ in range(num_of_sos):
        # SOS = 3 korta blink, 3 långa blink, 3 korta blink
        # Korta blink (250 ms)
        for _ in range(3):
            led.value(1)
            time.sleep(0.25)
            led.value(0)
            time.sleep(0.25)

        # Långa blink (750 ms)
        for _ in range(3):
            led.value(1)
            time.sleep(0.75)
            led.value(0)
            time.sleep(0.25)

        # 3 korta blink igen
        for _ in range(3):
            led.value(1)
            time.sleep(0.25)
            led.value(0)
            time.sleep(0.25)


try:
    while True:
        if not button.value():  # Om knappen är nedtryckt (logisk låg nivå)
            send_sos(1)  # Skicka SOS en gång så länge knappen är nertryckt
        else:
            led.value(0)  # Släck LED när knappen inte trycks ned
        time.sleep(0.1)  # Liten fördröjning för att undvika studsar
except KeyboardInterrupt:
    # Hanterar avbrott, stänger av LED när programmet avslutas
    led.value(0)

from raspledstrip.ledstrip import LEDStrip
from raspledstrip.animation import AlertStrobe
from raspledstrip.color import Color

led_driver = LEDStrip(36, True)
led_driver.all_off()

alert_animation = AlertStrobe(led_driver, Color(255.0, 0, 0, 1.0))
alert_animation.run(1, .01, 200)

led_driver.all_off()


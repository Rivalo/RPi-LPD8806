import time
from raspledstrip.ledstrip import LEDStrip
from raspledstrip.animation import AlertStrobe, FillFromCenter
from raspledstrip.color import Color

led_driver = LEDStrip(36, True)
led_driver.all_off()

alert_color = Color(255, 0, 0, 1.0)
alert_animation = AlertStrobe(led_driver, alert_color)
alert_animation.run(1, 20, 24)
fill_animation = FillFromCenter(led_driver, alert_color)
fill_animation.run(1, 30, 200)
led_driver.all_off()


from raspledstrip.ledstrip import LEDStrip
from raspledstrip.LPD8806 import LPD8806SPI
from raspledstrip.animation import AlertStrobe, FillFromCenter, BreathingLight
from raspledstrip.color import Color

led_strip = LEDStrip(LPD8806SPI(36))
led_strip.all_off()

alert_color = Color(255, 0, 0, 1.0)
alert_animation = AlertStrobe(led_strip, alert_color)
alert_animation.run(1, 20, 24)
fill_animation = FillFromCenter(led_strip, alert_color)
fill_animation.run(1, 30, 200)
breathing_animation = BreathingLight(led_strip, 255, 0, 0, 0, 1)
breathing_animation.run(1, 30, 512)
led_strip.all_off()


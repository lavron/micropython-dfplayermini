# DFPlayer Mini: simple mp3 player for micropython

Micropython implementation of DFRobot DFPlayer Mini. Tested on ESP32 boards (Lolin32, Waveshare ESP32 driver board, DOIT ESP32DEVKIT).

Module specification and pins reference is [here](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299).

## Methods

Playback control:
* play_track(track_id)
* play_next()
* play_previous()
* pause()
* resume()
* stop()
* loop_track(track_id)
* loop()
* loop_disable()

Volume control:
* volume_up()
* volume_down()
* set_volume(volume)

Module control:
* module_sleep()
* module_wake()
* module_reset()

## Wiring

Wire up the DFPlayer Mini MP3 breakout to the ESP32:

![DFPlayer-mini ESP32 micropython connection diagram](DFPlayer-mini_ESP32_connection_diagram.png)

* VCC  => 5V
* GND  => GND
* TX   => D16
* RX   => D17
* SPK1 and SPK2 to the small speaker or DAC_R and DAC_L to the amplifier

## How to use

The following example code show basic operations: 

```python
from dfplayermini import Player

from time import sleep

music = Player(pin_TX=17, pin_RX=16)

music.set_volume(20)
music.play_track(1)
sleep(10)

music.play_next()
sleep(10)

music.pause()

music.play_track(2)
music.loop()
sleep(20)

music.module_sleep()
```
## Authors

**Viktor Lavron** - *Initial work* - [github](https://github.com/lavron)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
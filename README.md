# DFPlayer Mini: simple mp3 player for micropython

Asynchronous micropython library for control of DFRobot DFPlayer Mini. 
Tested on ESP32 boards (Lolin32, Waveshare ESP32 driver board, DOIT ESP32DEVKIT)

Module specification and pins reference is [here](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299).

## Methods

Playback control:
* play(*track_id)
track_id, 'next' or 'prev'
* pause()
* resume()
* loop_track(track_id)
* loop()
* loop_disable()
* stop()
Fadeout (non-blocking) and stop
* fadeout(*fadeout_ms)

Volume control:
* volume(*level)
set volume level to 'level'
return volume level.

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

music.stop(fadeout_ms = 1000)

music.play_track(2)
music.loop()
sleep(20)

music.module_sleep()
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
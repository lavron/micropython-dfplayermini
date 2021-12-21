# DFPlayer Mini: simple mp3 player for micropython

Asynchronous micropython library for control of DFRobot DFPlayer Mini. 
Tested on ESP32 boards (Lolin32, Waveshare ESP32 driver board, DOIT ESP32DEVKIT)

Module specification and pins reference is [here](https://wiki.dfrobot.com/DFPlayer_Mini_SKU_DFR0299).

## Methods

Playback control:
```python
play(track_id) # track_id, 'next' or 'prev'
play(track_id, folder)  # track_id in folder (both integers)
pause()
resume()
loop_track(track_id)
loop()
loop_disable()
stop()
fadeout(fadeout_ms) # non-blocking fadeout and stop
```

Volume control:
```python
volume(level) # return volume level
```

Module control:
```python
module_sleep()
module_wake()
module_reset()
```

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

music.volume(20)
music.play(1)
sleep(10)

music.fadeout(2000)

music.play(2)
music.loop()
music.play(3, 2)  # Plays track 3 in folder 2
sleep(20)

music.module_sleep()
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

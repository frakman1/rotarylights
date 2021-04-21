<img src="https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg">

# rotarylights
[control LIFX bulbs with Pi using rotary encoder](https://www.youtube.com/watch?v=NKMdHzhjUak)


run using:

`DEBUG=0 python3 monitor-volume.py`


A recent upgrade to raspian broke something in the audio and I would get this error:

```bash
amixer: Unable to find simple control 'PCM',0

Traceback (most recent call last):
  File "monitor-volume.py", line 293, in <module>
    v = Volume()
  File "monitor-volume.py", line 133, in __init__
    self._sync()
  File "monitor-volume.py", line 208, in _sync
    output = self._amixer("get 'PCM'")
  File "monitor-volume.py", line 241, in _amixer
    raise VolumeError("Unknown error")
__main__.VolumeError: Unknown error
```

so I had to add this to /boot/cmdline.txt in order to get it to work again:

`snd_bcm2835.enable_hdmi=1 snd_bcm2835.enable_headphones=1 snd_bcm2835.enable_compat_alsa=1`


<sup>Special thanks to Andrew DuPont for his [tutorial](https://andrewdupont.net/2017/04/28/nostalgia-tron-part-6-adding-a-volume-knob-to-the-raspberry-pi/) on using a rotary encoder with a Pi to control the volume, upon which this project is based.</sub>

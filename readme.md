# ZX Spectrum font

This python script generates *.psf font for linux console. The font is generated from an image taken from [Wikipedia](https://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B1%D0%BE%D1%80_%D1%81%D0%B8%D0%BC%D0%B2%D0%BE%D0%BB%D0%BE%D0%B2_ZX_Spectrum). The original image is scaled down to 50% so that there is one image pixel for every font pixel.

# installation

add font to system:

~~~
# wget https://github.com/Kudesnick/zx_psf/raw/master/zx.psf -O /usr/share/consolefonts/zx_8x8.psf
~~~

open config `console-setup`

~~~
# sudo nano /etc/default/console-setup
~~~

and add the following settings:

~~~
FONTSIZE="8x8"
FONT='zx_8x8.psf'
~~~

save changes and reboot system.

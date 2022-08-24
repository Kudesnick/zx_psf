# -*- coding: utf-8 -*-

# https://en.wikipedia.org/wiki/ZX_Spectrum_character_set

from PIL import Image # pip install pillow
image = Image.open('zx.png')
pixels = [0 if i[0] > 0  else 1 for i in list(image.getdata())]
rows = []
h = image.height
w = image.width
for y in range(0, h*w, 8*w):
    for x in range(0, w, 8):
        for i in range(8):
            r = y + x + i*w
            b = 0
            for v in pixels[r:r+8]:
                b = (b << 1) + v
            rows.append(b)
print([rows[i:i+8] for i in range(0, len(rows), 8)])

import struct
PSF_FONT_MAGIC = 0x864ab572
OFFSET = 0x20
header = struct.pack('<8I',
    PSF_FONT_MAGIC, # magic;         /* magic bytes to identify PSF */
    0             , # version;       /* zero */
    8*4           , # headersize;    /* offset of bitmaps in file, 32 */
    0             , # flags;         /* 0 if there's no unicode table */
    int(len(rows) / 8) + OFFSET, # numglyph;  /* number of glyphs */
    8             , # bytesperglyph; /* size of each glyph */
    8             , # height;        /* height in pixels */
    8               # width;         /* width in pixels */
    )

with open('zx.psf', 'wb') as f:
    f.write(bytes(header))
    f.write(bytes([0] * OFFSET * 8))
    f.write(bytes(rows))

print('ok')

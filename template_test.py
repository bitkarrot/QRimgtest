#!/usr/bin/env python

from jinja2 import Template 
from PIL import Image
import qrcode
import qrcode.image.svg
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import RadialGradiantColorMask

import pyqrcode


RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)  # '#ae0909'
WHITE = (255, 255, 255)
L_YELLOW = (195,182,108) # #C3B66C
D_YELLOW = (142, 116, 56) # #8E7438

lnurl = "LNURL1DP68GURN8GHJ7MR9VAJKUEPWD3HXY6T5WVHXXMMD9AKXUATJD3CZ7CTSDYHHVVF0D3H82UNV9UUNWVCE4EM6P"

# this works
lnurl_file = "images/lnurl.png"
pyqr = pyqrcode.create(lnurl)
pyqr.png(lnurl_file, scale=3, module_color=[255,255,255,255], background=[170, 0, 0])


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=0.5,
)

# 30% or greater error conversion
#qr.add_data(lnurl)
#qr.make(fit=True)

#factory = qrcode.image.svg.SvgPathImage

# QR_PATH_STYLE = {'fill': '#000000', 'fill-opacity': '1',
#                     'fill-rule': 'nonzero', 'stroke': 'none'}
# update fill color to red, # gold yellow #C3B66C
'''
red = '#ae0909'
yellow = '#C3B66C'
dkyellow = '#8E7438'
black = '#000000'
white = '#ffffff'
other = '#5b1110ff'

factory.QR_PATH_STYLE['fill'] = '#ffffff'
print(factory.QR_PATH_STYLE['fill'])

factory.background = red
print(factory.background)

svg_img = qrcode.make(lnurl, image_factory=factory)
svg_img.save('qrcolor.svg')
'''

with open('templates/inlet_tiger_cut.svg', 'r') as f:
    templ = f.read()

#qr_code = "\"" + "qrcolor.svg" + "\""
qr_code = "\"" + "images/lnurl.png" + "\""
idnumber = "f7dfwer7a8cd43aabsdfs"
expires = "2022-03-15"
sats = "2000"

tm = Template(templ)
msg = tm.render(qrcode=qr_code, idnumber=idnumber, expires=expires, sats=sats)

with open('output.svg', 'w') as f:
    res = f.write(msg)
    f.close()
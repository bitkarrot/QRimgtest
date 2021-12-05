#!/usr/bin/env python

from jinja2 import Template 
import pyqrcode
import subprocess

'''
EDIT YOUR TEMPLATE FILE 
to refer to lnurl_file and qr_code, idnumber, expires and sats
with {{ }}

example: {{sats}}

'''

RED = (255, 0, 0)
DEEP_RED = (170, 0, 0)  # '#ae0909'
WHITE = (255, 255, 255)

lnurl = "LNURL1DP68GURN8GHJ7UM9DEJZUMRPD9EK2EFWDAEXWTMVDE6HYMRS9ASHQ6F0WCCJ7MRWW4EXCTEKF98VLF"

lnurl_file = "images/lnurl.png" # make this id number based for uniqueness
output_svg = 'output.svg'
output_png = 'output.png'
idnumber = "f7dfwer7a8cd43aabsdfs"
expires = "2022-03-15"
sats = "2500"

def create_laisee_qrcode(lnurl: str, idnumber: str, expires: str, sats: str):
    # todo: check if lnurl is valid
    pyqr = pyqrcode.create(lnurl)

    # change your QR code foreground and background colors here
    pyqr.png(lnurl_file, scale=3, module_color=[91,17,16], background=[220, 184, 102])

    with open('templates/inlet_tiger_cut.svg', 'r') as f:
        templ = f.read()

    qr_code = "\"" + lnurl_file + "\""
    tm = Template(templ)
    msg = tm.render(qrcode=qr_code, idnumber=idnumber, expires=expires, sats=sats)

    with open(output_svg, 'w') as f:
        res = f.write(msg)
        f.close()

    subprocess.run(['rsvg-convert', output_svg, '-o', output_png, '-w' , '600'], cwd=".")
    return output_png


if __name__ == "__main__":

    output_png = create_laisee_qrcode(lnurl, idnumber, expires, sats)

    # view file created
#    subprocess.run(['open', output_png])

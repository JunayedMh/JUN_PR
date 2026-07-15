import os
import pyqrcode
from pyqrcode import QRCode

output_folder = "Qr_Outputs"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)


objct = input("TEXT/URL: ")
url = pyqrcode.create(objct)

svg_path = os.path.join(output_folder, "myqr.svg")
png_path = os.path.join(output_folder, "myqr.png")

url.svg(svg_path, scale = 8)
url.png(png_path, scale = 6)

print("QR code generated successfully!")
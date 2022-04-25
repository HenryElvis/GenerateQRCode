import pyqrcode
from PIL import ImageColor

color = ImageColor.getcolor(input("couleur principale en hex : "), 'RGBA')
link = input(str('lien ou code : '))
qr = pyqrcode.create(link)

img = qr.png("code.png", scale=20, module_color=list(color))

print("Done.")

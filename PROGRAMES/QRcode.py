import qrcode
img = qrcode.make('https://wa.me/qr/JE3K4SVD2K7OG1')

img.save("myQRcode.png")
img.show()

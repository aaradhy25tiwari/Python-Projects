import qrcode as qr

txt = input("Enter the text or link to generate QR Code: ")
img = qr.make(txt)
img.save("qrcode.png")

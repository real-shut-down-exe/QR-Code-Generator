import qrcode # pip install qrcode
import image # pip install image
from cfonts import render, say # pip install python-cfonts

# Banner
banner1 = render('QR Code', colors=['red', 'white'], align='center')
banner2 = render('Generator', colors=['red', 'white'], align='center')
print(banner1)
print(banner2)

# QR Generator
qr = qrcode.QRCode(
    version = 15 , 
    box_size = 7 , 
    border = 5 , 
)

# Entries
data = input("Link Address: ")
text = input("QR Code Name: ")

qr.add_data(data)
qr.make(fit = True)

# Save QR Code as PNG
img = qr.make_image(fill="black",black_color="white")
img.save(text+".png")

# Finish

input("Task Completed")

import qrcode
data=input("Enter the link to get the corresponding qr code:")
img=qrcode.make(data)
img.save('qrcode.jpeg')

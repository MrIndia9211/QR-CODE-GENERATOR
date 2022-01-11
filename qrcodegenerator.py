import qrcode 
import image 
qr = qrcode.QRCode(
    version = 15,#15 means the version of the qr code highthe number bigger the code image and complicates picture
    box_size = 10, # size of the box when qrcode will be displayed
    border = 5 ,# it is the white part of image -- border in all sides with white color

)

data = "https://www.youtube.com/channel/UC_I-clKMfU5C4k5u2MPxRfg"
# path of qrcode 

qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill="black",back_color="white")
img.save("test.png")
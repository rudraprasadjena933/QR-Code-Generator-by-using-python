import qrcode 
# img = qr.make("hey")
# img.save("QR Scan")
from PIL import Image
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4)
qr.add_data("hey")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("beta")
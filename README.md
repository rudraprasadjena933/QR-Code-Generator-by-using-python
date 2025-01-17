# QR-Code-Generator-by-using-python
qr_content: This variable contains the data you want to encode in the QR code. It could be a URL, text, or any data that can be encoded.
qrcode.QRCode: This is the main class for generating QR codes. You configure it with parameters like version, error_correction, box_size, and border.
qr.add_data: Adds the data (qr_content) to the QR code instance.
qr.make(fit=True): Generates the QR code.
qr.make_image: Converts the QR code into an image using specified colors (fill for foreground and back_color for background).
qr_img.save('qrcode.png'): Saves the QR code as a PNG image file.
qr_img.show(): Displays the QR code using the default image viewer.

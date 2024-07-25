import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data("https://youtube.com/shorts/uV4Xo0VnGVs?si=uLLIYCMxiIZbbjyY")
qr.make(fit=True)
img=qr.make_image(fill_color="red", back_color="cyan", border="tight")
img.save("NewImage.png")
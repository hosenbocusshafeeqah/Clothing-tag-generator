import qrcode

def generate_qr(code):
    img = qrcode.make(code)
    img = img.resize((180, 180))
    img.save("qr.png")
    return "qr.png"

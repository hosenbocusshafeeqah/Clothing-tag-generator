from PIL import Image, ImageDraw, ImageFont
from qr_generator import generate_qr

def create_layout(qr_path, code, price, name, size=None, bulk_qty=None, bulk_price=None):
    price = str(price)
    tag = Image.new("RGB", (390, 560), "white")

    qr = Image.open(qr_path)
    tag.paste(qr, (210, 340))

    draw = ImageDraw.Draw(tag)

    font1 = ImageFont.truetype(r"C:\Windows\Fonts\coprgtb.TTF", 190)
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 35)
    font3 = ImageFont.truetype(r"C:\Windows\Fonts\forte.TTF", 75)
    font4 = ImageFont.truetype("arial.ttf", 24)
    font5 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 80)
    font6 = ImageFont.truetype(r"C:\Windows\Fonts\coopbl.ttf", 67)
    font7 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 60)
    font8 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 50)
    font9 = ImageFont.truetype(r"C:\Windows\Fonts\arlrdbd.ttf", 50)
    font10 = ImageFont.truetype(r"C:\Windows\Fonts\coprgtb.TTF", 175)

    draw.text((27, 5), "Soul Mart", fill="firebrick", font=font6)
    draw.text((13, 55), "HOT SALES", fill=(255, 0, 0), font=font3)

    draw.text((27, 266), "VAT INCLUDED", fill="black", font=font4)
    draw.text((27, 283), "SIZE", fill="maroon", font=font8)

    
    draw.text((211, 267), code[6:], fill="black", font=font7)
    draw.text((211, 267.5), code[6:], fill="black", font=font7)

    if len(price) == 2:
        draw.text((65, 86), price, fill="navy", font=font1)
    else:
        draw.text((12, 95), price, fill="navy", font=font10)


    draw.text((27, 327), name, fill="black", font=font2)

    if size:
        draw.text((39, 385), size, fill="red", font=font5)
    
    if bulk_qty not in (None, "", " ") and bulk_price not in (None, "", " "):
        text = f"{bulk_qty} POU {bulk_price}"
        draw.text((57, 490), text, fill="firebrick", font=font9)

    tag.save("tag.png")

    return "tag.png"


def create_sheet(tag_path):
    sheet = Image.new("RGB", (2480, 3508), "white")
    tag = Image.open(tag_path)
    tag = tag.resize((400, 570))

    for i in range(6):
        for j in range(6):
            length = j * 410
            width = i * 570
            sheet.paste(tag, (length, width))
    
    sheet.save("sheet.png")
    
    return "sheet.png"

def test():
    qr_path = generate_qr(666)
    tag_path = create_layout(qr_path, "10647468750", 60, "BLOUSE SSSSSSSSSSS", "XXL", 4, 1000)
    sheet_path = create_sheet(tag_path)

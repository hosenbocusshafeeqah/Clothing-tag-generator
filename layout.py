from PIL import Image, ImageDraw, ImageFont
from qr_generator import generate_qr

def create_layout(qr_path, code, price, name, size=None, bulk_qty=None, bulk_price=None):
    price = str(price)
    tag = Image.new("RGB", (390, 560), "white")

    qr = Image.open(qr_path)
    tag.paste(qr, (210, 320))

    draw = ImageDraw.Draw(tag)

    font1 = ImageFont.truetype(r"C:\USERS\HP\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\CLARENDONBTPRO-BLACK.TTF", 190)
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 35)
    font3 = ImageFont.truetype(r"C:\Windows\Fonts\forte.TTF", 75)
    font4 = ImageFont.truetype("arial.ttf", 24)
    font5 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 80)
    font6 = ImageFont.truetype(r"C:\USERS\HP\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\CLARENDONBTPRO-BLACK.TTF", 65)
    font7 = ImageFont.truetype(r"C:\USERS\HP\APPDATA\LOCAL\MICROSOFT\WINDOWS\FONTS\CLARENDONBTPRO-BOLD.TTF", 55)
    font8 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 50)
    font9 = ImageFont.truetype(r"C:\Windows\Fonts\impact.ttf", 60)

    draw.text((21, 18), "Soul Mart", fill="firebrick", font=font6)
    draw.text((13, 55), "HOT SALES", fill=(255, 0, 0), font=font3)

    draw.text((27, 247), "VAT INCLUDED", fill="black", font=font4)
    draw.text((27, 264), "SIZE", fill="maroon", font=font8)

    
    draw.text((200, 255), code[6:], fill="black", font=font7)
    draw.text((200, 255.5), code[6:], fill="black", font=font7)

    if len(price) == 2:
        draw.text((74, 100), price, fill="navy", font=font1)

    else:
        draw.text((10, 100), price, fill="navy", font=font1)


    draw.text((27, 307), name, fill="black", font=font2)

    if size:
        draw.text((39, 360), size, fill="red", font=font5)
    
    if bulk_qty not in (None, "", " ") and bulk_price not in (None, "", " "):
        text = f"{bulk_qty} POU {bulk_price}"
        draw.text((63, 470), text, fill="maroon", font=font9)

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
    tag_path = create_layout(qr_path, "10647468750", 75, "BLOUSE SSSSSSSSSSS", "XXL", 4, 1000)
    sheet_path = create_sheet(tag_path)

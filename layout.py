from PIL import Image, ImageDraw, ImageFont

def create_layout(qr_path, code, price, name, size):

    tag = Image.new("RGB", (390, 560), "white")

    qr = Image.open(qr_path)
    tag.paste(qr, (210, 332))

    draw = ImageDraw.Draw(tag)

    font1 = ImageFont.truetype("C:\Windows\Fonts\ALGER.TTF", 160)
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 35)
    font3 = ImageFont.truetype(r"C:\Windows\Fonts\COOPBL.TTF", 70)
    font4 = ImageFont.truetype("arial.ttf", 24)
    font5 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 250)

    draw.text((21, 18), "Soul Mart", fill="black", font=font3)
    draw.text((31, 78), "Hot Sales", fill="black", font=font3)

    draw.text((35, 290), "VAT INCLUDED", fill="black", font=font4)
    draw.text((35, 358), "SIZE", fill="black", font=font2)
    draw.text((38, 165), "Rs", fill="black", font=font4)

    draw.text((235, 288), code[6:], fill="black", font=font2)
    draw.text((68, 130), str(price), fill="black", font=font1)
    draw.text((35, 320), name, fill="black", font=font2)
    draw.text((60, 390), size, fill="black", font=font3)

    tag.save("tag.png")

    return "tag.png"

def create_layout_nosize(qr_path, code, price, name):

    tag = Image.new("RGB", (390, 560), "white")

    qr = Image.open(qr_path)
    tag.paste(qr, (210, 332))

    draw = ImageDraw.Draw(tag)

    font1 = ImageFont.truetype(r"C:\Windows\Fonts\ALGER.TTF", 160)
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 35)
    font3 = ImageFont.truetype(r"C:\Windows\Fonts\COOPBL.TTF", 70)
    font4 = ImageFont.truetype("arial.ttf", 24)

    draw.text((21, 18), "Soul Mart", fill="black", font=font3)
    draw.text((31, 78), "Hot Sales", fill="black", font=font3)

    draw.text((35, 290), "VAT INCLUDED", fill="black", font=font4)
    draw.text((35, 358), "SIZE", fill="black", font=font2)
    draw.text((38, 165), "Rs", fill="black", font=font4)

    draw.text((235, 288), code[6:], fill="black", font=font2)
    draw.text((68, 130), str(price), fill="black", font=font1)
    draw.text((35, 320), name, fill="black", font=font2)

    tag.save("tag.png")

    return "tag.png"


def create_sheet(tag_path):
    sheet = Image.new("RGB", (2480, 3508), "white")
    tag = Image.open(tag_path)
    tag = tag.resize((420, 600))

    for i in range(6):
        for j in range(6):
            length = j * 400
            width = i * 540
            sheet.paste(tag, (length, width))
    
    sheet.save("sheet.png")
    
    return "sheet.png"
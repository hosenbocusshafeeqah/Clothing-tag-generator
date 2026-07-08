**QR Code Tag generator

This is a Python app which takes in a code as input and generates a qr code then makes a tag which is then printed onto a 6x6 sheet.
It stores product hsitory using SQLite and allows users to go through past generated codes and even reprint it.

--------------

**Features:
-Generates QR codes for products
-Creates printable price tags
-Generates A4 sheet with multiple tags
-Stores product history using SQLite
-Reprint previous tags from history
-Optional size support for clothing items
-Input Validation and error handling

--------------

**Tech Stack:
-Python
-SQLite
-Pillow (PIL)
-qrcode

--------------

**How to run:
1. copy this repository: git clone https://github.com/yourusername/clothes-tag-generator.git
2. Install: pip install pillow qr code
3. run the program: python main.py
<img width="132" height="71" alt="Screenshot 2026-06-20 234336" src="https://github.com/user-attachments/assets/379cff0b-0f93-409b-be5f-d92e34079719" />

With size input:
<img width="206" height="143" alt="image" src="https://github.com/user-attachments/assets/d8a3f91e-171f-4976-af06-55aacfa04bf2" />

Tag (with size):
<img width="208" height="297" alt="image" src="https://github.com/user-attachments/assets/faac3f2b-c4a9-4216-b91d-1fa8501d40c2" />

Sheet (with size):
<img width="212" height="287" alt="image" src="https://github.com/user-attachments/assets/f91922c7-b8df-4dc5-a06f-34978884b21c" />

Tag (without size): 
<img width="183" height="260" alt="image" src="https://github.com/user-attachments/assets/3eb609e3-73e5-4dbc-8ace-a0bae2107f75" />

Reprint feature: 
<img width="150" height="144" alt="image" src="https://github.com/user-attachments/assets/01540868-4243-4565-afa1-da0da8726fea" />

Result: 
<img width="208" height="297" alt="image" src="https://github.com/user-attachments/assets/faac3f2b-c4a9-4216-b91d-1fa8501d40c2" />

--------------

**Note (Product code structure) - Business rule:
This project follows a fixed product coding system defined by the store owner,
meaning that all product codes begin with the prefix: 106474

The remaining digits follow a structured format:
The next 2 digits represent the product sequence number
The last 3 digits represent the product price

--------------

**EXAMPLE:
A product code such as: 10647480900
Can be interpreted as:
"80" being the product number (sequence in inventory)
"900" being the price which is 900 MUR

SO Another product with the same price (900 MUR) but a new entry would follow: 10647481900
Means:
"81" is the next product in sequence
and "900" same price (900 MUR)

Since the first 6 digits are already known by the system only the remaining digits are displayed on the printed tag for clarity and space optimization 

--------------

**This project is functional and will be further improved with a graphical user interface (Tkinter).

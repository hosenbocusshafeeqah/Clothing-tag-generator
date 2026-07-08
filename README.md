QR Code Tag generator

a desktop application built entirely with Python and it generates qr codes which is used to make tags and sheets and then printed. A preview is provided before the user prints it. you can also check the history of generated tags.

Features:
-Generates QR codes for products
-Creates printable price tags
-Tag preview before printing
-directly prints from the app
-Generates A4 sheet with multiple tags
-Stores product history using SQLite
-Reprint previous tags from history
-Optional size support for clothing items
-Input Validation and error handling
-deletes history older than 7 days
-Input validation to prevent errors

Tech Stack:
-Python
-SQLite
-Pillow (PIL)
-qrcode
Tkinter

main.py - Main gui and application logic
database.py - SQLite database functions
layout.py - Tag layout generation
qr_generator.py - qr code generation

How to run:
1. copy this repository: git clone https://github.com/yourusername/clothes-tag-generator.git
2. Install: pip install pillow qrcode
3. run the program: python main.py
<img width="362" height="377" alt="image" src="https://github.com/user-attachments/assets/492e8b72-03c5-4def-82cf-ae2d3561f0b8" />


<img width="362" height="380" alt="image" src="https://github.com/user-attachments/assets/4463612f-19ff-48d6-a047-7dd8f5c591ba" />


<img width="365" height="380" alt="image" src="https://github.com/user-attachments/assets/a410f3ff-7d08-442c-87ed-41be78a903f5" />


<img width="341" height="479" alt="image" src="https://github.com/user-attachments/assets/da7f2fa0-57eb-43c2-bfa4-142e0bcd518f" />


--------------

Note (Product code structure) - Business rule:
This project follows a fixed product coding system defined by the store owner,
meaning that all product codes begin with the prefix: 106474

The remaining digits follow a structured format:
The next 2 digits represent the product sequence number
The last 3 digits represent the product price

--------------

EXAMPLE:
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

Future improvements:
-Amount of tags generated on a sheet can be adjusted.
-Amount of size needed on one sheet can be adjusted.
-Configurable printer setting.
-Better aesthetics and more user friendly.

developped by Hosenbocus Shafeeqah

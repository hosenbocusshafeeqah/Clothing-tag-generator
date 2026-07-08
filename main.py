from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import os

from datetime import datetime, timedelta
from database import insert_values, create_table, view_history, delete_history
from qr_generator import generate_qr
from layout import create_layout, create_sheet

create_table()
delete_history()

backg1 = "bisque"

preview_window = None

def show_preview(tag_path, sheet_path):
    global preview_window
    if preview_window and preview_window.winfo_exists():
        preview_window.destroy()

    preview_window = tk.Toplevel(main_window)
    preview_window.title("Tag Preview")
    preview_window.geometry("450x650")

    try:
        img = Image.open(tag_path)
    except Exception as e:
        messagebox.showerror("Preview Error", str(e))
        return
    img = img.resize((400, 550))

    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(preview_window, image=img_tk)
    label.image = img_tk
    label.pack(pady=10)

    btn_frame = tk.Frame(preview_window)
    btn_frame.pack()
    tk.Button(btn_frame, text="Print", command=lambda: print_sheet(sheet_path)).pack(side="left", padx=10)
    tk.Button(btn_frame, text="Close", command=lambda: close(preview_window)).pack(side="right", padx=10)

def close(preview_window):
    preview_window.destroy()

def mouse_wheel_movement(event):
    history_canvas.yview_scroll(int(-event.delta/120), "units")

def update_scroll_region():
    history_content.update_idletasks()
    history_canvas.configure(scrollregion=history_canvas.bbox("all"))

def back_generate():
    generate_frame.pack_forget()
    clear_entries()
    frame_menu.pack(expand=True, anchor="center")

def back_view_history():
    history_frame.pack_forget()
    frame_menu.pack(expand=True, anchor="center")

def open_generate(frame_menu, generate_frame):
    frame_menu.pack_forget()
    generate_frame.pack()

def open_history(frame_menu):
    frame_menu.pack_forget()
    history_frame.pack(expand=True, fill="both")
    check_history()

def generate_process():
    code = code_entry_generate.get()
    price = price_entry_generate.get()
    name = name_entry_generate.get().strip()
    size = size_entry_generate.get().upper()
    bulk_qty = bulk_qty_entry_generate.get().strip()
    bulk_price = bulk_price_entry_generate.get().strip()

    if bulk_qty == "":
        bulk_qty = None

    if bulk_price == "":
        bulk_price = None
        
    if code =="":
        messagebox.showerror("Error", "Product code cannot be empty.")
        return
    elif not code.isdigit():
        messagebox.showerror("Error", "Product code must contain numbers only.")
        return

    if price =="":
        messagebox.showerror("Error", "Product price cannot be empty.")
        return
    elif not price.isdigit():
        messagebox.showerror("Error", "Product price must contain numbers only.")
        return

    if name == "":
        messagebox.showerror("Error", "Name cannot be empty.")
        return

    if (bulk_qty is None) != (bulk_price is None):
        messagebox.showerror("Error", "Both bulk fields must be filled or both left empty.")
        return

    qr_path = generate_qr(code)
    tag_path = create_layout(qr_path, code, price, name, size, bulk_qty, bulk_price)
    sheet_path = create_sheet(tag_path)

    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    insert_values(code, name, price, created_at, size, bulk_qty, bulk_price)

    show_preview(tag_path, sheet_path)


def print_sheet(sheet_path):
    try:
        os.startfile(sheet_path, "print")
    except Exception as e:
        messagebox.showerror("Printing Error", str(e))
        return
    if preview_window and preview_window.winfo_exists():
        preview_window.destroy()

def exiting():
    main_window.destroy()

def reprint(code, name, price, size, bulk_qty, bulk_price):
    qr_path = generate_qr(code)
    tag_path = create_layout(qr_path, code, price, name, size, bulk_qty, bulk_price)
    sheet_path = create_sheet(tag_path)

    show_preview(tag_path, sheet_path)

def clear_entries():
    code_entry_generate.delete(0, tk.END)
    name_entry_generate.delete(0, tk.END)
    price_entry_generate.delete(0, tk.END)
    size_entry_generate.delete(0, tk.END)
    bulk_qty_entry_generate.delete(0, tk.END)
    bulk_price_entry_generate.delete(0, tk.END)

def check_history():
    for widget in history_content.winfo_children():
        widget.destroy()

    code_column_label = tk.Label(history_content, text = "CODE", pady=5, padx= 10)
    code_column_label.grid(row=1, column=0, sticky="w")
    name_column_label = tk.Label(history_content, text = "NAME", pady=5, padx= 10)
    name_column_label.grid(row=1, column=1, sticky="w")
    price_column_label = tk.Label(history_content, text = "PRICE", pady=5, padx= 10)
    price_column_label.grid(row=1, column=2, sticky="w")
    size_column_label = tk.Label(history_content, text = "SIZE", pady=5, padx= 10)
    size_column_label.grid(row=1, column=3, sticky="w")
    bulk_qty_column_label = tk.Label(history_content, text = "BULK QTY", pady=5, padx= 10)
    bulk_qty_column_label.grid(row=1, column=4, sticky="w")
    bulk_price_column_label = tk.Label(history_content, text = "BULK PRICE", pady=5, padx= 10)
    bulk_price_column_label.grid(row=1, column=5, sticky="w")

    rows = view_history()
    for index, row in enumerate(rows):
        num = index + 2
        code, name, price, size, bulk_qty, bulk_price= row
        code_label = tk.Label(history_content, text = code)
        code_label.grid(row=num, column=0, sticky="nw", padx= 5, pady=3)
        name_label = tk.Label(history_content, text = name)
        name_label.grid(row=num, column=1, sticky="nw", padx= 7, pady=3)
        price_label = tk.Label(history_content, text = price)
        price_label.grid(row=num, column=2, sticky="nw", padx= 9, pady=3)
        size_label = tk.Label(history_content, text = size)
        size_label.grid(row=num, column=3, sticky="nw", padx= 10, pady=3)
        bulk_qty_label = tk.Label(history_content, text = bulk_qty)
        bulk_qty_label.grid(row=num, column=4, sticky="nw", padx= 10, pady=3)
        bulk_price_label = tk.Label(history_content, text = bulk_price)
        bulk_price_label.grid(row=num, column=5, sticky="nw", padx= 10, pady=3)
        reprint_button = tk.Button(history_content, text = "Reprint", command=lambda c=code, n=name, p=price, s=size, bq=bulk_qty, bp=bulk_price: reprint(c, n, p, s, bq, bp))
        reprint_button.grid(row=num, column=6, sticky="nw", pady=3)

    update_scroll_region()

###MAIN WINDOW
main_window = tk.Tk()
main_window.title("Soul Mart QR code generator system")
main_window.geometry("480x470")
main_window.resizable(False, False)

frame_menu = tk.Frame(main_window, bg=backg1)
frame_menu.pack(expand=True, anchor="center")
title_label_menu = tk.Label(frame_menu, text = "Clothing Tag Generator", font=("ArielRounded", 18, "bold"))
title_label_menu.grid(row=0, column=0)

generate_menu_button = tk.Button(frame_menu, text="Generate", command=lambda: open_generate(frame_menu, generate_frame), width=20)
generate_menu_button.grid(row=1, column=0)
history_menu_button = tk.Button(frame_menu, text="View History", command=lambda: open_history(frame_menu), width=20)
history_menu_button.grid(row=2, column=0)
exit_menu_button = tk.Button(frame_menu, text="Exit", command=exiting, width=20)
exit_menu_button.grid(row=3, column=0)

for widget in frame_menu.winfo_children():
    widget.grid_configure(padx=20, pady=10)


###GENERATION MENU FRAME
generate_frame = tk.Frame(main_window)
generate_info = tk.LabelFrame(generate_frame, text="Basic Information")
generate_info.grid(row=0, column=0, padx=10, pady=10)

code_label_generate = tk.Label(generate_info, text="Code:")
code_label_generate.grid(row=1, column=0, sticky="sw")
price_label_generate = tk.Label(generate_info, text="Price:")
price_label_generate.grid(row=1, column=1, sticky="sw")
name_label_generate = tk.Label(generate_info, text="Name:")
name_label_generate.grid(row=1, column=2, sticky="sw")

code_entry_generate = tk.Entry(generate_info)
code_entry_generate.grid(row=2, column=0)
code_entry_generate.insert(0, "106474")
price_entry_generate = tk.Entry(generate_info)
price_entry_generate.grid(row=2, column=1)
name_entry_generate = tk.Entry(generate_info)
name_entry_generate.grid(row=2, column=2)

for widget in generate_info.winfo_children():
    widget.grid_configure(padx=10, pady=10)


size_info = tk.LabelFrame(generate_frame, text="Size")
size_info.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

size_label_generate = tk.Label(size_info, text="Size:")
size_label_generate.grid(row=1, column=0, sticky="sw", padx=10, pady=10)
size_entry_generate = tk.Entry(size_info)
size_entry_generate.grid(row=2, column=0, padx=10, pady=10)


bulk_info = tk.LabelFrame(generate_frame, text="Bulk info")
bulk_info.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

bulk_qty_label_generate = tk.Label(bulk_info, text="Bulk Quantity:")
bulk_qty_label_generate.grid(row=1, column=0, sticky="w")
for_price_label_generate = tk.Label(bulk_info, text="POU")
for_price_label_generate.grid(row=2, column=1, sticky="w")
bulk_price_label_generate = tk.Label(bulk_info, text="Bulk Price:")
bulk_price_label_generate.grid(row=1, column=2, sticky="w")

bulk_qty_entry_generate = tk.Entry(bulk_info)
bulk_qty_entry_generate.grid(row=2, column=0)
bulk_price_entry_generate = tk.Entry(bulk_info)
bulk_price_entry_generate.grid(row=2, column=2)

for widget in bulk_info.winfo_children():
    widget.grid_configure(padx=10, pady=10)

generate_button = tk.Button(generate_frame, text="GENERATE", command=generate_process)
generate_button.grid(row=4, column=0, padx=10, pady=10)

back_to_menu_button_generate = tk.Button(generate_frame, text = "Back", command=back_generate)
back_to_menu_button_generate.grid(row=4, column=0, padx=10, pady=10, sticky="w")

clear_all_button_generate = tk.Button(generate_frame, text = "Clear All", command=clear_entries)
clear_all_button_generate.grid(row=4, column=0, padx=10, pady=10, sticky="e")

###OPEN HISTORY FRAME
history_frame = tk.Frame(main_window)
history_frame.grid_rowconfigure(1, weight=1)
history_frame.grid_columnconfigure(0, weight=1)

history_title_label = tk.Label(history_frame, text="History", width=50)
history_title_label.grid(row=0, column=0)

back_to_menu_button_history = tk.Button(history_frame, text = "Back", command=back_view_history)
back_to_menu_button_history.grid(row=0, column=0, sticky="w")

history_canvas = tk.Canvas(history_frame)
history_canvas.grid(pady=10, sticky="nsew")
history_scrollbar = tk.Scrollbar(history_frame, orient="vertical", width=18)
history_scrollbar.grid(row=1, column=1, sticky="ns", pady=10,)
history_canvas.configure(yscrollcommand=history_scrollbar.set)
history_scrollbar.configure(command=history_canvas.yview)
history_content = tk.Frame(history_canvas)

history_canvas.bind("<MouseWheel>", mouse_wheel_movement)


history_content.bind("<Configure>", lambda e: update_scroll_region())

history_canvas.create_window((0,0), window = history_content, anchor="nw")

main_window.mainloop()

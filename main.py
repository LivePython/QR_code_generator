from tkinter import *
import pyqrcode
from PIL import ImageTk, Image


def generate_qrcode():
    link_name = link_name_entry.get()
    link_value = link_value_entry.get()

    file_name = link_name + '.png'
    url = pyqrcode.create(link_value)
    url.png(file_name, scale=8)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(210, 330, window=image_label)

window = Tk()
window.resizable(width=False, height=False)

canvas = Canvas(window, width=400, height=500)
canvas.pack()

app_label = Label(text="QR Code generator", fg='blue', font=('Arial', 30))
canvas.create_window(200, 50, window=app_label)

link_name = Label(text='Link Name: ')
canvas.create_window(50, 90, window=link_name)

link_name_entry = Entry(width=50)
canvas.create_window(235, 90, window=link_name_entry)

link_value = Label(text='Link: ')
canvas.create_window(50, 130, window=link_value)

link_value_entry = Entry(width=50)
canvas.create_window(235, 130, window=link_value_entry)

qr_button = Button(text="Get QR Image", command=generate_qrcode)
canvas.create_window(210, 160, window=qr_button)


window.mainloop()
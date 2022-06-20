# homework tkinter media
from tkinter import *
from PIL import ImageTk, Image
from tkmacosx import Button

root = Tk()
root.title("Yara's Cat Photo 🐱")
canvas = Canvas(root, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open('/Users/yaraelsakka/Pictures/cat.jpg'))
canvas.create_image(20, 20, anchor=NW, image=img)

# save the image:

save_button = Button(text="save photo", bg='pink', command=root.destroy)
save_button.pack(pady=20, side=BOTTOM)

root.mainloop()

# end of code

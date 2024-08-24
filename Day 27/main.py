from tkinter import *

window = Tk()
window.title("PROMYTHEUS")
window.minsize(500, 300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="Test Label", font=('Ariel', 24, 'normal'))
my_label['text'] = 'New Text'
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
def button_clicked():
    my_label['text'] = input.get()

button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text='New Button')
new_button.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=2)

window.mainloop()
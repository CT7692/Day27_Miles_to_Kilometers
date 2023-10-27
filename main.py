from tkinter import *
MY_FONT = "Arial"
FONT_SIZE = 12
X_PAD = 5
Y_PAD = 5

def button_clicked(m_input, k_label):
    if m_input.get() != "":
        miles = float(m_input.get())
        kilometers = miles * 1.609344
        k_label["text"] = "{:.1f}".format(kilometers)

window = Tk()
window.minsize(width=400, height=100)
window.title("Miles to Km Converter")
window.config(padx=5, pady=5)
miles_label = Label(text="Miles:", font=(MY_FONT, FONT_SIZE))
miles_label.grid(column=0, row=3, padx=X_PAD,pady=Y_PAD)
miles_input = Entry(width=12)
miles_input.grid(column=1, row=3, padx=X_PAD,pady=Y_PAD)
miles_input.focus()
kilometers_label = Label(text="Kilometers:", font=(MY_FONT, FONT_SIZE))
kilometers_label.grid(column=3, row=3, padx=X_PAD,pady=Y_PAD)
result_label = Label(text="0", font=(MY_FONT, FONT_SIZE))
result_label.grid(column=4, row=3, padx=X_PAD, pady=Y_PAD)
my_button = Button(text="Calculate", command=lambda: button_clicked(miles_input, result_label))
my_button.grid(column=2, row=4, padx=X_PAD, pady=Y_PAD)
window.mainloop()
from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=20, pady=20)

CONVERT_VALUE = 1.60934


def miles_to_km():
    miles = float(mile_input.get())
    kilometer = round(miles * CONVERT_VALUE, 2)
    label_3["text"] = kilometer


# Entry
mile_input = Entry()
mile_input.grid(column=1, row=0, padx=5, pady=5)

# Label_1
label_1 = Label(text="Miles", font=("Arial", 10, "normal"))
label_1.grid(column=2, row=0, padx=5, pady=5)

# Label_2
label_2 = Label(text="is equal to", font=("Arial", 10, "normal"))
label_2.grid(column=0, row=1, padx=5, pady=5)

# Label_3
label_3 = Label(text="0", font=("Arial", 10, "normal"))
label_3.grid(column=1, row=1, padx=5, pady=5)

# Label_4
label_4 = Label(text="Km", font=("Arial", 10, "normal"))
label_4.grid(column=2, row=1, padx=5, pady=5)

# Button
calculate_btn = Button(text="Calculate", command=miles_to_km)
calculate_btn.grid(column=1, row=2, padx=5, pady=5)

window.mainloop()

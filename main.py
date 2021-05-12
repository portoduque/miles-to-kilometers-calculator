from tkinter import *

PADX = 12
PADY = 12


def miles_to_km():
    miles_value = float(miles_input.get())
    km_value = round(miles_value * 1.609, 2)
    km_value_label.config(text=km_value)


window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Create Entry miles value
miles_input = Entry()
miles_input.config(width=7)
miles_input.focus()
miles_input.insert(END, string=0)
miles_input.grid(column=1, row=0)

# Create Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=PADX, pady=PADY)

# Create is equal to Label
equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0, row=1)
equal_to_label.config(padx=PADX, pady=PADY)

# Create Km value Label
km_value_label = Label(text=0)
km_value_label.grid(column=1, row=1)
km_value_label.config(padx=PADX, pady=PADY)

# Create Km label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=PADX, pady=PADY)

# Create calculate button
calculate_button = Button(text="Calculate")
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=PADX, pady=PADY, command=miles_to_km)


window.mainloop()
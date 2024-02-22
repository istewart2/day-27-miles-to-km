from tkinter import *

KM_IN_MILE = 1.60934

# Create a new window
window = Tk()
window.title("Miles to Kilometre Converter")
window.minsize(width=300, height=300)

# Entry
miles_input = Entry(width=5)
miles_input.insert(END, string="0")
miles_input.grid(row=0, column=1)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to = Label(text="is equal to")
equal_to.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)


# Button
def miles_to_km():
    miles = float(miles_input.get())
    kilometres = miles * KM_IN_MILE
    km_value_label.config(text=kilometres)


button = Button(text="Calculate", command=miles_to_km)
button.grid(row=2, column=1)

window.mainloop()

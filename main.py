from tkinter import *



def miles_to_km():
    miles = float(input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=50, pady=50)

#Entries
input = Entry(width=7)
input.insert(END, string="0")
input.grid(column=1, row=0)

mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = Label(text="=")
equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

button = Button(text="計算する", command=miles_to_km)
button.grid(column=1, row=2)







window.mainloop()
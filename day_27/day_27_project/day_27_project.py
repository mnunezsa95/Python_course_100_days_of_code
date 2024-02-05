# ------------------------------------------------------------------------------------------------ #
#                                   Miles to Kilometer Converter                                   #
# ------------------------------------------------------------------------------------------------ #

import tkinter


def calculate_kms():
    kilometers = round(float(miles_input.get()) * 1.60934, 2)
    result_kms_label.config(text=f"{kilometers}")


window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=300, height=100)
window.config(padx=40, pady=20)

miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=2)

is_equal_label = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_label.grid(row=1, column=0)

result_kms_label = tkinter.Label(text="0", font=("Arial", 12, "bold"))
result_kms_label.grid(row=1, column=1)

kms_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
kms_label.grid(row=1, column=2)

calc_button = tkinter.Button(text="Calculate", command=calculate_kms)
calc_button.grid(row=3, column=1)

window.mainloop()

import tkinter as tk
import csv
app = tk.Tk(__name__)
app.title('Registration Form')
app.geometry('250x300')
name = tk.Variable(app)
name.set('')
email = tk.Variable(app)
email.set('')
phn = tk.Variable(app)
phn.set('')

tk.Label(app, text = "Form", font = ("Arial",15)).place(x=90, y=30)
tk.Label(app, text = "Name : ").place(x=25, y=70)
tk.Entry(app,textvariable = name).place(x=90,y=70)
tk.Label(app, text = "Email id : ").place(x=25, y=100)
tk.Entry(app, textvariable = email).place(x=90,y=100)
tk.Label(app, text = "Phone no. : ").place(x=25, y=130)
tk.Entry(app, textvariable = phn).place(x=90,y=130)

with open("reg_form","w") as f:
    datawriter=csv.writer(f)
    datawriter.writerow(["Name","Email id","Phone no."])
    f.close()
def click():
    with open("reg_form.csv","a") as f:
        f.write(name.get())
        f.write(",")
        f.write(email.get())
        f.write(",")
        f.write(phn.get())
        f.write(",")
        f.write("\n")
        f.close()
    name.set('')
    email.set('')
    phn.set('')

tk.Button(app,text = "Submit", command = click).place(x=90,y=200)

app.mainloop()
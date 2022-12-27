from tkinter import *

from PIL import ImageTk, Image
import tkinter.font as font

root = Tk()
root.title("Currency Converter by Tanmay Gupta")

root.maxsize(1920,1080)
root.minsize(1280,720)
HEIGHT = 720
WIDTH = 1280
FONT = font.Font(family="Sans-serif",size="14", weight="normal")

canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open(r"Currency-Converter/bg.jpg"))
background_label = Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = Frame(root, bg="black", bd=2)
frame.place(relx=0.5, rely=0.1, relwidth=0.8,relheight=0.25, anchor="n")

label_up = Label(frame)
label_up.place(relwidth=1, relheight=1)

lower_frame = Frame(root, bg="black", bd=2)
lower_frame.place(relx=0.5,rely=0.53, relwidth=0.8, relheight=0.25, anchor="n")

label_down = Label(lower_frame,font=FONT, fg="#001a4d", anchor="nw",justify="left", bd=4)
label_down.place(relwidth=1,relheight=1)

label1 = Label(frame,text = "FROM", font= FONT, bd=5,bg="#2f2fa2", highlightbackground = "#d9138a", fg="white")
label1.place(relx=0.188, rely=0.03, relwidth = 0.10, relheight=0.25)

label2 = Label(frame, text = "TO", font =FONT, bd =5, bg ="#2f2fa2", highlightbackground = "#d9138a", fg = "white")
label2.place(relx = 0.685,rely = 0.03,relwidth = 0.10, relheight =0.25)

#For Options menu
options = [
    "AUD",
    "BGN",
    "BRL",
    "BTC",
    "CAD",
    "CHF",
    "CNY",
    "CZK",
    "DKK",
    "EUR",
    "GBP",
    "HKD",
    "HRK",
    "HUF",
    "IDR",
    "ILS",
    "INR",
    "JPY",
    "KRW",
    "LTL",
    "MXN",
    "MYR",
    "NOK",
    "NZD",
    "PHP",
    "PLN",
    "RON",
    "RUB",
    "SEK",
    "SGD",
    "THB",
    "TRY",
    "USD",
    "ZAR"

]

clicked1 = StringVar()
clicked1.set("Select")
listbox1 = OptionMenu(frame, clicked1, *options)
listbox1.config(bg="#f64c72", fg="black", activeforeground="#fc034e",activebackground="light blue", font=FONT)
listbox1.place(relx=0.06,rely=0.3,relheight=0.28,relwidth=0.38)

clicked2 = StringVar()
clicked2.set("Select")
listbox2 = OptionMenu(frame,clicked2,*options)
listbox2.config(bg="#f64c72", fg="black", activeforeground="#fc034e",activebackground="light blue", font=FONT)
listbox2.place(relx=0.56,rely=0.3,relheight=0.28,relwidth=0.38)

#for logo image between two options list

label3 = Label(frame, text="AMOUNT", font=FONT, bg="#99738e",highlightbackground="#12a4d9",fg="white")
label3.place(relx=0.26,rely=0.7,relwidth=0.26,relheight=0.25)

entry = Entry(frame,font=FONT,fg="#001a4d", bd=4)
entry.place(relx=0.54,rely=0.7,relwidth=0.26,relheight=0.25)

#buttons
button1 = Button(root,text="CONVERT", font=FONT, bg="#553d67", fg="white", activeforeground="#553d67",activebackground="light yellow")
button1.place(relx=0.16,rely=0.4,relwidth=0.15,relheight=0.07)

button2 = Button(root, text = "CLEAR", font = FONT, bg="#553d67", fg="white", activeforeground="#553d67",activebackground="light yellow")
button2.place(relx = 0.35,rely = 0.4,relwidth = 0.13, relheight = 0.07)

button3 = Button(root, text = "ABBREVIATIONS", font = FONT, bg="#553d67", fg="white", activeforeground="#553d67",activebackground="light yellow")
button3.place(relx = 0.52, rely = 0.4, relwidth = 0.15, relheight = 0.07)

button4= Button(root, text = "EXIT", font = FONT, bg="#553d67", fg="white", activeforeground="#553d67",activebackground="light yellow")
button4.place(relx = 0.7, rely = 0.4, relwidth = 0.12, relheight = 0.07)

#-----------THE LOGIC---------------

from tkinter import messagebox
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

def clear():
    entry.delete(0,END)
    label_down["text"] = ""


def convert(c1,c2,amount):
    try:
        if amount == "":
            messagebox.showerror("Error", "Amount not specified")
        elif c1 == "Select" or c2 == "Select":
            messagebox.showinfo("Error", "Currency not selected")
        else:
            try:
                amount = float(amount)
                b = BtcConverter()
                c = CurrencyRates()
                if c1 == c2:
                    result = amount
                elif c1 == "BTC":
                    result = b.convert_btc_to_cur(amount, c2)
                elif c2 == "BTC":
                    result = b.convert_to_btc(amount, c1)
                else:
                    result = c.convert(c1, c2, int(amount))
                # print(result)
                label_down["text"] = f"Conversion Result: \n{amount} {c1} = {result} {c2}"
            except ValueError:
                messagebox.showerror("Error", "Invalid amount")
                clear()
    except Exception:
        messagebox.showerror("Error", "Something went wrong. Please try again")

def help():
    newwin = Tk()
    newwin.title("Abbreviations")
    newwin.maxsize(350,710)
    newwin.minsize(350,710)
    newcanvas = Canvas(newwin, height = 710, width = 300)
    newcanvas.pack()
    newframe = Frame(newwin, bg ="light blue")
    newframe.place(relwidth = 1, relheight = 1)
    newlabel = Label(newframe, font = FONT, fg ="#001a4d", anchor = "nw", justify = "left", bd =4)
    newlabel.place(relx = 0.03, rely = 0.02,relwidth = 0.94, relheight = 0.96)
    newlabel["text"] = "Abbrevations:\nAUD - Australian Dollar\nBGN - Bulgarian Lev\nBRL - Brazilian Real\nBTC - Bitcoin\nCAD - Canadian Dollar\nCHF - Swiss Franc\nCNY - Chinese Yuan\nCZK - Czech Koruna\nDKK - Danish Krone\nEUR - Euro\nGBP - Pound Sterling\nHKD - HongKong Dollar\nHRK - Croatian Kuna\nHUF - Hungarian Forint\nIDR - Indonesian Rupiah\nILS - Israeli New Shekel\nINR - Indian Rupee\nJPY - Japanese Yen\nKRW - South Korean Won\nLTL - Lithuanian Litas\nMXN - Mexican Peso\nMYR - Malaysian Ringgit\nNOK - Norwegian Krone\nNZD - New Zealand Dollar\nPHP - Philippine Peso\nPLN - Polish Zloty\nRON - Romanian Leu\nRUB - Russian Rubble\nSEK - Swedish Krona\nSGD - Singapore Dollar\nTHB - Thai Baht\nTRY - Turkish Lira\nUSD - United States Dollar\nZAR - South African Rand"



    newbutton = Button(newframe, text = "Back",font = ("Comic Sans MS", 11, "bold"),  bg = "#553d67", fg = "white", activeforeground = "#553d67", activebackground = "light yellow", command = lambda:newwin.destroy())
    newbutton.place(relx = 0.83, rely = 0.93, relwidth = 0.14, relheight = 0.05)
    newwin.mainloop()

def exit():
    root.destroy()


button1["command"] =lambda:convert(clicked1.get(), clicked2.get(), entry.get())
button2["command"] = clear
button3["command"] = help
button4["command"] = exit

root.mainloop()

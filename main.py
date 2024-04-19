import tkinter as tk

calc=" "
def add_calc(symbol):
    global calc
    calc +=str(symbol)
    calc_result.delete(1.0,"end")
    calc_result.insert(1.0, calc)

def evaluate():
    global calc
    try:
        calc=str(eval(calc))
        calc_result.delete(1.0,"end")
        calc_result.insert(1.0,calc)

    except:
        clear_field()
        calc_result.insert(1.0,"error")

def clear_field():
    global calc
    calc  = " "
    calc_result.delete(1.0, "end")


root=tk.Tk()
root.geometry("310x276")
root.config(bg="#D3D3D3")


calc_result=tk.Text(root, height=1 , width=17 , font=("Arial" , 24))
calc_result.grid(columnspan=5)

button__1=tk.Button(root,text="1" ,command=lambda: add_calc(1) , width=5 , font=('Arial', 14))
button__1.grid(row=2,column=1)

button__2=tk.Button(root,text="2" ,command=lambda: add_calc(2) , width=5 , font=('Arial', 14))
button__2.grid(row=2,column=2)

button__3=tk.Button(root,text="3" ,command=lambda: add_calc(3) , width=5 , font=('Arial', 14))
button__3.grid(row=2,column=3)

button__4=tk.Button(root,text="4" ,command=lambda: add_calc(4) , width=5 , font=('Arial', 14))
button__4.grid(row=3,column=1)

button__5=tk.Button(root,text="5" ,command=lambda: add_calc(5) , width=5 , font=('Arial', 14))
button__5.grid(row=3,column=2)

button__6=tk.Button(root,text="6" ,command=lambda: add_calc(6) , width=5 , font=('Arial', 14))
button__6.grid(row=3,column=3)

button__7=tk.Button(root,text="7" ,command=lambda: add_calc(7) , width=5 , font=('Arial', 14))
button__7.grid(row=4,column=1)

button__8=tk.Button(root,text="8" ,command=lambda: add_calc(8) , width=5 , font=('Arial', 14))
button__8.grid(row=4,column=2)

button__9=tk.Button(root,text="9" ,command=lambda: add_calc(9) , width=5 , font=('Arial', 14))
button__9.grid(row=4,column=3)

button__0=tk.Button(root,text="0" ,command=lambda: add_calc(0) , width=5 , font=('Arial', 14))
button__0.grid(row=5,column=2)

button__plus=tk.Button(root,text="+" ,command=lambda: add_calc("+") , width=5 , font=('Arial', 14))
button__plus.grid(row=2,column=4)

button__minus=tk.Button(root,text="-" ,command=lambda: add_calc("-") , width=5 , font=('Arial', 14))
button__minus.grid(row=3,column=4)

button__multiply=tk.Button(root,text="*" ,command=lambda: add_calc("*") , width=5 , font=('Arial', 14))
button__multiply.grid(row=4,column=4)

button__div=tk.Button(root,text="/" ,command=lambda: add_calc("/") , width=5 , font=('Arial', 14))
button__div.grid(row=5,column=4)

button__openbrac=tk.Button(root,text="(" ,command=lambda: add_calc("(") , width=5 , font=('Arial', 14))
button__openbrac.grid(row=5,column=1)

button__closebrac=tk.Button(root,text=")" ,command=lambda: add_calc(")") , width=5 , font=('Arial', 14))
button__closebrac.grid(row=5,column=3)

button__equal=tk.Button(root,text="=" ,command=evaluate, width=5 , font=('Arial', 14),bg="orange")
button__equal.grid(row=6,column=4)

button__clear=tk.Button(root,text="AC" ,command=clear_field, width=5 , font=('Arial', 14),bg="orange")
button__clear.grid(row=6,column=1)



root.mainloop() 
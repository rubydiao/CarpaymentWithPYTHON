from tkinter import *
f = Tk()
f.minsize(300,400)
f.maxsize(350,450)
f.title("โปรแกรมคิดค่างวดรถ")
f.configure(background = "pink")

pri = DoubleVar() #ราคา
dn= DoubleVar() #เงินดาวน์
qua = IntVar() #ผ่อน
i = DoubleVar() #ดอกเบี้ย
p = DoubleVar() #ดึงค่า pri มาเก็บไว้
d = DoubleVar() #ดึงค่า dn มาเก็บไว้ / 100
pd = DoubleVar() #ดึงค่า p และ d มาคูณกัน
t = DoubleVar() #ดึงค่า p มาลบกับ pd ได้เป็นค่าจัดไฟแนนซ์
ti = DoubleVar() 
q = IntVar() #ดึงค่า qua
i_per = DoubleVar() #ดึงค่า i มาเก็บไว้ /100
ti_ip = DoubleVar()
ti_ir = IntVar() #ค่างวดต่อเดือน
def input_change() :
    p.set(pri.get())
    d.set(dn.get()/100)
    pd.set(p.get()*d.get())
    pd.set(round(pd.get()))
    t.set(p.get()-pd.get())
    t.set(round(t.get()))
    i_per.set(i.get()/100)
    if qua.get()== 1 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/12)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 2 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/24)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 3 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/36)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 4 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/48)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 5 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/60)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 6 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/72)
        ti_ip.set(round(ti_ip.get()))
        
    elif qua.get()== 7 :
        q.set(qua.get()*t.get())
        ti.set(q.get()*i_per.get())
        ti_ir.set(ti.get()+t.get())
        ti_ip.set(ti_ir.get()/84)
        ti_ip.set(round(ti_ip.get()))
        
l_1 = Label(f,bg = "pink",fg = "white",font="AnsnaNew 15 bold",text="โปรแกรมคิดค่างวดรถ")
l_1.place(x=55,y=5)
l1 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ราคารถ :")
l1.place(x=15,y=35)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = pri)
e.place (x=65,y=35)
l_2 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="บาท")
l_2.place(x=195,y=35)
l3 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="เงินดาวน์ :")
l3.place(x=15,y=60)
l_3 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="%")
l_3.place(x=195,y=60)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = dn)
e.place (x=65,y=60)
l4 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ผ่อน :")
l4.place(x=15,y=85)
l_4 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ปี")
l_4.place(x=195,y=85)
l_4a = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="(1-7 ปี)")
l_4a.place(x=220,y=85)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = qua)
e.place (x=65,y=85)
l5 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ดอกเบี้ย :")
l5.place(x=15,y=110)
l_5 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="%")
l_5.place(x=195,y=110)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = i)
e.place (x=65,y=110)

b = Button(f,bg = "purple",fg = "white",font="AnsnaNew 8 bold",text="คำนวณ",command=input_change,width=20)
b.place(x=50,y=135)

l6 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ยอดจัดไฟแนนซ์ :")
l6.place(x=0,y=170)
l_6 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="บาท")
l_6.place(x=195,y=170)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = t)
e.place (x=65,y=170)
l7 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="เป็นเงินดาวน์ :")
l7.place(x=0,y=195)
l_7 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="บาท")
l_7.place(x=195,y=195)
e = Entry(f,fg = "blue",font="AnsnaNew 8 bold",textvariable = pd)
e.place (x=65,y=195)
l8 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="ค่างวดต่อเดือน :")
l8.place(x=0,y=220)
l_8 = Label(f,bg = "pink",font="AnsnaNew 8 bold",text="บาท")
l_8.place(x=195,y=220)
e = Entry(f,fg = "red",font="AnsnaNew 8 bold",textvariable =  ti_ip)
e.place (x=65,y=220)


f.mainloop()

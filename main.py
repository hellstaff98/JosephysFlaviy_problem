from math import sin, cos, pi
from tkinter import *


class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def delete_element_by_value(self, x):
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref
        if n.ref is None:
            print("item not found in the list")
        else:
            n.ref = n.ref.ref

def initializing():
    global step, r, edge, people, speed
    box.delete('all')
    scale1.config(state=ACTIVE)
    scale2.config(state=ACTIVE)
    but.config(state=ACTIVE)
    amount = int(scale1.get())
    step = int(scale2.get())
    speed = int(scale3.get())
    r = amount * 6
    edge = 2 * pi / amount
    people = []
    for i in range(amount):
        people.append(
            box.create_oval(start[0] + r * cos(edge * i), start[1] + r * sin(edge * i),
                            start[0] + r * cos(edge * i) + 30,
                            start[1] + r * sin(edge * i) + 30))
        box.create_text(start[0] + r * cos(edge * i) + 15, start[1] + r * sin(edge * i) + 15, text=i + 1)
    box.update_idletasks()
    for j in range(1, amount + 1):
        list1.insert_at_end(j)
    scale1.config(state=DISABLED)
    scale2.config(state=DISABLED)
    but.config(state=DISABLED)
    win.after(200, traverse_list)

def traverse_list():
    global now, n
    n = list1.start_node
    if n.ref is not None:
        nextS()
    else:
        win.after(1000,box.itemconfig(people[n.item-1], fill = 'green'))
        but.config(state=ACTIVE)
        scale1.config(state=ACTIVE)
        scale2.config(state=ACTIVE)


def nextS():
    global now, dif, n
    print(n.item, " ")
    line = box.create_line(start[0]+15,start[1]+15, (start[0] + r * cos(edge * (n.item-1))+ 15, start[1] + r * sin(edge * (n.item-1))+15))
    box.update_idletasks()
    if now == step:
        now = 1
        list1.delete_element_by_value(n.item)
        win.after(int(scale3.get()),box.itemconfig(people[n.item - 1], fill='red'))
        win.after(int(scale3.get())-50, box.delete(line))
        dif = True
    else:
        now += 1
        win.after(int(scale3.get()), box.delete(line))
    n = n.ref
    box.update_idletasks()

    if n is not None :
        win.after(int(scale3.get()), nextS)
    else:
        win.after(int(scale3.get()),traverse_list)


now = 1
start = (350, 200)

list1 = LinkedList()


win = Tk()
win.title('Задача Иосифа Флавия')
win.geometry('+0+0')
win.resizable(False, False)
box = Canvas(win, width=700, height=410)
fr1=Frame(win)
fr2=Frame(win)
fr3=Frame(win)
scale1 = Scale(fr1, orient='horizontal', resolution=1, from_=1, to=30)
scale1.set(10)

scale2 = Scale(fr2, orient='horizontal', resolution=1, from_=2, to=15)
scale2.set(3)

scale3 = Scale(fr3, orient='horizontal', resolution=10, from_=100, to=1000)
scale3.set(400)

but = Button(win, text='Старт', command=initializing)

Label(fr1, text='Количество людей:', font=('Arial', 13)).grid(row=1, column=0, sticky=S)
Label(fr2, text='Длина шага:', font=('Arial', 13)).grid(row=2, column=0, sticky=S)
Label(fr3, text='Задержка:', font=('Arial', 13)).grid(row=2, column=0, sticky=S)
Label(text='© Леонтьев 2022', font=('Arial', 10)).grid(row=5, column=1)

fr1.grid(row=1, column=0, columnspan=2, pady=10)
fr2.grid(row=2, column=0, columnspan=2, pady=10)
fr3.grid(row=3, column=0, columnspan=2, pady=10)
but.grid(row=4, column=0, columnspan=2, pady=10)
box.grid(row=0, column=0, columnspan=2)
scale1.grid(row=1, column=1)
scale2.grid(row=2, column=1)
scale3.grid(row=2, column=1)
mainloop()

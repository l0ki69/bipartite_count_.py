import tkinter as tk
from tkinter import *

class List():
    def __init__(self):
        self.vertex = 0
        self.Adj = []
        self.C = [False] * self.vertex  # visit
        self.G = [3] * self.vertex  # color
        self.k = 0
        # -1 - Red
        # 1 - Black

    def add(self, strbuf):
        q = True
        for i in range(0,len(strbuf)):
            if strbuf[i].isdigit():
                q = True
            else:
                q = False
                break
        if q:
            self.k +=1
            Str = "Введите вершины соединенные с вершиной " + str(self.k)
            show1.set(Str)
            showLabe1 = Label(root, textvariable = show1)
            showLabe1.place(x=0, y=120, width=300, height=15)

            buf = []
            for i in range(0, len(strbuf)):
                buf.append(int(strbuf[i]))
            self.Adj.append(buf[:])
            show4.set("Все верно")
            showLabe4 = Label(root, textvariable=show4)
            showLabe4.place(x=0, y=325, width=300, height=35)
        else:
            show4.set("Вершины заданы не корректно")
            showLabe4 = Label(root, textvariable=show4)
            showLabe4.place(x=0, y=325, width=300, height=35)

    def addvertex(self):
        buf = entry.get()
        if str(buf).isdigit():
            k = int(buf)
            self.vertex = k
            self.C = [False] * self.vertex  # visit
            self.G = [3] * self.vertex  # color
            show4.set("Все верно")
            showLabe4 = Label(root, textvariable=show4)
            showLabe4.place(x=0, y=325, width=300, height=35)
        else:
            show4.set("Кол-во вершин задано не корректно")
            showLabe4 = Label(root, textvariable = show4)
            showLabe4.place(x=0, y=325, width=300, height=35)

    def Print(self):
        show2.set(self.Adj)
        showLabe2 = Label(root, textvariable=show2)
        showLabe2.place(x=0, y=205, width=300, height=15)
        print(self.vertex,self.Adj)

    def bfs(self, graph, start):
        queue = [start]
        self.G[start] = 1
        self.C[start] = True
        while queue:
            temp = queue.pop(0)
            for g in graph[temp]:
                if (self.C[g]):
                    # print("g = ", g," G[g] = ", G[g], " temp = ",temp, " G[temp] = " ,G[temp])
                    if (self.G[g] == self.G[temp]):
                        return False
                    continue
                else:
                    self.C[g] = True
                    self.G[g] = self.G[temp] * (-1)
                    queue.append(g)
        return True

    def work(self):

        if self.bfs(self.Adj,0): str = "yes, the count is dicotyledonous"
        else: str  = "no count dicotyledonous"

        show3.set(str)
        showLabe3 = Label(root, textvariable=show3)
        showLabe3.place(x=0, y=290, width=300, height=35)

dll = List()
root = Tk()
root.title("Graph")
root.geometry("300x400")

show = StringVar()
show1 = StringVar()
show2 = StringVar()
show3 = StringVar()
show4 = StringVar()
entry = StringVar()
entry1 = StringVar()





def add():
    dll.add(entry1.get().split())


def showS():
    show.set(dll.show())


def Task():
    dll.sort()
    show.set(dll.show())

def Print():
    dll.Print()


show.set("Введите кол-во вершин графа")

showLabe = Label(root, textvariable = show)
showLabe.place(x = 0, y = 0, width = 300, height = 35)

addEntry = Entry(root, textvariable = entry)
addEntry.place(x = 0, y = 35, width = 300, height = 35)

addButton = Button(root, text="Ввести кол-во вершин", command =  dll.addvertex )
addButton.place(x=0, y= 70, width=300, height=35)


show1.set("Введите вершины соединенные с вершиной " + str(0))
showLabe1 = Label(root, textvariable = show1)
showLabe1.place(x=0, y= 120, width=300, height=15)

addEntry1 = Entry(root, textvariable = entry1)
addEntry1.place(x = 0, y = 135, width = 300, height = 35)

addButton1 = Button(root, text="Добавить элемент", command = add )
addButton1.place(x=0, y= 170, width=300, height=35)


show2.set("")
showLabe2 = Label(root, textvariable = show2)
showLabe2.place(x=0, y= 205, width=300, height=15)

addButton2 = Button(root, text="Вывести", command = Print )
addButton2.place(x=0, y= 220, width=300, height=35)

addButton3 = Button(root, text="Проверить граф на двудольность", command = dll.work )
addButton3.place(x=0, y= 255, width=300, height=35)


root.mainloop()


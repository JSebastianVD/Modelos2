from tkinter import *
import math

class Figuras:
    __pos = []
    __canvas, __marco, antx, anty, x, y = None, None, None, None, None, None
    def __init__(self):
        self.__marco = Tk()
        self.__marco.title("Linea")
        self.__marco.geometry("700x500")
        self.__canvas = Canvas(self.__marco, width=700, height=400, bg="white")
        self.__canvas.place(x=0,y=100)
        self.__canvas.pack



    def eventoMouse(self,event):
        self.__pos.append(str(event.x) + "-" + str(event.y))
        self.__canvas.create_oval(event.x-1,event.y-1,event.x+1,event.y+1, fill = "black")
        aux = 0
        for p in self.__pos:
            xy = p.split("-")
            self.x = xy[0]
            self.y = xy[1]
            if aux == 0:
                self.antx = self.x
                self.anty = self.y
                aux = 1
            else:
                r = math.sqrt((int(self.x) - int(self.antx)) ** 2 + (int(self.y) - int(self.anty)) ** 2)
                self.getCanvas().create_oval(int(self.antx) + r, int(self.anty) + r, int(self.antx) - r,
                                             int(self.anty) - r, fill="midnight blue")
                self.getCanvas().create_rectangle(int(self.antx), int(self.anty), int(self.x), int(self.y),
                                                  fill="yellow")
                self.getCanvas().create_polygon(int(self.x), int(self.y), int(self.antx), int(self.anty),
                                                int(self.x), int(self.anty), fill="red")
                break
        self.__r1.set(circulo.perimetro(self))
        self.__r2.set(circulo.area(self))
        self.__r3.set(cuadrado.perimetro(self))
        self.__r4.set(cuadrado.area(self))
        self.__r5.set(triangulo.perimetro(self))
        self.__r6.set(triangulo.area(self))

    def modulo(self):
        r = math.sqrt((int(self.x) - int(self.antx)) ** 2 + (int(self.y) - int(self.anty)) ** 2)
        return r

    def getCanvas(self):
        return self.__canvas

    def getMarco(self):
        return self.__marco

    def area(self):
        pass

    def perimetro(self):
        pass


    def configurar(self):
        self.__canvas.bind("<Button-1>", self.eventoMouse)
        # Circulo
        self.__r1 = StringVar()
        self.__r2 = StringVar()
        self.l1 = Label(self.__marco, text = "Perimetro = ").place(x = 10, y = 20)
        self.__resultado1 = Label(self.__marco, textvariable = self.__r1).place(x = 80, y= 20)
        self.l2 = Label(self.__marco, text="Area = ").place(x=10, y=70)
        self.__resultado2 = Label(self.__marco, textvariable=self.__r2).place(x=80, y=70)
        # Cuadrado
        self.__r3 = StringVar()
        self.__r4 = StringVar()
        self.l3 = Label(self.__marco, text="Perimetro = ").place(x=210, y=20)
        self.__resultado3 = Label(self.__marco, textvariable=self.__r3).place(x=280, y=20)
        self.l4 = Label(self.__marco, text="Area = ").place(x=210, y=70)
        self.__resultado4 = Label(self.__marco, textvariable=self.__r4).place(x=280, y=70)
        # Triangulo
        self.__r5 = StringVar()
        self.__r6 = StringVar()
        self.l5 = Label(self.__marco, text="Perimetro = ").place(x=410, y=20)
        self.__resultado1 = Label(self.__marco, textvariable=self.__r5).place(x=480, y=20)
        self.l6 = Label(self.__marco, text="Area = ").place(x=410, y=70)
        self.__resultado2 = Label(self.__marco, textvariable=self.__r6).place(x=480, y=70)
        self.__marco.mainloop()


class circulo(Figuras):
    def __init__(self):
        Figuras.__init__(self)

    def perimetro(self):
        r = self.modulo()
        p = 2*math.pi*r
        return p


    def area(self):
        a = math.pi * (self.modulo()**2)
        return a



class cuadrado(Figuras):

    def __init__(self):
        Figuras.__init__(self)


    def perimetro(self):
        self.__lx = math.sqrt((int(self.x) - int(self.antx)) ** 2)
        self.__ly = math.sqrt((int(self.anty) - int(self.y)) ** 2)
        p = (self.__lx*2) + (self.__ly*2)
        return p

    def area(self):
        a = self.__lx * self.__ly
        return a

class triangulo(Figuras):

    def __init__(self):
        Figuras.__init__(self)

    def perimetro(self):
        r = self.modulo()
        self.__lx = math.sqrt((int(self.x) - int(self.antx)) ** 2)
        self.__ly = math.sqrt((int(self.anty) - int(self.y)) ** 2)
        p = r + self.__lx + self.__ly
        return p

    def area(self):
        a = (self.__lx * self.__ly)/2
        return a

class maain(Figuras):
    def __init__(self):
        Figuras.__init__(self)




maaain = maain()
maaain.configurar()



from tkinter import *
import math

class Figuras:
    __pos = []
    __canvas, __marco, antx, anty, x, y = None, None, None, None, None, None
    def __init__(self):
        self.__marco = Tk()
        self.__marco.title("Linea")
        self.__marco.geometry("500x500")
        self.__canvas = Canvas(self.__marco, width=210, height=210, bg="midnight blue")
        self.__canvas.place(x=0,y=0)
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
                                             int(self.anty) - r, fill="black")
                self.getCanvas().create_rectangle(int(self.antx), int(self.anty), int(self.x), int(self.y),
                                                  fill="yellow")
                self.getCanvas().create_polygon(int(self.x), int(self.y), int(self.antx), int(self.anty),
                                                int(self.x), int(self.anty), fill="red")
                break

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


    def mostrar(self):
        self.__canvas.bind("<Button-1>", self.eventoMouse)
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
        p = (int(self.x)-int(self.antx))*4
        return p

    def area(self):
        a = math.pi * (self.modulo()**2)
        return a

class triangulo(Figuras):

    def __init__(self):
        Figuras.__init__(self)

    def perimetro(self):
        r = self.modulo
        p = r + (int(self.x)-int(self.antx))+(int(self.anty)-int(self.y))
        return p

    def area(self):
        a = math.pi * (self.modulo()**2)
        return a

    def dibujar(self,marco, canvas):

        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_oval(10, 10, self.__modulo()*100, self.__modulo()*100, width=5, fill="yellow")


# x1,y1,x2,y2 = int(input("Valor: ")),int(input("Valor: ")),int(input("Valor: ")),int(input("Valor: "))
# obj = circulo(x1,y1,x2,y2)
# obj2 = cuadrado(x1,y1,x2,y2)
# print(str(obj.area()))
# print(str(obj.perimetro()))
# obj.dibujar(marco,canvas)
# obj2.dibujar(marco,canvas)
# marco.mainloop()

obj = cuadrado()

obj.mostrar()
obj.perimetro()

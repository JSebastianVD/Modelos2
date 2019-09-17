from tkinter import *
import math

class Figuras:
    __pos = []
    __canvas,__marco, __boton = None, None, None
    def __init__(self):
        self.__marco = Tk()
        self.__marco.title("Linea")
        self.__marco.geometry("500x500")
        self.__canvas = Canvas(self.__marco, width=210, height=210, bg="midnight blue")
        self.__canvas.place(x=0,y=0)
        self.__canvas.pack

    # def __modulo(self):
    #     r = math.sqrt(((self.__y2-self.__y1)**2)+((self.__x2-self.__x1)**2))
    #     return r

    def eventoMouse(self,event):
        self.__pos.append(str(event.x) + "-" + str(event.y))
        self.__canvas.create_oval(event.x-1,event.y-1,event.x+1,event.y+1, fill = "black")
        aux = 0
        for p in self.__pos:
            xy = p.split("-")
            x = xy[0]
            y = xy[1]
            if aux == 0:
                antx = x
                anty = y
                aux = 1
            else:
                r = math.sqrt((int(x) - int(antx))**2 + (int(y) - int(anty))**2)
                self.__canvas.create_oval(int(antx) +r, int(anty) +r , int(antx)-r, int(anty)-r, fill="black")
                self.__canvas.create_rectangle(int(antx), int(anty),int(x),int(y), fill="yellow")
                self.__canvas.create_polygon(int(x),int(y), int(antx), int(anty), int(x), int(anty), fill= "red")
                break


    def mostrar(self):
        self.__canvas.bind("<Button-1>", self.eventoMouse)
        self.__marco.mainloop()


class circulo:

    def __init__(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def __modulo(self):
        r = math.sqrt(((self.__y2-self.__y1)**2)+((self.__x2-self.__x1)**2))
        return r

    def perimetro(self):
        p = 2*math.pi*self.__modulo()
        return p

    def area(self):
        a = math.pi * (self.__modulo()**2)
        return a

    def dibujar(self,marco,canvas):
        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_oval(10, 10, self.__modulo()*100, self.__modulo()*100, width=5, fill="yellow")


class cuadrado:

    def __init__(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def __modulo(self):
        r = math.sqrt(((self.__y2-self.__y1)**2)+((self.__x2-self.__x1)**2))
        return r

    def perimetro(self):
        p = 2*math.pi*self.__modulo()
        return p

    def area(self):
        a = math.pi * (self.__modulo()**2)
        return a

    def dibujar(self,marco, canvas):
        canvas.pack(expand=YES, fill=BOTH)
        canvas.create_rectangle(10, 10, self.__modulo()*100, self.__modulo()*100, width=5, fill="yellow")


class triangulo:

    def __init__(self,x1,y1,x2,y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def __modulo(self):
        r = math.sqrt(((self.__y2-self.__y1)**2)+((self.__x2-self.__x1)**2))
        return r

    def perimetro(self):
        p = 2*math.pi*self.__modulo()
        return p

    def area(self):
        a = math.pi * (self.__modulo()**2)
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

obj = Figuras()
obj.mostrar()



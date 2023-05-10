from tkinter import *


ventana = Tk()
ventana.title("calculadora")

entrada_texto =Entry(ventana,font=("Calibri 20"))
entrada_texto.grid(row=0,column=0,columnspan=4,padx=5,pady=2)




#funciones 
i = 0
def click_boton(valor):
  global i
  entrada_texto.insert(i,valor)
  i+=1
  
def operacion():
  result = eval(entrada_texto.get())
  print(result)
  entrada_texto.delete(0,END)
  i=0
  entrada_texto.insert(0,result)
  


def borrar():
  entrada_texto.delete(0,END)
#botones 
boton_borrar=Button(ventana,width=5,height=2,text="AC",command=lambda:borrar())
boton_parentesis = Button(ventana,width=5,height=2,text="(",command=lambda:click_boton("("))
boton_parentesis2=Button(ventana,width=5,height=2,text=")",command= lambda:click_boton(")"))
boton_div=Button(ventana,width=5,height=2,text="/",command= lambda:click_boton("/"))

boton7=Button(ventana,width=5,height=2,text="7",command= lambda:click_boton(7))
boton8=Button(ventana,width=5,height=2,text="8",command= lambda:click_boton(8))
boton9=Button(ventana,width=5,height=2,text="9",command= lambda:click_boton(9))
boton_mult=Button(ventana,width=5,height=2,text="*",command= lambda:click_boton("*"))

boton4=Button(ventana,width=5,height=2,text="4",command= lambda:click_boton(4))
boton5=Button(ventana,width=5,height=2,text="5",command= lambda:click_boton(5))
boton6=Button(ventana,width=5,height=2,text="6",command= lambda:click_boton(6))
boton_suma=Button(ventana,width=5,height=2,text="+",command= lambda:click_boton("+"))

boton1=Button(ventana,width=5,height=2,text="1",command= lambda:click_boton(1))
boton2=Button(ventana,width=5,height=2,text="2",command= lambda:click_boton(2))
boton3=Button(ventana,width=5,height=2,text="3",command= lambda:click_boton(3))
boton_resta=Button(ventana,width=5,height=2,text="-",command= lambda:click_boton("-"))

boton0=Button(ventana,width=16,height=2,text="0",command= lambda:click_boton(0))
boton_punto=Button(ventana,width=5,height=2,text=".",command= lambda:click_boton("."))
boton_igual=Button(ventana,width=5,height=2,text="=",command= lambda:operacion())

#posicion botones 
boton_borrar.grid(row=1,column=0,padx=2,pady=2)
boton_parentesis.grid(row=1,column=1,padx=2,pady=2)
boton_parentesis2.grid(row=1,column=2,padx=2,pady=2)
boton_div.grid(row=1,column=3,padx=2,pady=2)

boton7.grid(row=2,column=0,padx=2,pady=2)
boton8.grid(row=2,column=1,padx=2,pady=2)
boton9.grid(row=2,column=2,padx=2,pady=2)
boton_mult.grid(row=2,column=3,padx=2,pady=2)

boton4.grid(row=3,column=0,padx=2,pady=2)
boton5.grid(row=3,column=1,padx=2,pady=2)
boton6.grid(row=3,column=2,padx=2,pady=2)
boton_suma.grid(row=3,column=3,padx=2,pady=2)

boton1.grid(row=4,column=0,padx=2,pady=2)
boton2.grid(row=4,column=1,padx=2,pady=2)
boton3.grid(row=4,column=2,padx=2,pady=2)
boton_resta.grid(row=4,column=3,padx=2,pady=2)

boton0.grid(row=5,column=0,padx=2,pady=2,columnspan=2)
boton_punto.grid(row=5,column=2,padx=2,pady=2)
boton_igual.grid(row=5,column=3,padx=2,pady=2)
#estilos botones 


ventana.mainloop()
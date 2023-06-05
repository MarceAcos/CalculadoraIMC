from tkinter import *
from tkinter import ttk 
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image

#Creamos la ventana
ventana = Tk()
ventana.title('CALCULADORA DE IMC')
ventana.geometry('300x600')
ventana.configure(bg='white')


#Definimos el calculo
def calcular():
    try:
        peso = int(peso_2.get())
    except ValueError:
        messagebox.showerror('Error', 'Introduce un numero entero en el peso')

    try:
        altura = float(altura_letra2.get())
    except ValueError:
        messagebox.showerror('Error', 'Introduce un número decimal en la altura ( . )')

    imc = peso / (altura**2)
    resultado = imc


    if resultado < 18.5:
        resultado_texto['text'] = 'Tienes bajo peso'
        bajopeso_ubi.place(x=30, y=25)
    elif resultado >= 18.5 and resultado < 25:
        resultado_texto['text'] = 'Tienes un IMC normal' 
        normal_ubi.place(x=30, y=25)
    elif resultado >= 25 and resultado < 30:
        resultado_texto['text'] = 'Tienes sobre peso'
        sobrepeso_ubi.place(x=30, y=25)
    else:
        resultado_texto['text'] = 'Tienes obesidad'
        obesidad_ubi.place(x=30, y=25)

    resultado_letra['text'] = "{:.{}f}".format(resultado, 2)


#Partimos la ventana en tres partes para posicionar mejor la parte gráfica
frame_arriba = Frame(ventana, width=300, height=50, bg='white', pady= 0, padx= 0, relief='flat')
frame_arriba.grid(row=0, column=0, sticky=NSEW)

frame_abajo = Frame(ventana, width=300, height=180, bg='white', pady= 0, padx= 0, relief='flat')
frame_abajo.grid(row=1, column=0, sticky=NSEW)

frame_ultimo = Frame(ventana, width=300, height=400, bg='white', pady= 0, padx=0, relief='flat')
frame_ultimo.grid(row=3, column=0, sticky=NSEW)

#Colocamos el titulo
app_nombre = Label(frame_arriba, text='Calculadora de IMC',width=23, height=2,padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg='green', fg='white')
app_nombre.place(x=0, y=0)

#Colocamos el titulo de los consejos
consejos_titulo = Label(frame_abajo, text='Consejos', width=23, height=2, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg='green', fg='white')
consejos_titulo.place(x=0, y=195)

#Escribiendo los textos de la calculadora
peso_letra = Label(frame_abajo, text='Dime tu peso en kg', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg='white', fg='black')
peso_letra.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

#Aca se crea el cuadro en el que se va ingresar los numeros
peso_2 = Entry(frame_abajo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
peso_2.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

altura_letra = Label(frame_abajo, text='Dime tu altura en m', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg='white', fg='black')
altura_letra.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

altura_letra2 = Entry(frame_abajo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
altura_letra2.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

#Se crea el cuadro en el cual va aparecer el imc
resultado_letra = Label(frame_abajo, text='---',width=4, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg='green', fg='white')
resultado_letra.place(x=200, y=10)

#Texto en el que aparece si tiene normal, sobrepeso, etc
resultado_texto = Label(frame_abajo, text='',width=20, height=1, padx=0, pady=8, relief='flat', anchor='center', font=('Ivy 12 bold'), bg='white', fg='black')
resultado_texto.place(x=46, y=95)

#Cargamos las imagenes
bajopeso1 = Image.open('') #Agrega la ruta de la imagen dentro de las " "
bajopeso1 = bajopeso1.resize((240, 240))
photo1 = ImageTk.PhotoImage(bajopeso1)
bajopeso_ubi = tk.Label(frame_ultimo, image = photo1)

normal2 = Image.open('') #Agrega la ruta de la imagen dentro de las " "
normal2 = normal2.resize((240, 240))
photo2 = ImageTk.PhotoImage(normal2)
normal_ubi = tk.Label(frame_ultimo, image = photo2)

sobrepeso3 = Image.open("") #Agrega la ruta de la imagen dentro de las " "
sobrepeso3 = sobrepeso3.resize((240, 240))
photo3 = ImageTk.PhotoImage(sobrepeso3)
sobrepeso_ubi = tk.Label(frame_ultimo, image = photo3)

obesidad4 = Image.open('') #Agrega la ruta de la imagen dentro de las " "
obesidad4 = obesidad4.resize((240, 240))
photo4 = ImageTk.PhotoImage(obesidad4)
obesidad_ubi = tk.Label(frame_ultimo, image = photo4)

#Configuramos el boton de calcular
calcular = Button(frame_abajo, command=calcular, text='Calcular',width=31, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 11 bold'), bg='green', fg='white')
calcular.grid(row=4, column=0, sticky=NSEW, pady=70, padx=5, columnspan=60)

ventana.mainloop()
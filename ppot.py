# Autor: no7sag

import random
import tkinter as tk


def jugar(resp_usuario):
    ''' 0 = Piedra
        1 = Papel
        2 = Tijera '''
    
    global cont_racha
    resp_cpu = random.randint(0, 2)
        
    # Piedra
    if resp_usuario == 0:
        if resp_cpu == 2:
            resultado.config(text='La computadora eligió tijera. Ganaste!')
            cont_racha += 1
        if resp_cpu == 1:
            resultado.config(text='La computadora eligió papel. Perdiste!')
            cont_racha = 0
        if resp_cpu == 0:
            resultado.config(text='La computadora eligió piedra. Empate!')
    # Papel
    if resp_usuario == 1:
        if resp_cpu == 0:
            resultado.config(text='La computadora eligió piedra. Ganaste!')
            cont_racha += 1
        if resp_cpu == 2:
            resultado.config(text='La computadora eligió tijera. Perdiste!')
            cont_racha = 0
        if resp_cpu == 1:
            resultado.config(text='La computadora eligió papel. Empate!')
    # Tijera
    if resp_usuario == 2:
        if resp_cpu == 1:
            resultado.config(text='La computadora eligió papel. Ganaste!')
            cont_racha += 1
        if resp_cpu == 0:
            resultado.config(text='La computadora eligió piedra. Perdiste!')
            cont_racha = 0
        if resp_cpu == 2:
            resultado.config(text='La computadora eligió tijera. Empate!')
    
    generar_contador(cont_racha)


def generar_contador(cont_racha):
    ''' Mientras mayor sea el parámetro cont_racha, más
        signos de exclamación tendrá el mensaje de racha '''
        
    texto_racha = f'Racha de victorias: {cont_racha}'
    
    if cont_racha > 2: texto_racha = f'{texto_racha}!'  # ! x 2
    if cont_racha > 4: texto_racha = f'{texto_racha}!'  # ! x 3
    if cont_racha > 9: texto_racha = f'{texto_racha}!'  # ! x 4
    
    racha.config(text=texto_racha)


# Interfaz
window = tk.Tk()
window.title('Jueguito en Python')
window.resizable(False, False)
#window.iconbitmap(default='img\icon.ico')

# Texto superior
label = tk.Label(window, text='Piedra, papel o tijera')
label.grid(row=0, columnspan=4, padx=10, pady=18)

# Imágenes
img_rock = tk.PhotoImage(file = r'img\rock.png')
canvas_rock = tk.Canvas(window, width=192, height=128)
canvas_rock.create_image(96, 64, image=img_rock) 
canvas_rock.grid(row=1, column=0)

img_paper = tk.PhotoImage(file = r'img\paper.png')
canvas_paper = tk.Canvas(window, width=192, height=128)
canvas_paper.create_image(96, 64, image=img_paper) 
canvas_paper.grid(row=1, column=1)

img_scissors = tk.PhotoImage(file = r'img\scissors.png')
canvas_scissors = tk.Canvas(window, width=192, height=128)
canvas_scissors.create_image(96, 64, image=img_scissors) 
canvas_scissors.grid(row=1, column=2)

# Botones
button_piedra = tk.Button(window, text='Piedra')
button_piedra.config(command=lambda: jugar(0))
button_piedra.grid(row=2, column=0, padx=10, pady=10)

button_papel = tk.Button(window, text='Papel')
button_papel.config(command=lambda: jugar(1))
button_papel.grid(row=2, column=1, padx=10, pady=10)

button_tijera = tk.Button(window, text='Tijera')
button_tijera.config(command=lambda: jugar(2))
button_tijera.grid(row=2, column=2, padx=10, pady=10)

# Texto inferior
resultado = tk.Label(window, text=None)
resultado.grid(row=4, columnspan=4, sticky=tk.W+tk.E)

racha = tk.Label(window, text=None)
racha.grid(row=5, columnspan=4, sticky=tk.W+tk.E)

# Inicializar
if __name__ == '__main__':
    cont_racha = 0
    window.mainloop()

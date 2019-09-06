# coding: utf-8
# https://yadi.sk/d/e06rsSVo3CJU9L

# Комментарий

# # Транспонирование матрицы
# matrix = [[0.5, 0, 0, 0, 0],
#         [ 1, 0.5, 0, 0, 0],
#         [ 1, 1, 0.5, 0, 0],
#         [ 1, 1, 1, 0.5, 0],
#         [ 1, 1, 1, 1, 0.5]]

# #Транспонирование
# matrix_t = list(zip(*matrix))

# # Вывод матриц
# print(matrix)
# print(matrix_t)

# SublimeREPL

# import tkinter
from tkinter import *
from random import shuffle
import os
# import time  # sleep

SIDE = 6                   # кол-во элеметов в строке и столбце
QSIDE = (SIDE ** 2) // 2   # кол-во уникальных значений        

prev = None

print('Memorizer')


def cmd():      # PEP-8
    x = 13
    print('Алиса, выпей чаю!')
    print(x)


def hide_all(btns):
    pass                # nop ;; no operation
    for i in range(SIDE):
        for j in range(SIDE):
            # btns[i][j].configure(text=' ? ')
            btns[i][j].configure(image=faq)


def hide_both(btns, i1, j1, i2, j2):
    # btns[i1][j1].configure(text=' ? ')
    # btns[i2][j2].configure(text=' ? ')
    btns[i1][j1].configure(image=faq)
    btns[i2][j2].configure(image=faq)


def change(btns, xs, i, j):
    global prev

    # btns[i][j].configure(text='{:>3}'.format(xs[i * SIDE + j]))
    btns[i][j].configure(image=imgs[i * SIDE + j])
    if prev:
        if xs[i * SIDE + j] != xs[prev[0] * SIDE + prev[1]]:
            main_window.after(1000, hide_both, btns, prev[0], prev[1], i, j)
        prev = None    
    else:
        prev = (i, j)    



# def <lambda> (ii=i, jj=j):
#  return change(buttons, ls, ii, jj)

main_window = Tk()
main_window.title('Запоминалка')

faq = PhotoImage(file='FAQ.gif')

# ls = []
# for i in range(1, 100):
#     ls.append(i)

# Создаем список имён файлов картинок
images = [os.path.join('gif', f) for f in os.listdir('gif')]

shuffle(images)     # перемешиваем список
images = images[:QSIDE] * 2     # берём срез от списка и размножаем его
shuffle(images)                  # ещё раз перемешаем
print(images)

# Создаем список картинок на основании имён файлов
imgs = [PhotoImage(file=f) for f in images]

ls = [i for i in range(1, 100)]     # что происходит см. выше
shuffle(ls)     # перемешиваем список
ls = ls[:QSIDE] * 2     # берём срез от списка и размножаем его
shuffle(ls)             # ещё раз перемешаем
print(ls)


buttons = []
for i in range(SIDE):
    buttons.append([])
    for j in range(SIDE):
        x = ls[i * SIDE + j]
        button = Button(main_window, # text=' ? ',
                                # text='{:>3}'.format(x), 
                                image=imgs[i * SIDE + j],
                                font=('Courier New', 12, 'normal'),
                                relief=FLAT, 
                                command=lambda ii=i, jj=j: change(buttons, images, ii, jj))
        buttons[i].append(button)
        # button.pack()
        button.grid(row=i, column=j)


main_window.after(2000, hide_all, buttons)
main_window.mainloop()
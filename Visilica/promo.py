import random                   
import turtle
import sys
import time
def gotoxy(x, y):                  #функция указывающая где начать рисовать в системе координат 
     turtle.penup()
     turtle.goto(x, y)
     turtle.pendown()

def draw_line(from_x, from_y, to_x, to_y):      #функция указывает в определенной системе координат
     gotoxy(from_x, from_y)
     turtle.goto(to_x, to_y)

def draw_head(x, y, r):
	gotoxy(-100,0)
	turtle.circle(20)


def erase (x, y):     
     gotoxy(x, y)
     turtle.color('White')
     turtle.begin_fill()
     turtle.begin_poly()
     turtle.fd(200)
     turtle.left(90)
     turtle.fd(50)
     turtle.left(90)
     turtle.fd(200)
     turtle.left(90)
     turtle.fd(50)
     turtle.left(90)
     turtle.end_poly()
     turtle.end_fill()

funcs = [draw_line, draw_line, draw_line, draw_line, draw_head, draw_line, draw_line, draw_line, draw_line, draw_line]


def draw_gibbet(step, coord):
	turtle.color('blue')
	funcs[step](*coord_list[step])

	#if step == 4:
	#	draw_head(*coord[step])
	#else:	
	#	draw_line(*coord[step])


x = random.randint(1,100)

#print(x)

turtle.speed(0)                 #скорость рисования

coord_list = []
coord = open('coord.txt')

for line in coord:
	line = line.strip().split(',')
	nums = []
	for n in line:
		nums.append(int(n))
	coord_list.append(nums)	




#draw_line(*coord_list[0])
#draw_line(*coord_list[1])
#draw_line(*coord_list[2])
#draw_line(*coord_list[3])
#draw_line(*coord_list[4])
#draw_line(*coord_list[5])
#draw_line(*coord_list[6])
#draw_line(*coord_list[7])
#draw_line(*coord_list[8])
#draw_line(*coord_list[9])

#for coord in coord_list:
#	draw_line(*coord)
#gotoxy(-100,0)
#turtle.circle(20)
	


answer = turtle.textinput("Играть?", "y/n")             #создает окно с вопросом играть или нет
if answer != "y":
	sys.exit()

hints = False  #True
answer = turtle.textinput("Давать ли подсказки", "y/n")
if answer == 'y':
	hints = True 	

try_count = 0	                                        #колличество попыток

while True:
	number = turtle.numinput("Угадайте", "Число от 0 до 100", 0, 0, 100)            #цикл до победного или же выход
	if number == x:
		erase(-150, 100)
		gotoxy(-150,200)
		turtle.color('green')
		turtle.write("Ура!Вы победили!",font=("Arial", 28, "normal"))
		break
	else:
		gotoxy(-150, 100)
		turtle.color('red')
		turtle.write("НЕ ВЕРНО!", font=("Arial", 16, "normal"))
		
		if hints:
			gotoxy(100, 100 - try_count * 15)
			if number > x:
				turtle.write(str(number) +' Загадонное число меньше!')
			else:
				turtle.write(str(number) + ' Загадонное число больше!')
				
		
		draw_gibbet(try_count, coord_list)
		try_count += 1
		
		if try_count == 10:
		    gotoxy(-100, 200)
		    turtle.color('red')
		    turtle.write("ТЫ ПРОИГРАЛ", font=("Arial", 33, "normal"))
		    break
time.sleep(5)

#dont commit

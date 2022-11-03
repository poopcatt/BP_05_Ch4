#기초파이썬 연습문제 4장 터틀그래픽



7. #사용자가 입력하는 3가지 색상을 리스트에 저장하였다가 하나씩 꺼내서 그색상으로 채워진 원을 그리는 프로그램을 작성해보자. 
   #반복문은 사용하지 않는다. 채워진 원을 그리려면 다음과 같은 문장들을 사용한다.

import turtle

colorlist=[]
color=str(input("색상 #1을 입력하시오: "))
colorlist.append(color)
color=str(input("색상 #2을 입력하시오: "))
colorlist.append(color)
color=str(input("색상 #3을 입력하시오: "))
colorlist.append(color)
print(colorlist)

t=turtle.Turtle()
t.shape("turtle")
t.fillcolor(colorlist[0])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(100,0)
t.down()
t.fillcolor(colorlist[1])
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(200,0)
t.down()
t.fillcolor(colorlist[2])
t.begin_fill()
t.circle(50)
t.end_fill()
t.screen.exitonclick()


8. #사용자가 입력하는 3개의 좌표(x, y)를 리스트에 저장한다. 이들 좌표를 꺼내서 거북이를 이동하는 프로그램을 작성해보자.

import turtle
t=turtle.Turtle()
t.shape("turtle")
x1= int(input("x1:"))
y1= int(input("y1:"))
x2= int(input("x2:"))
y2= int(input("y2:"))
x3= int(input("x3:"))
y3= int(input("y3:"))

list_x=[x1,x2,x3]
list_y=[y1,y2,y3]
t.goto(list_x[0],list_y[0])
t.goto(list_x[1],list_y[1])
t.goto(list_x[2],list_y[2])
t.screen.exitonclick()

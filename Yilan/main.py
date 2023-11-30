import turtle
import time
import random

hiz = 0.15
puan = 0
kuyruklar = []
pencere = turtle.Screen()
pencere.title("Yılan Oyunu by Khajz")
pencere.bgpic('Yilan\cg.png')
pencere.setup(width=600, height=600)
pencere.tracer(0)
pencere.addshape('Yilan\hmbr.gif')
pencere.addshape('Yilan\hd.gif')
pencere.addshape('Yilan\lahm.gif')

kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('Yilan\hd.gif')
kafa.color('orange')
kafa.penup()
kafa.goto(0, 100)
kafa.direction = 'stop'

kuyrukyaz = turtle.Turtle()
kuyrukyaz.speed(0)
kuyrukyaz.shape('square')
kuyrukyaz.color('white')
kuyrukyaz.penup()
kuyrukyaz.goto(160, -268)
kuyrukyaz.hideturtle()
kuyrukyaz.write('Kuyruklar:{}'.format(len(kuyruklar)), align='center', font=('Courier', 24, 'normal'))

puanyaz = turtle.Turtle()
puanyaz.speed(0)
puanyaz.shape('square')
puanyaz.color('white')
puanyaz.penup()
puanyaz.goto(-200, -268)
puanyaz.hideturtle()
puanyaz.write('Puan:{}'.format(puan), align='center', font=('Courier', 24, 'normal'))

yem = turtle.Turtle()
yem.speed(0)
yem.shape('Yilan\hmbr.gif')
yem.color('green')
yem.penup()
yem.goto(0, 0)


yem1 = turtle.Turtle()
yem1.speed(0)
yem1.shape('Yilan\lahm.gif')
yem1.color('green')
yem1.penup()
yem1.goto(1500, 1500)


def hareket():
    if kafa.direction=='up':
        y = kafa.ycor()
        kafa.sety(y + 20)
    if kafa.direction=='down':
        y = kafa.ycor()
        kafa.sety(y - 20)
    if kafa.direction=='left':
        x = kafa.xcor()
        kafa.setx(x - 20)
    if kafa.direction=='right':
        x = kafa.xcor()
        kafa.setx(x + 20)
        
def yukariHareket():
    if kafa.direction != 'down':
        kafa.direction = 'up'
def asagiHareket():
    if kafa.direction != 'up':
        kafa.direction = 'down'
def solaHareket():
    if kafa.direction != 'right':
        kafa.direction = 'left'
def sagaHareket():
    if kafa.direction != 'left':
        kafa.direction = 'right'    

pencere.listen()
pencere.onkey(yukariHareket, 'Up')
pencere.listen()
pencere.onkey(asagiHareket, 'Down')
pencere.listen()
pencere.onkey(solaHareket, 'Left')
pencere.listen()
pencere.onkey(sagaHareket, 'Right')
pencere.listen()


while True:
    pencere.update()
    if kafa.xcor() > 260 or kafa.xcor() < -260 or kafa.ycor() > 280 or kafa.ycor() < -180:
        kafa.direction='stop'
        time.sleep(1)
        puan = 0
        puanyaz.clear()
        puanyaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
        kafa.goto(0, 0)
        yem1.goto(1500,1500)
        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)
            hiz = 0.15
            kuyruklar=[]
            kuyrukyaz.clear()
            kuyrukyaz.write('Kuyruklar: {}'.format(len(kuyruklar)), align='center', font=('Courier', 24, 'normal'))
    
    if kafa.distance(yem)<30:
        x= random.randint(-240,240)
        y= random.randint(-170,240)
        yem.goto(x,y)
        
        puan = puan + 10  
        puanyaz.clear()
        puanyaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))
        if puan>=150 and puan<250:
            puan = puan + 20
        elif puan>=250 and puan<400:
            puan = puan + 30
        elif puan>=400:
            puan = puan + 40
        
        hiz = hiz - 0.003
        yeniKuyruk = turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('circle')
        yeniKuyruk.color('green')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)
        kuyrukyaz.clear()
        kuyrukyaz.write('Kuyruklar: {}'.format(len(kuyruklar)), align='center', font=('Courier', 24, 'normal'))
        
    if puan>150 and puan<210:
        yem1.goto(0,0)
        
    if kafa.distance(yem1)<30:
        x = random.randint(-240,240)
        y = random.randint(-170,240)
        yem1.goto(x,y)
        x = random.randint(-240,240)
        y = random.randint(-170,240)
        yem.goto(x,y)
        hiz = hiz - 0.004   
        puan = puan + 50
        puanyaz.clear() 
        puanyaz.write('Puan: {}'.format(puan), align='center', font=('Courier', 24, 'normal'))    
        if puan>=150 and puan<250:
            puan = puan + 20
        elif puan>=250 and puan<400:
            puan = puan + 30
        elif puan>=400:
            puan = puan + 50        
    for i in range(len(kuyruklar)- 1, 0, -1):
        x = kuyruklar[i-1].xcor()
        y = kuyruklar[i-1].ycor()
        kuyruklar[i].goto(x,y)
    if len(kuyruklar)>0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y)

    hareket()
    time.sleep(hiz)
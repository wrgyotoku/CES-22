#Ex1.
#nos permite usar turtle
import turtle
#cor da caneta rosa
turtle.pencolor("lightpink")
#tamanho da caneta
turtle.pensize(3)
#Configura a janela e seus atributos
wn = turtle.Screen()
#cor da tela verde
wn.bgcolor("lightgreen")
#Para fazer 5 formas de quadrados
for quadrado in range(0, 5):
    #Desenha o quadrado
    for i in range(4):
        turtle.forward(20 + quadrado * 20)
        turtle.left(90)
    #Vai para o novo quadrado de maneira concentrica
    #interrompe o desenho
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(180)
    # volta a desenhar
    turtle.pendown()
#Espera usuario fechar a janela
wn.mainloop()
########################################################
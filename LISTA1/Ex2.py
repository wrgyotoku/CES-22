#Ex.2
import turtle
#Funcao recebe parametros turtle t, n lados, de lado sz
def draw_poly(t, n, sz):
    """Faz turtle t desenhar poligono regular de sz."""
    a = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(a)


#Cria turtle tess
tess = turtle.Turtle()
#cor da caneta rosa
tess.pencolor("lightpink")
#tamanho da caneta
tess.pensize(3)
#Configura a janela e seus atributos
wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("tess meets a function")
#Teste que chama a funcao para desenhar poligono regular
draw_poly(tess, 8, 50)
wn.mainloop()
#############################################################
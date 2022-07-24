#Creado por Miguel Yáñez
#Muestra de interfaz gráfica con turtle

import turtle
import sys


#------------------------------------------------Interfaz de Inicio--------------------------------------------------------------
ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("Laberinto")
ventana.setup(700, 700)

global contador
contador = 0

#------------------------------------------------Entidades--------------------------------------------------------------
class Bloques(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

class Jugador(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("circle")
		self.color("red")
		self.penup()
		self.speed(0)

	def subir(self):
		global contador
		moverX = self.xcor()
		moverY = self.ycor() + 24

		if (moverX, moverY) not in muros:
			self.goto(moverX, moverY)

		if (moverX, moverY) in goal:
			contador += 1
			cambiarNivel()

	def bajar(self):
		global contador
		moverX = self.xcor()
		moverY = self.ycor() - 24

		if (moverX, moverY) not in muros:
			self.goto(moverX, moverY)

		if (moverX, moverY) in goal:
			contador += 1
			cambiarNivel()

	def izquierda(self):
		global contador
		moverX = self.xcor() - 24
		moverY = self.ycor()

		if (moverX, moverY) not in muros:
			self.goto(moverX, moverY)

		if (moverX, moverY) in goal:
			contador += 1
			cambiarNivel()

	def derecha(self):
		global contador
		moverX = self.xcor() + 24
		moverY = self.ycor()

		if (moverX, moverY) not in muros:
			self.goto(moverX, moverY)

		if (moverX, moverY) in goal:
			contador += 1
			cambiarNivel()

class Meta(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("yellow")
		self.penup()
		self.speed(0)

#--------------------------------------------------Niveles--------------------------------------------------------------
#Cambiar niveles (Orden del apendice)
nivelUno = [
	"XXXXXXXXXXXXXXXXXXXXXXXXX",
	"XPX              X      X",
	"X X XXXXXXXXXXXX X XXXX X",
	"X X     X          X    X",
	"X XXXXX X XXX XXXXXXXXXXX",
	"X X     X X X           X",
	"X X XXXXX   XXXXXXX XXX X",
	"X   X     X   X       X X",
	"XXXXX XXXXXXX X XXXXX X X",
	"X             X X   X X X",
	"X XXXXXXXXXXXXX X X X X X",
	"X X             X X X X X",
	"X X X XXXXXXXXXXX X X X X",
	"X X X X           X X X X",
	"X XXX X XXXXXXXXXXX X X X",
	"X     X             X X X",
	"XXXXXXXXXXXXXXX XXX X X X",
	"X             X X X X X X",
	"XXXXXXXXXXXXX X X X X X X",
	"X     X         X X X X X",
	"X XXX X XXXXXXXXX X X X X",
	"X X   X       X   X X X X",
	"X X X XXXXXXX X XXX XXX X",
	"X X X         X         X",
	"XXXMXXXXXXXXXXXXXXXXXXXXX"
]

nivelDos = [
	"XXXXXXXXXXXXXXXXXXXXXXXX",
	"XP                     X",
	"XXXXXXXXXXXXXXXXXXXXXX X",
	"X                    X X",
	"X XXXXXXXXXXXXXXXXXX X X",
	"X X                X X X",
	"X X XXXXXXXXXXXXXX X X X",
	"X X X            X X X X",
	"X X X XXXXXXXXXX X X X X",
	"X X X X        X X X X X",
	"X X X X XXXXXX X X X X X",
	"X X X X X    X X X X X X",
	"X X X X X XX X X X X X X",
	"X X X X X XM X X X X X X",
	"X X X X X XXXX X X X X X",
	"X X X X X      X X X X X",
	"X X X X XXXXXXXX X X X X",
	"X X X X          X X X X",
	"X X X XXXXXXXXXXXX X X X",
	"X X X              X X X",
	"X X XXXXXXXXXXXXXXXX X X",
	"X X                  X X",
	"X XXXXXXXXXXXXXXXXXXXX X",
	"X                      X",
	"XXXXXXXXXXXXXXXXXXXXXXXX"
]

nivelTres = [
	"XXXXXXXXXXXXXXXXXXXXXXXXX",
	"XP                      X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                      MX",
	"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

nivelCuatro = [
	"XXXXXXXXXXXXXXXXXXXXXXXXX",
	"XP                      X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X     X XXXXX           X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X            XXXXX      X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X               XXX     X",
	"X                       X",
	"X   M                   X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"X                       X",
	"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

niveles = [nivelUno, nivelDos, nivelUno, nivelDos]

#--------------------------------------------------SetUp----------------------------------------------------------------

bloques = Bloques()
jugador = Jugador()
meta = Meta()

#-------------------------------------------------Movimiento------------------------------------------------------------

turtle.listen()
turtle.onkey(jugador.subir, "Up")
turtle.onkey(jugador.bajar, "Down")
turtle.onkey(jugador.izquierda, "Left")
turtle.onkey(jugador.derecha, "Right")

#------------------------------------------------CreacionDeMapa---------------------------------------------------------

def crearLaberinto(nivel):
	muros.clear()
	goal.clear()

	for fila in range(len(nivel)):
		for columna in range(len(nivel[fila])):

			caracter = nivel[fila][columna]
			ejeX = -288 + (columna * 24)
			ejeY = 288 - (fila * 24)

			if caracter == 'X':
				bloques.goto(ejeX, ejeY)
				bloques.stamp()
				muros.append((ejeX, ejeY))
			elif caracter == 'P':
				jugador.goto(ejeX, ejeY)
			elif caracter == 'M':
				meta.goto(ejeX, ejeY)
				goal.append((ejeX, ejeY))

muros = []
goal = []

#--------------------------------------------------CambioNivel----------------------------------------------------------

def cambiarNivel():
	try:
		bloques.clear()
		crearLaberinto(niveles[contador])
		#moverseEnLaberinto()
	except IndexError:
		print("Fin del juego")
		exit()

cambiarNivel()
ventana.mainloop()


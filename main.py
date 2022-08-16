import turtle
import random

# Modifying the window name and color
turtle.title("Sierpinski Triangle")
turtle.screensize(canvwidth=400, canvheight=400, bg="black")

s = turtle.getscreen()	# Create and open the turtle screen

t = turtle.Turtle()		# Asign the turtle to the variable t

# Personalizing the turtle
t.fillcolor("white")
t.pencolor("white")
t.shapesize(1,1,1)
t.speed(50)

# Drawing the triangle apices

a = (0,150)
b = (-150, -150)
c = (150, -150)

t.penup()
t.goto(a)
t.pendown()
t.dot(1)

t.penup()
t.goto(b)
t.pendown()
t.dot(1)

t.penup()
t.goto(c)
t.pendown()
t.dot(1)

# Drawing the first random point within the triangle
t.penup()

y = random.randint(-150, 150) # y coordinate between the base and the top of the triangle

x_left_limit = int((y - 150) / 2)			# The line that connect the top and left apices is: y = 2x + 150
x_right_limit =  int((y - 150) / -2)		# The line that connect the top and right apices is: y = -2x + 150

x = random.randint(x_left_limit, x_right_limit)	# x coordinate between calculated limits

last_point = (x, y)

t.goto(last_point)
t.pendown()
t.dot(1)
t.penup()

for i in range(5000):

	# Choosing one of the 3 starting points

	chooser = random.randint(1, 3)

	if chooser == 1:
		chosen = a
	elif chooser == 2:
		chosen = b
	else:
		chosen = c


	# Calculating midpoint between chosen and last_point		[ M = ((x1 + x2) / 2), (y1 + y2) / 2) ]

	midpoint = ( (chosen[0] + last_point[0]) / 2 , (chosen[1] + last_point[1]) / 2 )

	t.goto(midpoint)
	t.pendown()
	t.dot(1)
	t.penup()

	last_point = midpoint	# Asign the new point as the last_point
	

t.goto(400, 400)	# Move the turtle outside of the triangle


turtle.done()	#Keep the window from closing. If you delete this line the screen will close as soon as it finish
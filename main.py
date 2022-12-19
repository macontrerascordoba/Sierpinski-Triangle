import turtle
import random
import time
import os


##################################
#								 #
#			User Inputs	 		 #			More input value checks to be added to the while loops
#								 #
##################################

points = 5000
speed = 0

os.system('cls' if os.name == 'nt' else 'clear')

# Choosing number of dots

points = input("How many dots do you want me to draw: (Min = 1, Default = 5000)  ->  ")

while True:	

	if points == "":
			points = 5000
			break

	try:
		points = int(points)
	except:
		points = input("\nIt has to be a number. Please try again:  ->  ")
	else:
		if points < 1:
			points = 1
		break

print("\nPerfect, I'm going to draw ", points, " points\n\n")


# Choosing speed

speed = input("At what speed do you me want to move: (1 - Slowest, 10 - Fastest, 0 (default) - Almost Instant Movement)  ->  ")

while True:

	if speed == "":
		speed = 0
		break

	try:
		speed = int(speed)
	except:
		speed = input("\nIt has to be a number. Please try again:  ->  ")
	else:
		if speed < 0 or speed > 10:
			speed = 0
		break

if speed == 0:
	print("\nOk, I'll go as fast as I can")
else:
	print("\nAwesome, I'm going to change my speed to ", speed, " units")


print("\n\nEverything set, I will start now")

time.sleep(3)


##############################################################################################################################


# Modifying the window name and color
turtle.title("Sierpinski Triangle")
turtle.screensize(canvwidth=400, canvheight=400, bg="black")

s = turtle.getscreen()	# Create and open the turtle screen

t = turtle.Turtle()		# Asign the turtle to the variable t

# Personalizing the turtle
t.color("white", "white")
t.shapesize(1,1,1)
t.speed(speed)


# Drawing the triangle apices

a = (0,150)
b = (-150, -150)
c = (150, -150)

t.penup()
t.goto(a)
t.pendown()
t.dot(2)

t.penup()
t.goto(b)
t.pendown()
t.dot(2)

t.penup()
t.goto(c)
t.pendown()
t.dot(2)

# Drawing the first random point within the triangle
t.penup()

y = random.randint(-150, 150) # y coordinate between the base and the top of the triangle

# x_left_limit = int((y - 150) / 2)			# The line that connect the top and left apices is: y = 2x + 150
# x_right_limit =  int((y - 150) / -2)		# The line that connect the top and right apices is: y = -2x + 150

# x = random.randint(x_left_limit, x_right_limit)	# x coordinate between calculated limits

side = random.randint(0, 1)	# Left side and right side respectively

if side == 0:
	x = (y - 150) / 2
else:
	x = (y - 150) / -2

last_point = (x, y)

t.goto(last_point)
t.pendown()
t.dot(2)
t.penup()

for i in range(points):

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
	t.dot(2)
	t.penup()

	last_point = midpoint	# Asign the new point as the last_point
	
t.goto(a)
t.pendown()
t.goto(b)
t.goto(c)
t.goto(a)
t.penup()

t.goto(400, 400)	# Move the turtle outside of the triangle

turtle.done()	#Keep the window from closing. If you delete this line the screen will close as soon as it finish

os.system('cls' if os.name == 'nt' else 'clear')
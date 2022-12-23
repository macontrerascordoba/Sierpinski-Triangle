import turtle, random, time

class Painter():
    
    def __init__(self, dots, speed):
        self.dots = dots
        self.speed = speed


    def start(self):

        colors = {
                'bg' : '#201a1a',
                'turtle' : '#dbd2d2'
            }

        # Modifying the window name and color
        turtle.title("Sierpinski Triangle")
        turtle.screensize(canvwidth=400, canvheight=400, bg=colors['bg'])

        s = turtle.Screen()	# Create and open the turtle screen

        t = turtle.Turtle()		# Asign the turtle to the variable t

        # Personalizing the turtle
        t.color(colors['turtle'], colors['turtle'])
        t.shapesize(1,1,1)
        t.speed(self.speed)
        t.penup()

        
        # Drawing the triangle apices

        apices = [(0,150), (-150, -150), (150, -150)]

        for apex in apices:
            t.goto(apex)
            t.dot(2)

        # Drawing the first random point
        
        apex = apices[0]
        i = random.randint(1, 2)

        last_point = ((apex[0] + apices[i][0])/2, (apex[1] + apices[i][1])/2)

        t.goto(last_point)
        t.dot(2)

        for i in range(self.dots):

            # Choosing one of the 3 starting points

            apex = random.choice(apices)

            # Calculating midpoint between chosen and last_point		[ M = ((x1 + x2) / 2), (y1 + y2) / 2) ]

            midpoint = ( (apex[0] + last_point[0]) / 2 , (apex[1] + last_point[1]) / 2 )

            t.goto(midpoint)
            t.dot(2)

            last_point = midpoint	# Asign the new point as the last_point
            
        t.goto(apices[-1])
        t.pendown()
        for apex in apices:
            t.goto(apex)
        t.penup()

        t.goto(400, 400)	# Move the turtle outside of the triangle

        turtle.done()	#Keep the window from closing. If you delete this line the screen will close as soon as it finish
import tkinter as tk
import Painter as ptr

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        # GENERAL VARIABLES
        colors = {
            'bg' : '#201a1a',
            'sbt' : '#ffb1c8',
            'sbttxt' : '#581a31',
            'qbt' : '#673d0d',
            'qbttxt' : '#ffdcbe',
            'num' : '#ece0e0',
            'title' : '#dbd2d2',
            'error' : '#Ff0005'
        }

        self.errors = {
            'dotsNum' : True,
            'speedNum' : True,
            'dotsRanged' : True,
            'speedNum' : True
        }


        # MAIN WINDOW CONFIGURATION
        self.title("Sierpinski Triangle")
        self.geometry("400x400")
        self.resizable(False, False)
        self.config(background=colors['bg'])
        

        # TITLE LABEL
        tk.Label(self, text='Sierpinski Triangle', font=('Consolas bold', 22),
                    bg=colors['bg'], fg=colors['title']).place(x=50, y=30)


        # FIRST INPUT
        tk.Label(self, text='Number of dots: (Min = 1)', font=('Consolas bold', 14),
                    bg=colors['bg'], fg=colors['title']).place(x=20, y=100)
        tk.Label(self, text='Your input: ', font=('Consolas', 14),
                    bg=colors['bg'], fg=colors['title']).place(x=20, y=130)
        self.firstInput = tk.StringVar()
        tk.Entry(self, textvariable=self.firstInput, width=11,font=('OCR A Extended', 14),
                    bg=colors['title'], fg=colors['bg']).place(x=140, y=130)
        self.firstInput.set(5000)

        self.error1 = tk.StringVar()
        tk.Label(self, textvariable=self.error1, font=('Console bold', 12),
                    bg=colors['bg'], fg=colors['error']).place(x=275, y=130)

        

        #SECOND INPUT
        tk.Label(self, text='Speed: (1 - Slowest, 11 - Fastest)', font=('Consolas bold', 14),
                    bg=colors['bg'], fg=colors['title']).place(x=20, y=170)
        tk.Label(self, text='Your input: ', font=('Consolas', 14),
                    bg=colors['bg'], fg=colors['title']).place(x=20, y=200)
        self.secondInput = tk.StringVar()
        tk.Entry(self, textvariable=self.secondInput, width=11, font=('OCR A Extended', 14),
                    bg=colors['title'], fg=colors['bg']).place(x=140, y=200)
        self.secondInput.set(11)

        self.error2 = tk.StringVar()
        tk.Label(self, textvariable=self.error2, font=('Console bold', 12),
                    bg=colors['bg'], fg=colors['error']).place(x=275, y=200)


        # NOTe
        tk.Label(self, text='Note: at max speed it draws \naproximately 5 points per second', font=('Consolas bold', 10),
                    bg=colors['bg'], fg=colors['error']).place(x=80, y=227)


        #BUTTONS
        tk.Button(self, text='START', width=9, font=('Consolas bold', 14),
                    bg=colors['sbt'], fg=colors['sbttxt'], command=self.start).place(x=155, y=270)
        tk.Button(self, text='QUIT', width=7, font=('Consolas bold', 14),
                    bg=colors['qbt'], fg=colors['qbttxt'], command=quit).place(x=164, y=320)

    
    def start(self):
        dots = speed = 0
        self.error1.set('')
        self.error2.set('')
        error1 = error2 = False

        try:
            dots = int(self.firstInput.get())
        except:
            self.error1.set('Invalid Number')
            error1 = True
        
        try:
            speed = int(self.secondInput.get())
        except:
            self.error2.set('Invalid Number')
            error2 = True


        if not error1 and dots < 1:
            self.error1.set('Out of Range')
            error1 = True
            
        if not error2 and (speed < 1 or speed > 11):
            self.error1.set('Out of Range')
            error2 = True


        valid = True
        if error1 or error2:
            valid = False

        if valid:
            
            self.destroy()
            painter = ptr.Painter(dots, speed)
            
            try:
                painter.start()
            except:
                quit()


            
        
from tkinter import *
from board import *
import math as m
import tkinter.font as tkFont

class View:
    def reveal_surrounding(self, x, y, num):
        
        self.canvas.create_text(x, y, text=str(num), font=self.fontStyle, fill='red')
        
            

    def select_square(self,event):
        x = m.floor((event.x /self.scale +  1)) 
        y = m.floor((event.y /self.scale +  1))
        if(self.board.is_mine(x-1,y-1)):
            exit()
        
        x_scale_up = x *self.scale - self.scale/2
        y_scale_up = y *self.scale - self.scale/2
        #self.canvas.create_text(x_scale_up, y_scale_up, text="X", font=self.fontStyle, fill='red')
        self.reveal_surrounding(x_scale_up, y_scale_up,self.board.count_surrounding(x-1,y-1))
        if(self.board.count_surrounding(x-1, y-1) == 0):
            print("TRUE")
            for i in range(3):
                for j in range(3):
                    if((i-1 == 0 and j-1 == 0) or (x-1+(i-1) >= self.game_width) or (y-1+(j-1) >= self.game_height) or (x-1+(i-1) < 0) or (y-1+(j-1) < 0)):
                        continue
                    else:
                        self.reveal_surrounding(x_scale_up +((i-1) * self.scale),y_scale_up + ((j-1) * self.scale), self.board.count_surrounding(x-1 + i-1, y-1 + j-1))

    def flag_square(self, event):
        x = m.floor((event.x /self.scale +  1)) 
        y = m.floor((event.y /self.scale +  1))
        x_scale_up = x *self.scale - self.scale/2
        y_scale_up = y *self.scale - self.scale/2
        
        self.canvas.create_text(x_scale_up, y_scale_up, text="F", font=self.fontStyle, fill='red')

    def __init__(self, h, w):
        self.top = Tk()
        self.scale = 100
        self.game_height, self.game_width = h, w
        self.board =  Board(self.game_height, self.game_width, 18)
        self.canvas = Canvas(self.top, bg="white", width = self.game_width*self.scale, height = self.game_height*self.scale)
        self.draw_board()
        self.canvas.bind('<Button-1>',self.select_square, add=True)
        self.canvas.bind('<Button-3>',self.flag_square, add=True)
        self.board.show_mine_loc()
        self.fontStyle = tkFont.Font(family="Lucida Grande", size=50)

    def draw_board(self):
        coord = [0, 0, self.scale, self.scale]
        coord2 = [self.scale, self.scale, self.scale*2, self.scale*2]
        space = self.scale*2
        for i in range (self.game_width):
    
            for j in range (self.game_width):
        
                self.canvas.create_rectangle(coord, fill='grey', outline='grey')
                coord[0] = coord[0] + space
                coord[2] = coord[2] + space
            coord[0] = 0
            coord[2] = self.scale
            coord[1] = coord[1] + space
            coord[3] = coord[3] + space
        
        
        for i in range (self.game_height-1):
    
            for j in range (self.game_height-1):
        
                self.canvas.create_rectangle(coord2, fill='grey', outline='grey')
                coord2[0] = coord2[0] + space
                coord2[2] = coord2[2] + space
            coord2[0] = self.scale
            coord2[2] = self.scale*2
            coord2[1] = coord2[1] + space
            coord2[3] = coord2[3] + space
        
        
        self.canvas.pack()

    def view_loop(self):      
        
        self.canvas.pack()
        self.top.mainloop()



v = View(10,10)
v.view_loop()
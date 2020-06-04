# ex 9.6
from tkinter import *
from random import randint
import tkinter.messagebox
class Tic_Tac_Toe:
    def __init__(self):
        window = Tk()
        window.title("Tic Tac Toe")

        self.canvas = Canvas(window, bg = "white", width = 240, height = 240)
        self.canvas.pack()

        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]
        self.list_of_coordinates = []
        self.list_of_coordinates_for_computer = []

        self.canvas.create_line(0, 80, 240, 80, fill = "blue")
        self.canvas.create_line(0, 160, 240, 160, fill = "blue")
        self.canvas.create_line(80, 0, 80, 240, fill = "blue")
        self.canvas.create_line(160, 0, 160, 240, fill = "blue")

        self.crossImage = PhotoImage(file = "C:\\Users\\Home\\PycharmProjects\\Tutorial\\pybook\\image\\x.gif")
        self.circleImage = PhotoImage(file = "C:\\Users\\Home\\PycharmProjects\\Tutorial\\pybook\\image\\o.gif")
        self.circleImage = self.circleImage.zoom(2)
        self.crossImage = self.crossImage.zoom(2)
        #self.circleImage = self.circleImage.zoom(20)
        #self.circleImage = self.circleImage.subsample(10)

        self.count_each_time_for_player = 0
        self.count_each_time_for_computer = 0
        self.count_step_for_computer = 0
        self.canvas.bind("<Button-1>", self.processMouseEvent)
        #self.First_move()

        window.mainloop()

    def quit_window(self):
        quit()

    def Messagebox_win(self):
        self.isOK = tkinter.messagebox.askokcancel("You win!", "Restart?")
        if self.isOK == True:
            self.canvas.delete("line", "image")
            self.board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
            self.list_of_coordinates = []
            self.list_of_coordinates_for_computer = []
            self.count_each_time_for_player = 0
            self.count_each_time_for_computer = 0
            #self.count_step_for_computer = 0
            #self.First_move()
            #self.canvas.bind("<Button-1>", self.processMouseEvent)
        else:
            self.quit_window()

    def Messagebox_draw(self):
        self.isOK = tkinter.messagebox.askokcancel("Draw!", "Restart?")
        if self.isOK == True:
            self.canvas.delete("line", "image")
            self.board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
            self.list_of_coordinates = []
            self.list_of_coordinates_for_computer = []
            self.count_each_time_for_player = 0
            self.count_each_time_for_computer = 0
            #self.count_step_for_computer = 0
            #self.First_move()
            #self.canvas.bind("<Button-1>", self.processMouseEvent)
        else:
            self.quit_window()

    def Messagebox_loss(self):
        self.isOK = tkinter.messagebox.askokcancel("You lose!", "Restart?")
        if self.isOK == True:
            self.canvas.delete("line", "image")
            self.board = [0, 0, 0,
                          0, 0, 0,
                          0, 0, 0]
            self.list_of_coordinates = []
            self.list_of_coordinates_for_computer = []
            self.count_each_time_for_player = 0
            self.count_each_time_for_computer = 0
            #self.count_step_for_computer = 0
            #self.First_move()
            #self.canvas.bind("<Button-1>", self.processMouseEvent)
        else:
            self.quit_window()



    def processMouseEvent(self, event):
        print(event.x, event.y)
        while self.count_each_time_for_player < 5:
            if event.x < 80 and event.y < 80:
                if self.board[0] == 0:
                    self.canvas.create_image(40, 40, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[0] = 1
                    self.list_of_coordinates.append((40, 40))
                else:
                    break
            elif 80 <= event.x < 160 and event.y < 80:
                if self.board[1] == 0:
                    self.canvas.create_image(120, 40, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[1] = 1
                    self.list_of_coordinates.append((120, 40))
                else:
                    break
            elif event.x >= 160 and event.y < 80:
                if self.board[2] == 0:
                    self.canvas.create_image(200, 40, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[2] = 1
                    self.list_of_coordinates.append((200, 40))
                else:
                    break
            elif event.x < 80 and 80 <= event.y < 160:
                if self.board[3] == 0:
                    self.canvas.create_image(40, 120, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[3] = 1
                    self.list_of_coordinates.append((40, 120))
                else:
                    break
            elif 80 <= event.x < 160 and 80 <= event.y < 160:
                if self.board[4] == 0:
                    self.canvas.create_image(120, 120, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[4] = 1
                    self.list_of_coordinates.append((120, 120))
                else:
                    break
            elif event.x >= 160 and 80 <= event.y < 160:
                if self.board[5] == 0:
                    self.canvas.create_image(200, 120, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[5] = 1
                    self.list_of_coordinates.append((200, 120))
                else:
                    break
            elif event.x < 80 and event.y >= 160:
                if self.board[6] == 0:
                    self.canvas.create_image(40, 200, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[6] = 1
                    self.list_of_coordinates.append((40, 200))
                else:
                    break
            elif 80 <= event.x < 160 and event.y >= 160:
                if self.board[7] == 0:
                    self.canvas.create_image(120, 200, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[7] = 1
                    self.list_of_coordinates.append((120, 200))
                else:
                    break
            elif event.x >= 160 and event.y >= 160:
                if self.board[8] == 0:
                    self.canvas.create_image(200, 200, anchor=CENTER, image=self.crossImage, tag="image")
                    self.board[8] = 1
                    self.list_of_coordinates.append((200, 200))
                else:
                    break
            self.mechanism(self.list_of_coordinates)
            print(self.count_each_time_for_player)
            print(self.board)
            print(self.list_of_coordinates)
            if self.player_wins == True:
                self.computer_wins = False
                self.Messagebox_win()
                break
            #elif self.isFirst_move == False and self.player_wins == True:
            #    self.computer_wins = False
            #    self.Messagebox_win()
            #    break
            elif self.count_each_time_for_player == 4:
                self.player_wins = False
                self.computer_wins = False
                self.Messagebox_draw()
                break
            else:
                self.count_each_time_for_player += 1
                self.count_each_time_for_computer = 0
                self.computersTurn(self.board)
                if self.computer_wins == True:
                    self.player_wins = False
                    self.Messagebox_loss()
                    #self.computersTurn(self.board)
                    #self.count_each_time_for_computer = 0
                    break
            print(self.list_of_coordinates_for_computer)


    def computersTurn(self, board):
        while self.count_each_time_for_computer < 1:
            computer_x = randint(0, 240)
            computer_y = randint(0, 240)
            if computer_x < 80 and computer_y < 80:
                if board[0] == 0:
                    self.canvas.create_image(40, 40, anchor=CENTER, image=self.circleImage, tag="image")
                    board[0] = 2
                    self.list_of_coordinates_for_computer.append((40, 40))
                else:
                    continue
            elif 80 <= computer_x < 160 and computer_y < 80:
                if board[1] == 0:
                    self.canvas.create_image(120, 40, anchor=CENTER, image=self.circleImage, tag="image")
                    board[1] = 2
                    self.list_of_coordinates_for_computer.append((120, 40))
                else:
                    continue
            elif computer_x >= 160 and computer_y < 80:
                if board[2] == 0:
                    self.canvas.create_image(200, 40, anchor=CENTER, image=self.circleImage, tag="image")
                    board[2] = 2
                    self.list_of_coordinates_for_computer.append((200, 40))
                else:
                    continue
            elif computer_x < 80 and 80 <= computer_y < 160:
                if board[3] == 0:
                    self.canvas.create_image(40, 120, anchor=CENTER, image=self.circleImage, tag="image")
                    board[3] = 2
                    self.list_of_coordinates_for_computer.append((40, 120))
                else:
                    continue
            elif 80 <= computer_x < 160 and 80 <= computer_y < 160:
                if board[4] == 0:
                    self.canvas.create_image(120, 120, anchor=CENTER, image=self.circleImage, tag="image")
                    board[4] = 2
                    self.list_of_coordinates_for_computer.append((120, 120))
                else:
                    continue
            elif computer_x >= 160 and 80 <= computer_y < 160:
                if board[5] == 0:
                    self.canvas.create_image(200, 120, anchor=CENTER, image=self.circleImage, tag="image")
                    board[5] = 2
                    self.list_of_coordinates_for_computer.append((200, 120))
                else:
                    continue
            elif computer_x < 80 and computer_y >= 160:
                if board[6] == 0:
                    self.canvas.create_image(40, 200, anchor=CENTER, image=self.circleImage, tag="image")
                    board[6] = 2
                    self.list_of_coordinates_for_computer.append((40, 200))
                else:
                    continue
            elif 80 <= computer_x < 160 and computer_y >= 160:
                if board[7] == 0:
                    self.canvas.create_image(120, 200, anchor=CENTER, image=self.circleImage, tag="image")
                    board[7] = 2
                    self.list_of_coordinates_for_computer.append((120, 200))
                else:
                    continue
            elif computer_x >= 160 and computer_y >= 160:
                if board[8] == 0:
                    self.canvas.create_image(200, 200, anchor=CENTER, image=self.circleImage, tag="image")
                    board[8] = 2
                    self.list_of_coordinates_for_computer.append((200, 200))
                else:
                    continue
            self.mechanism_for_computer(self.list_of_coordinates_for_computer)
            #print(self.count_step_for_computer)
            #self.count_step_for_computer += 1
            #if self.isFirst_move == False and self.count_step_for_computer == 5:
            #    self.player_wins = False
            #    self.computer_wins = False
            #    self.Messagebox_draw()
            #    break
            self.count_each_time_for_computer += 1

    def mechanism(self, list_of_coordinates):
        self.player_wins = False
        count = 0
        count2 = 1
        if len(list_of_coordinates) >= 3:
            for i in range(len(list_of_coordinates)):
                while count < len(list_of_coordinates):
                    if list_of_coordinates[i] == list_of_coordinates[i - count]:
                        count += 1
                        continue
                    else:
                        while count2 < (len(list_of_coordinates) + 1):
                            if list_of_coordinates[i - count] == list_of_coordinates[i - count2] \
                                    or list_of_coordinates[i] == list_of_coordinates[i - count2]:
                                count2 += 1
                                continue
                            else:
                                x1 = float(list_of_coordinates[i][0])
                                y1 = float(list_of_coordinates[i][1])
                                x2 = float(list_of_coordinates[i - count][0])
                                y2 = float(list_of_coordinates[i - count][1])
                                x3 = float(list_of_coordinates[i - count2][0])
                                y3 = float(list_of_coordinates[i - count2][1])
                                try:
                                    slope_a = (y2 - y1) / (x2 - x1)
                                except ZeroDivisionError:
                                    slope_a = 100
                                try:
                                    slope_b = (y3 - y2) / (x3 - x2)
                                except ZeroDivisionError:
                                    slope_b = 100
                                if slope_a == slope_b:
                                    self.player_wins = True
                                    self.canvas.create_line(x1, y1, x2, y2, x3, y3, fill = "green", width = 10, tags="line")
                                    return self.player_wins
                                count2 += 1
                        count2 = 0
                    count += 1
                count = 0

    def mechanism_for_computer(self, list_of_coordinates):
        self.computer_wins = False
        count = 0
        count2 = 1
        if len(list_of_coordinates) >= 3:
            for i in range(len(list_of_coordinates)):
                while count < len(list_of_coordinates):
                    if list_of_coordinates[i] == list_of_coordinates[i - count]:
                        count += 1
                        continue
                    else:
                        while count2 < (len(list_of_coordinates) + 1):
                            if list_of_coordinates[i - count] == list_of_coordinates[i - count2] \
                                    or list_of_coordinates[i] == list_of_coordinates[i - count2]:
                                count2 += 1
                                continue
                            else:
                                x1 = float(list_of_coordinates[i][0])
                                y1 = float(list_of_coordinates[i][1])
                                x2 = float(list_of_coordinates[i - count][0])
                                y2 = float(list_of_coordinates[i - count][1])
                                x3 = float(list_of_coordinates[i - count2][0])
                                y3 = float(list_of_coordinates[i - count2][1])
                                try:
                                    slope_a = (y2 - y1) / (x2 - x1)
                                except ZeroDivisionError:
                                    slope_a = 100
                                try:
                                    slope_b = (y3 - y2) / (x3 - x2)
                                except ZeroDivisionError:
                                    slope_b = 100
                                if slope_a == slope_b:
                                    self.computer_wins = True
                                    self.canvas.create_line(x1, y1, x2, y2, x3, y3, fill="green", width=10, tags="line")
                                    return self.computer_wins
                                count2 += 1
                        count2 = 0
                    count += 1
                count = 0

                    #if self.player_wins == 4:
                    #    print("Draw!")
                    #print(count_num)
                        #return self.player_wins
                    #print(count_num)

        '''
        while self.count_press < 10:
            self.click = self.canvas.bind("<Button-1>", self.processMouseEvent)
            self.response = self.computersTurn(self.board)
            self.count_each_time_for_player = 0
            self.count_each_time_for_computer = 0
            self.count_press += 1

        self.canvas.focus_set()
        '''
        #print(self.count_each_time_for_player)
        #print(self.count_each_time_for_computer)



        #self.computersTurn(self.board)
Tic_Tac_Toe()

'''
    def First_move(self):
        self.isFirst_move = tkinter.messagebox.askokcancel("First move?", "Player first?")
        if self.isFirst_move == True:
            print("hihi")
            self.canvas.bind("<Button-1>", self.processMouseEvent)
        else:
            print("hibye")
            self.computersTurn(self.board)
            self.count_each_time_for_computer = 0
            self.canvas.bind("<Button-1>", self.processMouseEvent)
'''

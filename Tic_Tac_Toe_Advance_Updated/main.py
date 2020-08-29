from tkinter import *
from random import randint
import tkinter.messagebox
import math
from collections import deque
import os
import sys
class Tic_Tac_Toe:
    def __init__(self):
        self.window = Tk()
        self.window.title("Tic Tac Toe")

        self.canvas = Canvas(self.window, bg = "white", width = 240, height = 240)
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

        self.crossImage = PhotoImage(file = "C:\\Users\\Home\\PycharmProjects\\Tutorial\\GUI\\Tic_Tac_Toe_Advance\\cross.gif")
        self.circleImage = PhotoImage(file = "C:\\Users\\Home\\PycharmProjects\\Tutorial\\GUI\\Tic_Tac_Toe_Advance\\circle.gif")
        self.crossImage = PhotoImage(file = os.getcwd() + "\\cross.gif")
        self.circleImage = PhotoImage(file = os.getcwd() + "\\circle.gif")
        self.circleImage = self.circleImage.zoom(2)
        self.crossImage = self.crossImage.zoom(2)
        #self.circleImage = self.circleImage.zoom(20)
        #self.circleImage = self.circleImage.subsample(10)

        self.count_each_time_for_player = 0
        self.count_each_time_for_computer = 0
        self.count_step_for_computer = 0
        self.alert_player_ready_to_win = False
        self.notification_of_next_step = False
        self.notification_of_next_step_to_win = False
        #self.canvas.bind("<Button-1>", self.processMouseEvent)
        self.First_move()

        self.window.mainloop()

    def quit_window(self):
        self.window.destroy()


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
            self.count_step_for_computer = 0
            self.First_move()
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
            self.count_step_for_computer = 0
            self.First_move()
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
            self.count_step_for_computer = 0
            self.First_move()
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
            print(self.board)
            print(self.list_of_coordinates)
            if self.isFirst_move == True:
                if self.player_wins == True:
                    self.computer_wins = False
                    self.Messagebox_win()
                    break
                elif self.count_each_time_for_player == 4:
                    self.player_wins = False
                    self.computer_wins = False
                    self.Messagebox_draw()
                    break
                else:
                    print(self.count_each_time_for_player)
                    self.count_each_time_for_player += 1
                    self.count_each_time_for_computer = 0
                    self.computersTurn(self.board)
                    if self.computer_wins == True:
                        self.player_wins = False
                        self.Messagebox_loss()
                        break
            else:
                if self.player_wins == True:
                    self.computer_wins = False
                    self.Messagebox_win()
                    break
                else:
                    #self.count_each_time_for_player += 1
                    print(self.count_step_for_computer)
                    self.count_each_time_for_computer = 0
                    self.computersTurn(self.board)
                    self.count_step_for_computer += 1
                    if self.computer_wins == True:
                        self.player_wins = False
                        self.Messagebox_loss()
                        break
                    elif self.count_step_for_computer == 4:
                        self.player_wins = False
                        self.computer_wins = False
                        self.Messagebox_draw()
                        break
            print(self.list_of_coordinates_for_computer)

    def computersTurn(self, board):
        computer_x = 0
        computer_y = 0
        while self.count_each_time_for_computer < 1:
            self.computer_blocking_mechanism(self.list_of_coordinates, self.board)
            print("self.alert_player_ready_to_win is " + str(self.alert_player_ready_to_win))
            self.expansion_mechanism_for_computer(self.list_of_coordinates_for_computer, self.board)
            print("self.notification_of_next_step is " + str(self.notification_of_next_step))
            print("self.notification_of_next_step_to_win is " + str(self.notification_of_next_step_to_win))
            if self.alert_player_ready_to_win == False and self.notification_of_next_step_to_win == True:
                computer_x = self.x_for_next_step
                computer_y = self.y_for_next_step
                print("will win")
            elif self.alert_player_ready_to_win == True and self.notification_of_next_step_to_win == True:
                computer_x = self.x_for_next_step
                computer_y = self.y_for_next_step
                print("should win but not block")
            elif self.alert_player_ready_to_win == True and self.notification_of_next_step == True:
                computer_x = self.x3_for_player_expected
                computer_y = self.y3_for_player_expected
                print("should block")
            elif self.alert_player_ready_to_win == True and self.notification_of_next_step == False:
                computer_x = self.x3_for_player_expected
                computer_y = self.y3_for_player_expected
                print("block")
            elif self.alert_player_ready_to_win == False and self.notification_of_next_step == True:
                computer_x = self.x_for_next_step
                computer_y = self.y_for_next_step
                print("expand")
            elif self.notification_of_next_step == False and self.notification_of_next_step == False:
                computer_x = randint(0, 240)
                computer_y = randint(0, 240)
                print("random")
            print(computer_x, computer_y)
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
            self.alert_player_ready_to_win = False
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

    def computer_blocking_mechanism(self, list_of_coordinates_for_player, board):
        self.alert_player_ready_to_win = False
        count_for_player = 0
        self.x3_for_player_expected = 0
        self.y3_for_player_expected = 0
        if len(list_of_coordinates_for_player) >= 2:
            for i in range(len(list_of_coordinates_for_player)):
                while count_for_player < len(list_of_coordinates_for_player):
                    if list_of_coordinates_for_player[i] == list_of_coordinates_for_player[i - count_for_player]:
                        count_for_player += 1
                        continue
                    else:
                        self.x1_for_player = float(list_of_coordinates_for_player[i][0])
                        self.y1_for_player = float(list_of_coordinates_for_player[i][1])
                        self.x2_for_player = float(list_of_coordinates_for_player[i - count_for_player][0])
                        self.y2_for_player = float(list_of_coordinates_for_player[i - count_for_player][1])
                        try:
                            slope_a_for_player = (self.y2_for_player - self.y1_for_player) / (self.x2_for_player - self.x1_for_player)
                        except ZeroDivisionError:
                            slope_a_for_player = 100
                        distance_of_two_points = math.sqrt((self.x2_for_player - self.x1_for_player) ** 2 + (self.y2_for_player - self.y1_for_player) ** 2)
                        if slope_a_for_player == 0:
                            if distance_of_two_points == 80:
                                if self.x1_for_player == 40 or self.x2_for_player == 40:
                                    self.x3_for_player_expected = 200
                                elif self.x1_for_player == 200 or self.x2_for_player == 200:
                                    self.x3_for_player_expected = 40
                            elif distance_of_two_points == 160 and self.x1_for_player == 40 or self.x2_for_player == 40:
                                self.x3_for_player_expected = 120
                            self.y3_for_player_expected = self.y2_for_player
                        elif slope_a_for_player == 100:
                            if distance_of_two_points == 80:
                                if self.y1_for_player == 40 or self.y2_for_player == 40:
                                    self.y3_for_player_expected = 200
                                elif self.y1_for_player == 200 or self.y2_for_player == 200:
                                    self.y3_for_player_expected = 40
                            elif distance_of_two_points == 160 and self.y1_for_player == 40 or self.y2_for_player == 40:
                                self.y3_for_player_expected = 120
                            self.x3_for_player_expected = self.x2_for_player
                        elif slope_a_for_player == 1:
                            if math.floor(distance_of_two_points) == 113:
                                if (self.x1_for_player, self.y1_for_player) == (40, 40) or (self.x2_for_player, self.y2_for_player) == (40, 40):
                                    (self.x3_for_player_expected, self.y3_for_player_expected) = (200, 200)
                                elif (self.x1_for_player, self.y1_for_player) == (200, 200) or (self.x2_for_player, self.y2_for_player) == (200, 200):
                                    (self.x3_for_player_expected, self.y3_for_player_expected) = (40, 40)
                            elif math.floor(distance_of_two_points) == 226:
                                (self.x3_for_player_expected, self.y3_for_player_expected) = (120, 120)
                        elif slope_a_for_player == -1:
                            if math.floor(distance_of_two_points) == 113:
                                if (self.x1_for_player, self.y1_for_player) == (200, 40) or (self.x2_for_player, self.y2_for_player) == (200, 40):
                                    (self.x3_for_player_expected, self.y3_for_player_expected) = (40, 200)
                                elif (self.x1_for_player, self.y1_for_player) == (40, 200) or (self.x2_for_player, self.y2_for_player) == (40, 200):
                                    (self.x3_for_player_expected, self.y3_for_player_expected) = (200, 40)
                            elif math.floor(distance_of_two_points) == 226:
                                (self.x3_for_player_expected, self.y3_for_player_expected) = (120, 120)
                        else:
                            self.alert_player_ready_to_win = False
                            count_for_player += 1
                            continue

                        if self.x3_for_player_expected != 0 and self.y3_for_player_expected != 0:
                            if (self.x3_for_player_expected, self.y3_for_player_expected) == (40, 40) and board[0] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (120, 40) and board[1] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (200, 40) and board[2] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (40, 120) and board[3] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (120, 120) and board[4] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (200, 120) and board[5] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (40, 200) and board[6] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (120, 200) and board[7] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif (self.x3_for_player_expected, self.y3_for_player_expected) == (200, 200) and board[8] != 0:
                                self.alert_player_ready_to_win = False
                                count_for_player += 1
                                continue
                            elif 0 not in board:
                                self.alert_player_ready_to_win = False
                                return self.alert_player_ready_to_win
                            else:
                                self.alert_player_ready_to_win = True
                                #print((self.x3_for_player_expected, self.y3_for_player_expected))
                                #print(self.x1_for_player, self.y1_for_player, self.x2_for_player, self.y2_for_player, self.x3_for_player_expected, self.y3_for_player_expected)
                                return self.alert_player_ready_to_win
                        else:
                            self.alert_player_ready_to_win = False
                            count_for_player += 1
                            continue

                count_for_player = 0

    def expansion_mechanism_for_computer(self, list_of_coordinates_for_computer, board):
        board_coordinates = [(40, 40), (120, 40), (200, 40),
                             (40, 120), (120, 120), (200, 120),
                             (40, 200), (120, 200), (200, 200)]
        possible_coordinates = deque()
        self.x_for_next_step = 0
        self.y_for_next_step = 0
        self.notification_of_next_step = False
        self.notification_of_next_step_to_win = False
        count = 0
        count2 = 0
        count_for_occupied_grid = 0
        first_coordinate_occupied = False
        second_coordinate_occupied = False
        third_coordinate_occupied = False
        if len(list_of_coordinates_for_computer) > 0:
            for i in range(len(board_coordinates)):
                if board[i] == 0:
                    possible_coordinates.appendleft(board_coordinates[i])

            for i in range(len(board_coordinates)):
                if board[i] == 2:
                    possible_coordinates.appendleft(board_coordinates[i])

            print(possible_coordinates)

            if len(possible_coordinates) >= 3:
                for i in range(len(possible_coordinates)):
                    while count < len(possible_coordinates):
                        if possible_coordinates[i] == possible_coordinates[i - count]:
                            count += 1
                            continue
                        else:
                            while count2 < (len(possible_coordinates) + 1):
                                if possible_coordinates[i - count] == possible_coordinates[i - count2] \
                                        or possible_coordinates[i] == possible_coordinates[i - count2]:
                                    count2 += 1
                                    continue
                                else:
                                    x1 = float(possible_coordinates[i][0])
                                    y1 = float(possible_coordinates[i][1])
                                    x2 = float(possible_coordinates[i - count][0])
                                    y2 = float(possible_coordinates[i - count][1])
                                    x3 = float(possible_coordinates[i - count2][0])
                                    y3 = float(possible_coordinates[i - count2][1])
                                    try:
                                        slope_a = (y2 - y1) / (x2 - x1)
                                    except ZeroDivisionError:
                                        slope_a = 100
                                    try:
                                        slope_b = (y3 - y2) / (x3 - x2)
                                    except ZeroDivisionError:
                                        slope_b = 100
                                    if slope_a == slope_b:
                                        print(slope_a, slope_b)
                                        print((x1, y1), (x2, y2), (x3, y3))
                                        if (x1, y1) in list_of_coordinates_for_computer:
                                            print("o1")
                                            count_for_occupied_grid += 1
                                            first_coordinate_occupied = True
                                        if (x2, y2) in list_of_coordinates_for_computer:
                                            print("o2")
                                            count_for_occupied_grid += 1
                                            second_coordinate_occupied = True
                                        if (x3, y3) in list_of_coordinates_for_computer:
                                            print("o3")
                                            count_for_occupied_grid += 1
                                            third_coordinate_occupied = True
                                        print(count_for_occupied_grid)
                                        if count_for_occupied_grid == 3:
                                            count2 += 1
                                            continue
                                        elif count_for_occupied_grid == 2:

                                            self.notification_of_next_step_to_win = True
                                            if first_coordinate_occupied == False:
                                                self.x_for_next_step = x1
                                                self.y_for_next_step = y1
                                            elif second_coordinate_occupied == False:
                                                self.x_for_next_step = x2
                                                self.y_for_next_step = y2
                                            elif third_coordinate_occupied == False:
                                                self.x_for_next_step = x3
                                                self.y_for_next_step = y3
                                            return self.notification_of_next_step_to_win
                                        elif count_for_occupied_grid == 1:
                                            self.notification_of_next_step = True
                                            number = randint(0, 1)
                                            print(number)
                                            if first_coordinate_occupied == True:
                                                if number == 0:
                                                    self.x_for_next_step = x2
                                                    self.y_for_next_step = y2
                                                else:
                                                    self.x_for_next_step = x3
                                                    self.y_for_next_step = y3
                                            elif second_coordinate_occupied == True:
                                                if number == 0:
                                                    self.x_for_next_step = x1
                                                    self.y_for_next_step = y1
                                                else:
                                                    self.x_for_next_step = x3
                                                    self.y_for_next_step = y3
                                            elif third_coordinate_occupied == True:
                                                if number == 0:
                                                    self.x_for_next_step = x1
                                                    self.y_for_next_step = y1
                                                else:
                                                    self.x_for_next_step = x2
                                                    self.y_for_next_step = y2
                                            return self.notification_of_next_step
                                        elif count_for_occupied_grid == 0:
                                            print(None)
                                            self.notification_of_next_step = True
                                            number = randint(0, 2)
                                            print(number)
                                            if number == 0:
                                                self.x_for_next_step = x1
                                                self.y_for_next_step = y1
                                            elif number == 1:
                                                self.x_for_next_step = x2
                                                self.y_for_next_step = y2
                                            elif number == 2:
                                                self.x_for_next_step = x3
                                                self.y_for_next_step = y3
                                            return self.notification_of_next_step
                                        count_for_occupied_grid = 0
                                    count2 += 1
                            count2 = 0
                        count += 1
                    count = 0

    def First_move(self):
        self.isFirst_move = tkinter.messagebox.askokcancel("First move?", "Player first?")
        if self.isFirst_move == True:
            print("hihi")
            self.canvas.bind("<Button-1>", self.processMouseEvent)
        else:
            print("bye")
            self.computersTurn(self.board)
            self.canvas.bind("<Button-1>", self.processMouseEvent)

Tic_Tac_Toe()

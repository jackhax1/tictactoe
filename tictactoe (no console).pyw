import tkinter as tk

class Tictactoe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Tictactoe')
        self.root.geometry('230x250')
        self.root.resizable(width=False,height=False)
        self.createbutton()
        self.root.mainloop()

    def showgame(self):
        global maingame
        print(maingame)

    def checkgame(self):
        global maingame
        for i in range(0, 3):
            win1 = 0
            win2 = 0
            for j in range(0, 3):
                if maingame[i][j] == 'X':
                    win1 += 1
                if maingame[i][j] == 'O':
                    win2 += 1
            if win1 == 3:
                print('win1-r')
                self.status.delete(0,'end')
                self.status.insert(0,'player1win')
                return True
            if win2 == 3:
                print('win2-r')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player2win')
                return True

        for i in range(0, 3):
            win1 = 0
            win2 = 0
            for j in range(0, 3):
                if maingame[j][i] == 'X':
                    win1 += 1
                if maingame[j][i] == 'O':
                    win2 += 1
            if win1 == 3:
                print('win1-c')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player1win')
                return True
            if win2 == 3:
                print('win2-c')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player2win')
                return True

        for i in range(1):
            win1 = 0
            win2 = 0
            for j in range(0, 3):
                if maingame[j][j] == 'X':
                    win1 += 1
                if maingame[j][j] == 'O':
                    win2 += 1
            if win1 == 3:
                print('win1-diag')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player1win')
                return True
            if win2 == 3:
                print('win2-diag')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player2win')
                return True

        for i in range(1):
            win1 = 0
            win2 = 0
            x = 2
            y = 0
            for j in range(0, 3):
                if maingame[x][y] == 'X':
                    win1 += 1
                if maingame[x][y] == 'O':
                    win2 += 1
                x -= 1
                y += 1
            if win1 == 3:
                print('win1-adiag')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player1win')
                return True
            if win2 == 3:
                print('win2-adiag')
                self.status.delete(0, 'end')
                self.status.insert(0, 'player2win')
                return True
        tiecheck = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if maingame[i][j] != '':
                    tiecheck += 1
        if tiecheck == 9:
            print('tie')
            return True

    def createbutton(self):
        self.label1 = tk.Label(self.root,text='Start')
        self.label1.place(x=50,y=10)
        self.status = tk.Entry(self.root)
        self.status.place(x=30, y=10, width=65, height=20)

        self.buttonstart = tk.Button(self.root, text='Start',command= self.gamestart)
        self.buttonstart.place(x=150, y=10, width=50)

        self.button1 = tk.Button(self.root,command = self.play1)
        self.button1.place(x=30, y=50, height=50, width=50)

        self.button2 = tk.Button(self.root,command=self.play2)
        self.button2.place(x=90, y=50, height=50, width=50)

        self.button3 = tk.Button(self.root,command=self.play3)
        self.button3.place(x=150, y=50, height=50, width=50)

        self.button4 = tk.Button(self.root,command=self.play4)
        self.button4.place(x=30, y=110, height=50, width=50)

        self.button5 = tk.Button(self.root,command=self.play5)
        self.button5.place(x=90, y=110, height=50, width=50)

        self.button6 = tk.Button(self.root,command=self.play6)
        self.button6.place(x=150, y=110, height=50, width=50)

        self.button7 = tk.Button(self.root,command=self.play7)
        self.button7.place(x=30, y=170, height=50, width=50)

        self.button8 = tk.Button(self.root,command=self.play8)
        self.button8.place(x=90, y=170, height=50, width=50)

        self.button9 = tk.Button(self.root,command=self.play9)
        self.button9.place(x=150, y=170, height=50, width=50)

    def gamestart(self):
        global i,maingame

        for i in range (0,3):
            for j in range(0,3):
                maingame[i][j]=''

        self.button1.config(text='')
        self.button2.config(text='')
        self.button3.config(text='')
        self.button4.config(text='')
        self.button5.config(text='')
        self.button6.config(text='')
        self.button7.config(text='')
        self.button8.config(text='')
        self.button9.config(text='')

        if i%2==0:
            self.status.delete(0,'end')
            self.status.insert(0,'Player 1(X)')
        else:
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(O)')

    def play1(self):
        global i,maingame
        if i%2==0:
            maingame[0][0]='X'
            self.button1.config(text='X')
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(O)')
        else:
            self.button1.config(text='O')
            maingame[0][0] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i+=1
        self.checkgame()

    def play2(self):
        global i
        if i%2==0:
            self.button2.config(text='X')
            maingame[0][1] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button2.config(text='O')
            maingame[0][1] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i+=1
        self.checkgame()

    def play3(self):
        global i
        if i%2==0:
            self.button3.config(text='X')
            maingame[0][2] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button3.config(text='O')
            maingame[0][2] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i+=1
        self.checkgame()

    def play4(self):
        global i
        if i%2==0:
            self.button4.config(text='X')
            maingame[1][0] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button4.config(text='O')
            maingame[1][0] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i+=1
        self.checkgame()

    def play5(self):
        global i
        if i%2==0:
            self.button5.config(text='X')
            maingame[1][1] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button5.config(text='O')
            maingame[1][1] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i+=1
        self.checkgame()

    def play6(self):
        global i
        if i % 2 == 0:
            self.button6.config(text='X')
            maingame[1][2] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button6.config(text='O')
            maingame[1][2] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i += 1
        self.checkgame()

    def play7(self):
        global i
        if i % 2 == 0:
            self.button7.config(text='X')
            maingame[2][0] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button7.config(text='O')
            maingame[2][0] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i += 1
        self.checkgame()

    def play8(self):
        global i,maingame
        if i % 2 == 0:
            self.button8.config(text='X')
            maingame[2][1] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button8.config(text='O')
            maingame[2][1] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i += 1
        self.checkgame()

    def play9(self):
        global i
        if i % 2 == 0:
            self.button9.config(text='X')
            maingame[2][2] = 'X'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 2(0)')
        else:
            self.button9.config(text='O')
            maingame[2][2] = 'O'
            self.status.delete(0, 'end')
            self.status.insert(0, 'Player 1(X)')
        i += 1
        self.checkgame()

i=0
maingame= [['','',''],
           ['','',''],
           ['','','']]

app = Tictactoe()

from tkinter import *
from tkinter.messagebox import showinfo, showwarning


x = 0
# array holding the block no occupied by each player respectively
player_1 = []
player_2 = []

# funtion to check the winning condition

def check_winner_player(a, s):
    t = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {7, 5, 3}]
    flag = 0
    for i in t:
        if all(v in a for v in i):
            flag = 1
            break
    if flag == 1:
        if s == "p1":
            showinfo("Tic-Tac-Toe", message=("Congratulations  " + entry1.get() + "  !!!!\n you win"))
        else:
            showinfo("Tic-Tac-Toe", message=("Congratulations  " + entry2.get() + "  !!!!\n you win"))
    elif set(player_1).union(set(player_2)) == set(range(1, 10)):
        showinfo(title="Tic-Tac-Toe", message="This is a Draw!!")

# funtion to define the sign "X" or "O" which will print alternatively
def define_sign(n, a):
    global x
    # conditon checking if the player has clicked on the already filled block
    if n in player_2 or n in player_1:
        showwarning("Tic-Tic-Toe", "Already filled! please choose the another box")
    
    # checking which player's move is this.. even moves will be of player 1 as player 1 will start the game 
    if x % 2 == 0:
        a.config(text="X", font=("times", 10, 'bold'))
        player_1.append(n)
        check_winner_player(player_1, "p1")
    else:
        a.config(text="O", font=("times", 10, 'bold'))
        player_2.append(n)
        check_winner_player(player_2, "p2")
    x += 1

def fun():

    global entry1
    global entry2

    x = Tk()
    x.geometry("776x550+300+0")
    x.configure(background="light blue")
    x.title("TIC-TAC-TOE")

    tops = Frame(x, bg="red", pady=2, padx=10, height=100, width=776, bd=10, relief=RIDGE)
    tops.grid(row=0, column=0)

    l1 = Label(tops, font=('arial', 50, 'bold'), text="TIC - TAC - TOE  GAME", bg="yellow", fg="red", justify=CENTER)
    l1.grid(row=0, column=0)

    main_frame = Frame(x, bg="green", pady=2, height=400, width=776, bd=10, relief=RIDGE)
    main_frame.grid(row=1, column=0)


    frame1 = Frame(main_frame, bg="green", pady=2, height=200, width=190, bd=10, relief=RIDGE)
    frame1.grid(row=0, column=0)

    frame2 = Frame(main_frame, bg="green", pady=2, height=200, width=190, bd=10, relief=RIDGE)
    frame2.grid(row=1, column=0)

    l2 = Label(frame1, text="Player 1 : ", font=('time', 10, 'bold'))
    l2.grid(row=0, column=0)

    entry1 = Entry(frame1, text="", font=('time', 10, 'bold'))
    entry1.grid(row=0, column=1)

    l3 = Label(frame1, text="Player 2 : ", font=('time', 10, 'bold'))
    l3.grid(row=1, column=0)

    entry2 = Entry(frame1, text="", font=('time', 10, 'bold'))
    entry2.grid(row=1, column=1)

    b1 = Button(frame2, width=8, height=4, command=lambda: define_sign(1, b1))
    b1.grid(row=2, column=2)
    b2 = Button(frame2, width=8, height=4, command=lambda: define_sign(2, b2))
    b2.grid(row=2, column=3)
    b3 = Button(frame2, width=8, height=4, command=lambda: define_sign(3, b3))
    b3.grid(row=2, column=4)
    b4 = Button(frame2, width=8, height=4, command=lambda: define_sign(4, b4))
    b4.grid(row=3, column=2)
    b5 = Button(frame2, width=8, height=4, command=lambda: define_sign(5, b5))
    b5.grid(row=3, column=3)
    b6 = Button(frame2, width=8, height=4, command=lambda: define_sign(6, b6))
    b6.grid(row=3, column=4)
    b7 = Button(frame2, width=8, height=4, command=lambda: define_sign(7, b7))
    b7.grid(row=4, column=2)
    b8 = Button(frame2, width=8, height=4, command=lambda: define_sign(8, b8))
    b8.grid(row=4, column=3)
    b9 = Button(frame2, width=8, height=4, command=lambda: define_sign(9, b9))
    b9.grid(row=4, column=4)
    x.mainloop()


# beginning of execution
fun()

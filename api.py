from random import randint
import tkinter

stats = []

def get_winner(call):
    t = ["rock", "paper", "scissors", "lizard", "spock"]

    throw = t[randint(0,4)]

    if (throw == "rock" and call == "paper") or (throw == "rock" and call == "spock")\
            or (throw == "paper" and call == "scissors") or (throw == "paper" and call == "lizard")\
            or (throw == "scissors" and call == "rock") or (throw == "scissors" and call == "spock")\
            or (throw == "lizard" and call == "rock") or (throw == "lizard" and call == "scissors")\
            or (throw == "spock" and call == "paper") or (throw == "spock" and call == "lizard"):
        stats.append('W')
        result = "You won! " + call + " beats " + throw + "!"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lose! " + throw + " beats " + call + "!"

    global output
    output.config(text=result)

def pass_s():
    get_winner("scissors")
def pass_r():
    get_winner("rock")
def pass_p():
    get_winner("paper")
def pass_l():
    get_winner("lizard")
def pass_v():
    get_winner("spock")

window = tkinter.Tk()
window.title("Rock, Paper, Scissors, Lizard, Spock?")

scissors = tkinter.Button(window, text = "Scissors", bg = "#ff9999", padx=10, pady=5, command=pass_s, width=40)
rock = tkinter.Button(window, text = "Rock", bg = "#80ff80", padx=10, pady=5, command=pass_r, width=40)
paper = tkinter.Button(window, text = "Paper", bg = "#3399ff", padx=10, pady=5, command=pass_p, width=40)
lizard = tkinter.Button(window, text = "Lizard", bg = "#00ff00", padx=10, pady=5, command=pass_l, width=40)
spock = tkinter.Button(window, text = "Spock", bg = "#777777", padx=10, pady=5, command=pass_v, width=40)
output = tkinter.Label(window, width=40, fg = "red", text="What's your call?")

scissors.pack()
rock.pack()
paper.pack()
lizard.pack()
spock.pack()
output.pack()
window.mainloop()

for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou lose the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou win the series."

print(result)

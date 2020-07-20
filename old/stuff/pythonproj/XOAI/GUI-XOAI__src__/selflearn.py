
from random import choice


epochs = int(input("enter epoch #: "))
comm = input("enter command (truncate): ")
grid = []
logs = {}
if comm == "truncate":
    f = open("memory.txt", "w")
    f.truncate(0)
    f.close()
f = open("memory.txt", "r+")
f1 = f.readlines()
for x in f1:
    sol = []
    for i in x[9:].strip("\n"):
        sol.append(int(i))
    logs[x[:9]] = sol
f.close()

def init():
    for y in range(0, 9):
        grid.append(str(y + 1))

def update(log):
    for x in log.keys():
        if x in logs.keys():
            logs[x].append(log[x])
        else:
            logs[x] = [log[x]]

def draw():
    for x in range(0, 3):
        y = 3 * x
        print("".join(grid[y:y + 3]))

def remove(the_list, val):
    return [value for value in the_list if value != val]

init()

def win():
    g = grid
    wins = (
        g[0:3],
        g[3:6],
        g[6:9],
        g[0:9:3],
        g[1:9:3],
        g[2:9:3],
        g[0:9:4],
        [g[2], g[4], g[6]])
    if ["X", "X", "X"] in wins:
        return "X"
    elif ["O", "O", "O"] in wins:
        return "O"
    return 0

templogs = {}
Owin = 0
Xwin = 0
ties = 0
l = 40
counter = l
counter = int((epochs - (epochs % counter))) / counter
for x in range(int(epochs)):
    if (x % counter == 0):
        print("÷" * (l - (int(int(x) / int(counter)))))
    grid = []
    init()
    templogs = {}
    for x in range(9):
        if win() == "O":
            update(templogs)
            Owin += 1
            break
        elif win() == "X":
            Xwin += 1
            break
        if x % 2 == 0:
            avail = remove(grid, "X")
            avail = remove(avail, "O")
            pick = choice(avail)
            grid[int(pick) - 1] = "X"
        else:
            avail = remove(grid, "X")
            avail = remove(avail, "O")
            pick = choice(avail)
            templogs["".join(grid)] = pick
            grid[int(pick) - 1] = "O"
    if win() == 0:
        update(templogs)
        ties += 1
input("press enter to view results")
print("\n" * 20)
# for x in logs.keys():
# print(x, " =>", logs[x])
print(len(logs), " cases :")
print("X won %d times", Xwin)
print("O won %d times", Owin)
print("# of ties: ", ties)
input("press enter to save file")
print("\n\n\n\n saving DO NOT TURN OFF")
f = open("memory.txt", "a")
f.truncate(0)
epochs = len(logs)
a = 0
counter = l
counter = int((epochs - (epochs % counter))) / counter
for x in logs.keys():
    a += 1
    print((a / epochs) * 100, "%")
    f.write(x + str(max(logs[x], key=logs[x].count)) + "\n")
f.close()
print("now safe to close program")


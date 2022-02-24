import tkinter as tk

size = (9, 9)
board = {(2,3):"w", (3,3):"w", (4,3):"w", (5,3):"w", (2,2):"w", (2,1):"w", (3,5):"w"}
#air = None, wall = x, start = s, end = e, processing = p, path = o
start = (1, 1)
end = (4, 2)
mainlist = [(start, 0)]
step = 0

root = tk.Tk()
root.title("A* Pathfinding Algorithm")
root.geometry("500x500")
titlelabel = tk.Label(root, text=f"{size} table")
titlelabel.pack()
frame1 = tk.Frame(root, bg="grey79")
frame1.pack()

processbut = tk.Button(root, text="Process!")
processbut.pack()


def constructwall():
    for i in range(size[0]):
        board[(i, 0)] = "w"
        board[(i, size[0]-1)] = "w"
    for i in range(size[1]):
        board[(0, i)] = "w"
        board[(size[1] - 1, i)] = "w"
    board[start] = "s"
    board[end] = "e"

def updateFrame():
    for e in frame1.winfo_children():
        e.grid_forget()

    for r in range(size[0]):
        for c in range(size[1]):
            if board.get((r,c)) == None:
                nlabel = tk.Label(frame1, text="     ", bg="white")
            elif board[(r,c)] == "w":
                nlabel = tk.Label(frame1, text="     ", bg="brown")
            elif board[(r,c)] == "s":
                nlabel = tk.Label(frame1, text="  s  ", bg="yellow")
            elif board[(r,c)] == "e":
                nlabel = tk.Label(frame1, text="  e  ", bg="red")
            elif board[(r,c)] == "p":
                nlabel = tk.Label(frame1, text="     ", bg="cadetblue1")
            elif board[(r,c)] == "o":
                nlabel = tk.Label(frame1, text="     ", bg="orange")

            nlabel.grid(row=r, column=c, padx=2, pady=2)

def testifAir(testcord):

    print(f"testing {testcord}", end=",  ")
    if board.get(testcord) == None:
        board[testcord] = "p"
        mainlist.append((testcord, step+1))
        print("air")
    elif board[testcord] == "e":
        print("found end")
        foundEnd()
    else:
        print("wall")

def process():
    global step
    for i in mainlist:
        if i[1] == step:
            print("legit square cord:", i[0])
            cord = i[0]
            testifAir((cord[0] + 1, cord[1]))
            testifAir((cord[0] - 1, cord[1]))
            testifAir((cord[0], cord[1] + 1))
            testifAir((cord[0], cord[1] - 1))

    step += 1
    updateFrame()
    print("end process")

def backtrack(path, s):
    print(f"{path=} {s=}")
    if ((path[0]+1, path[1]), s) in mainlist:
        path2 = (path[0]+1, path[1])
    if ((path[0]-1, path[1]), s) in mainlist:
        path2 = (path[0]-1, path[1])
    if ((path[0], path[1]+1), s) in mainlist:
        path2 = (path[0], path[1]+1)
    if ((path[0], path[1]-1), s) in mainlist:
        path2 = (path[0], path[1]-1)

    return path2

def foundEnd():
    path = end
    processbut["state"] = "disabled"
    processbut["text"] = "Pathing..."

    for o in range(step):
        path = backtrack(path, step-o)
        board[path] = "o"

    updateFrame()
    print(f"Path Finding Finished in {step+1} steps")

def main():
    processbut.config(command=process)

    constructwall()
    updateFrame()
    root.mainloop()


if __name__ == "__main__":
    main()









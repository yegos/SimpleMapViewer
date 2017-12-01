import tkinter
from PIL import Image, ImageTk
from pathlib import Path

basedir = "./map"

class State:
    def __init__(self, z_, x_, y_):
        self.z = z_
        self.x = x_
        self.y = y_

    def zoom(self):
        return self.z

    def to_str(self):
        return basedir + "/" + str(self.z) + "/" + str(self.x) + "/" + str(self.y) + ".png"

state_list = [State(0, 0, 0)]

root = tkinter.Tk()
root.title("Map Viewer")
root.resizable(0, 0)
im_main = ImageTk.PhotoImage(Image.open(state_list[0].to_str()))
label = tkinter.Label(root, image=im_main)
label.grid(row=1, column=1)


def key(event):
    global label
    if event.char == '5':
        if len(state_list) > 1:
            print("::back-to-pre-state")
            print("::::", state_list[-1].to_str() , " to ", state_list[-2].to_str(), sep="")
            state_list.pop(-1)
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::base-state")

    if event.char == '1':
        z = state_list[-1].z + 1
        x = 2*state_list[-1].x
        y = 2*state_list[-1].y
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")

    if event.char == '7':
        z = state_list[-1].z + 1
        x = 2*state_list[-1].x
        y = 2*state_list[-1].y + 1
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")

    if event.char == '9':
        z = state_list[-1].zoom() + 1
        x = 2*state_list[-1].x + 1
        y = 2*state_list[-1].y + 1
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")

    if event.char == '3':
        z = state_list[-1].zoom() + 1
        x = 2*state_list[-1].x + 1
        y = 2*state_list[-1].y
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")
			
    if event.char == '2':
        z = state_list[-1].z
        x = state_list[-1].x
        y = state_list[-1].y - 1
		
        right = 2 ** z - 1
        left = 0
        x = x if x <= right else right
        x = x if x >= left else left
        y = y if y <= right else right
        y = y if y >= left else left
		
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")
			
    if event.char == '4':
        z = state_list[-1].z
        x = state_list[-1].x - 1
        y = state_list[-1].y
		
        right = 2 ** z - 1
        left = 0
        x = x if x <= right else right
        x = x if x >= left else left
        y = y if y <= right else right
        y = y if y >= left else left
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")
			
    if event.char == '6':
        z = state_list[-1].z
        x = state_list[-1].x + 1
        y = state_list[-1].y

        right = 2 ** z - 1
        left = 0
        x = x if x <= right else right
        x = x if x >= left else left
        y = y if y <= right else right
        y = y if y >= left else left
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")
			
    if event.char == '8':
        z = state_list[-1].z
        x = state_list[-1].x 
        y = state_list[-1].y + 1

        right = 2 ** z - 1
        left = 0
        x = x if x <= right else right
        x = x if x >= left else left
        y = y if y <= right else right
        y = y if y >= left else left
        new_state = State(z, x, y)
        if Path(new_state.to_str()).is_file():
            print("::new-", z, "-", x, "-", y, "-state", sep="")
            state_list.append(State(z, x, y))
            im_main_new = ImageTk.PhotoImage(Image.open(state_list[-1].to_str()))
            new_label = tkinter.Label(root, image=im_main_new)
            new_label.image = im_main_new
            label.grid_forget()
            label.destroy()
            label = new_label
            new_label.grid(row=1, column=1)
        else:
            print("::new level does not exist")

root.bind("<Key>", key)
root.mainloop()

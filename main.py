from tkinter import filedialog
from tkinter import *
import os
import shutil
import pandas as pd

root = Tk()
folder_path = StringVar()
root.title('G Studio 5')
# root.geometry('200x100')


def list_to_csv(path, lst):
    df = pd.DataFrame(lst)
    # saving the dataframe
    df.to_csv(path, encoding='utf-16', index=False)


def filetolist(name=" "):
    if not name.endswith('.txt'):
        name = name + '.txt'

    f = open(name, "r")
    line = " "
    lst = []
    while line:
        if line != '\n':
            arr = line.split('\t')

            if len(arr) > 1:
                arr = arr[1].split('\n')
                temp = list(range(100))
                for i in range(1, 100):
                    temp[i] = str(temp[i]) + '.'
                if arr[0] in temp:
                    arr2 = arr.split(" ")[1:]
                    arr.clear()
                    for i in arr2:
                        arr = arr + i + " "
            else:
                arr = arr[0].split('\n')
                temp = list(range(100))
                for i in range(1, 100):
                    temp[i] = str(temp[i]) + '.'
                if arr[0] in temp:
                    arr2 = arr.split(" ")[1:]
                    arr.clear()
                    for i in arr2:
                        arr = arr + i + " "
            # print("|" + arr[0] + "|")
            lst.append(arr[0])
        line = f.readline()
    f.close()
    lst.remove(" ")
    return lst


def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    lbl1['text'] = ''
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    selectDir(filename)


def read_text_file(path, file):
    file_path = f"{path}\{file}"
    lst = filetolist(file_path)
    file = file.split(".")[0]
    list_to_csv(path+'\\Done\\'+file+'.csv', lst)
    shutil.move(path+"\\"+file+".txt", path+"\\textDone\\"+file+".txt")


# c://desktop//file.txt
# file.txt
def moveToDir(parent_dir):
    # Directory
    directory = "Done"
    directory2 = "textDone"
    # Path
    destination = os.path.join(parent_dir, directory)
    if not os.path.isdir(destination):
        os.mkdir(destination)
    destination2 = os.path.join(parent_dir, directory2)
    if not os.path.isdir(destination2):
        os.mkdir(destination2)
    # Move the content of
    # source to destination


def selectDir(path):
    # Change the directory
    os.chdir(path)
    # Read text File
    # iterate through all file
    tryDone = 0
    moveToDir(path)
    for file in os.listdir():
        # Check whether file is in text format or not
        if file.endswith(".txt"):
            # call read text file function
            read_text_file(path, file)
        else:
            tryDone += 1
    print("Converted")
    lbl1['text'] = 'Done'
# desktop/file1.txt


Label(text="G Studio5", width = 20, height = 1).pack()
# lbl1.grid(row=3, column=3)

lbl2 = Label(text="Text to CSV converter", width = 20, height = 3)
# lbl1.grid(row=3, column=3)
lbl2.pack()

button2 = Button(text="Select Folder", command=browse_button, fg='black', bg='skyblue')
# button2.grid(row=1, column=3)
button2.pack()

lbl1 = Label(text="waiting")
# lbl1.grid(row=3, column=3)
lbl1.pack()

mainloop()

import Parser
import Player
from tkinter import *


root = Tk()
root.geometry("570x420")
root.title(string="IPTV")
root.iconbitmap("TV.ico")

global channelList
global selectedChannel
channelList=[]





def play_channel():
    global selectedChannel
    channelListName = Parser.get_AllName(channelList)
    number = int(channelListName.index(screenLB.get(ANCHOR)))
    link = Parser.linkFromList(channelList, number)
    Player.play(link)
    selectedChannel = screenLB.get(ANCHOR)


#playing next channel
def next_channel():
    global selectedChannel

    channelListName = Parser.get_AllName(channelList)
    number = int(channelListName.index(selectedChannel))  #actual channel index
    nextChannel = channelListName[number + 1]
    link = Parser.linkFromList(channelList, number +1)
    stop_buffering()
    Player.play(link)
    selectedChannel = nextChannel

def previous_channel():
    global selectedChannel

    channelListName = Parser.get_AllName(channelList)
    number = int(channelListName.index(selectedChannel))  #actual channel index
    nextChannel = channelListName[number - 1]
    link = Parser.linkFromList(channelList, number -1)
    stop_buffering()
    Player.play(link)
    selectedChannel = nextChannel


def stop_buffering():
    Player.stop()

def channelNamesPrint():
    global channelList
    channelList = Parser.get_List()
    channelListNames = Parser.get_AllName(channelList)

    screenLB.delete(0, END)
    for channel in channelListNames:
        screenLB.insert(END, channel)



def searchChannel(channel):
    global channelList


    channelList = Parser.searchChannel(channel)
    channelListNames = Parser.get_AllName(channelList)

    screenLB.delete(0, END)
    for channel in channelListNames:
        screenLB.insert(END, channel)


def showCateg():
    categ_List = Parser.get_AllCategories()

    screenLB.delete(0, END)
    for categ in categ_List:
        screenLB.insert(END, categ)
def selectCateg():
    global channelList

    categ = screenLB.get(ANCHOR)

    channelList = Parser.searchcategory(categ)
    channelListNames = Parser.get_AllName(channelList)

    screenLB.delete(0, END)
    for channel in channelListNames:
        screenLB.insert(END, channel)

#creat search and entry box to search for channel use a previous function
def show_searchChannel_button():
    searchBox = Entry(root, text="enter channel Name")
    searchBox.grid(row=4, column=1)

    searchEnterB = Button(root, text="Search!", command=lambda: searchChannel(searchBox.get()))
    searchEnterB.grid(row=4, column=4)





#seeting up menu BOX

my_frame = Frame(root)
frame_scrollbar =  Scrollbar(my_frame, orient=VERTICAL, )

screenLB = Listbox(my_frame, width=50, yscrollcommand=frame_scrollbar)

frame_scrollbar.config(command=screenLB.yview)
frame_scrollbar.pack(side=RIGHT, fill=Y)

my_frame.grid(row=1, column=10)
screenLB.pack()


#Buttons Inisiated
showNamesB = Button(root, text="Show available channels", command=channelNamesPrint,width=20, height=2)
showNamesB.grid(row=1, column=1)

showCategoriesB = Button(root, text="Show available Categories", command=showCateg,width=20, height=2)
showCategoriesB.grid(row=2, column=1)

searchForChannelB = Button(root, text="Search for channel",command=show_searchChannel_button ,width=20, height=2)
searchForChannelB.grid(row=3, column=1)

exitB=Button(root, text="EXIT", command=exit)
exitB.grid(row=5,column=1)

selectB=Button(root,text="SELECT", command=selectCateg, width=5, height=2)
selectB.grid(row=2,column=2)


#play Buttons


playB=Button(root, text="▶", command=play_channel,width=5, height=2)
playB.grid(row=4,column=2)

stopB=Button(root, text="⏸",command=stop_buffering , width=5, height=2)
stopB.grid(row=4,column=3)

#assign button to remote controll


root.bind("p", lambda e : play_channel())
root.bind("o", lambda e : stop_buffering())
root.bind("w", lambda e : next_channel())
root.bind("s", lambda e : previous_channel())

root.mainloop()

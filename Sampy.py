import os
from tkinter import *
from mutagen.mp3 import MP3
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox

root = Tk()


statusbar = Label(root, text= 'Hey there', relief= SUNKEN, anchor=W)
statusbar.pack(side = BOTTOM, fill = X)

# root window= statusbar, leftframe, rightframe
# leftframe= playlist
# rightframe= topframe, middleframe, bottomframe

#creating a menubar

menubar = Menu(root)
root.config(menu = menubar)

leftframe= Frame(root)
leftframe.pack(side= LEFT)

playlist= []

def browse_file():
    global filename_path
    filename_path = filedialog.askopenfile()
    add_to_playlist(filename_path)

def add_to_playlist(filename):
    # filename= os.path.basename(filename)
    index= 0
    playlistbox.insert(index, filename)
    playlist.insert(index, filename_path)
    index +=1

playlistbox = Listbox(leftframe)
playlistbox.pack()

btnadd= Button(leftframe,text= "+ ADD", command= browse_file)
btnadd.pack(side= LEFT)

def del_song():
    selected_song= playlistbox.curselection()
    selected_song=int(selected_song[0])
    playlistbox.delete(selected_song)
    playlist.pop(selected_song)
btndel= Button(leftframe,text= "- DEL", command= del_song)
btndel.pack(side= LEFT)

rightframe = Frame(root)
rightframe.pack()

topframe= Frame(rightframe)
topframe.pack()


#creating a sub-menu

subMenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu= subMenu)
subMenu.add_command(label= "Open", command = browse_file)
subMenu.add_command(label= "Exit", command = root.destroy)

def about_us():
    tkinter.messagebox.showinfo("Sampy", message= "SAMEER MAHAJAN SE COMPS-A")


subMenu = Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "Help", menu= subMenu)
subMenu.add_command(label= "About us", command = about_us)


mixer.init() #initialising


root.title("sampy")
root.iconbitmap(r'images/sampy.ico')

filelabel = Label(topframe, text= 'Welcome to sampy music player')
filelabel.pack(pady=10)

# lengthlabel = Label(root, text= 'Total Length : --:--')
# lengthlabel.pack()



def show_details():
    filelabel['text'] = 'Playing'
    # file_data = os.path.splitext(filename)
    # if file_data[1] == '.mp3':
    #     audio = MP3(filename)
    #     total_length = audio.info.length
    # else:
    #     a = mixer.Sound(filename)
    #     total_length = a.get_length()
    #     min, sec = divmod(total_length, 60)
    #     min = round(min)
    #     sec = round(sec)
    #     timeformat = '(:02d):(:02d)'.format(min, sec)
    #     lengthlabel['text'] = "Total Length" + '-' + timeformat




def play_music():
    global paused

    if paused:
        mixer.music.unpause()
        statusbar['text'] = 'Music Resumed'
        paused= FALSE
    else:
        try:
            selected_song= playlistbox.curselection()
            selected_song = int(selected_song[0])
            play_it= playlist[selected_song]
            mixer.music.load(play_it)
            mixer.music.play()
            statusbar ['text'] = "Music is playing"
            show_details()

        except:
            tkinter.messagebox.showerror('Sampy','Sampy could not find the file')



def stop_music():
    mixer.music.stop()
    statusbar['text']= 'Music stopped'

paused = FALSE

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusbar['text'] = 'Music paused'

def rewind_music():
    play_music()
    statusbar['text']='Music Rewinded'

def set_vol(val):
    volume = int(val)/100
    mixer.music.set_volume(volume) #set volume of mixer takes value only from 0 to 1. eg. 0.2, 0.4

muted = FALSE

def mute_music():
    global muted

    if muted:
        mixer.music.set_volume(0.7)
        volumeb5.configure(image = volumebutton)
        scale.set(70)
        muted=FALSE
    else:
        mixer.music.set_volume(0)
        volumeb5.configure(image=mutebutton)
        scale.set(0)
        muted=TRUE


middleframe= Frame(rightframe)
middleframe.pack(padx=30,pady=30)

playPhoto = PhotoImage(file= 'images/playbutton.png')
playb1 = Button(middleframe, image= playPhoto, command = play_music)
playb1.grid(row=0,column= 0,padx=10)

stopPhoto = PhotoImage( file= 'images/stopbutton.png')
stopb2 = Button(middleframe, image= stopPhoto, command = stop_music)
stopb2.grid(row=0,column=1,padx=10)

pausePhoto = PhotoImage( file= 'images/pausebutton.png')
pauseb3 = Button(middleframe, image= pausePhoto, command = pause_music)
pauseb3.grid(row=0,column=2,padx=10)

bottomframe = Frame(rightframe)
bottomframe.pack()

rewindPhoto = PhotoImage(file= 'images/rewindbutton.png')
rewindb4 = Button(bottomframe, image= rewindPhoto, command= rewind_music)
rewindb4.grid(row=0, column=0)

mutebutton = PhotoImage(file = 'images/mutebutton.png')
volumebutton = PhotoImage(file = 'images/volumebutton.png')
volumeb5 = Button(bottomframe, image = volumebutton,command=mute_music)
volumeb5.grid(row=0,column=1)


scale = Scale(bottomframe, from_=0 ,to=100,orient = HORIZONTAL, command =set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.grid(row=0, column= 2, padx=30,pady=15)




root.mainloop()

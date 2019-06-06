#declaring the menubar and adjusting the postion of the buttons
leftframe=Frame(root)
leftframe.pack(side=LEFT)

rightframe=Frame(root)
rightframe.pack(side=RIGHT)

topframe=Frame(rightframe)
topframe.grid(row=0,column=0)

middleframe=Frame(rightframe)
middleframe.grid(row=1,column=0)

bottomframe=Frame(rightframe)
bottomframe.grid(row=2,column=0)

menubar= Menu (root)
root.config(menu=menubar)

submenu=Menu(menubar,tearoff=0)



#adjusting the backgrouund photo of music_player
labelphoto=Label(topframe,image=photo)
labelphoto.grid(padx=15,pady=15)



#adding the menubar button and there command
menubar.add_cascade(label='file',menu=submenu)

submenu.add_command(label='Exit',command=root.destroy)

submenu=Menu(menubar,tearoff=0)

menubar.add_cascade(label='help',menu=submenu)

submenu.add_command(label='about project',command=show_off)


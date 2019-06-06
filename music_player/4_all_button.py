#declaring the listbox for storing the song which are slected
list_box=Listbox(leftframe)
list_box.pack(padx=15)
playlist =[]
index=0


        
#all buttons initialisation
add_butn=Button(leftframe,text='add+',command=add_song)
add_butn.pack(side=LEFT,padx=20,pady=10)

del_butn=Button(leftframe,text='del-',command=del_song)
del_butn.pack(side=RIGHT,padx=20,pady=10)

next_butn=Button(middleframe,text='next',command=next_song)
next_butn.grid(row=2,column=2,padx=10,pady=10)

previous_butn=Button(middleframe,text='previous',command=previous_song)
previous_butn.grid(row=2,column=0,padx=10,pady=10)

play_butn=Button(middleframe,text='play',command=check_it)
play_butn.grid(row=1,column=1,padx=10,pady=10)

stop_butn=Button(middleframe,text='stop',command=stop_it)
stop_butn.grid(row=0,column=0,padx=10,pady=10)

distance_butn=Button(middleframe,text='image',command=distance_working)
distance_butn.grid(row=0,column=2,padx=10,pady=10)

#declaring the scale for song volume
scale=Scale(bottomframe,from_=0,to=100,orient=HORIZONTAL,command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)
scale.pack(padx=10,pady=15)
        

#repeating the window loop again again to sj=how thw window of Music_Player
root.mainloop()        
        
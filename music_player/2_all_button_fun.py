#function for finding distance for distance_butn

def find_marker(image):
    blurred_frame=cv2.GaussianBlur(image,(5,5),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)
    lower=np.array([38,86,0])
    upper=np.array([121,255,255])
    mask=cv2.inRange(hsv,lower,upper)
    _,contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    con=max(contour,key=cv2.contourArea)
    return cv2.minAreaRect(con)


def distance_to_camera(x,y,z):
    return (x*y)/z


def distance_finder():
    know_dis = 30.0
    know_wid= 3.0
    global cap
    cap=cv2.VideoCapture(0)
    ret,image=cap.read()
    marker=find_marker(image)
    focallength=(marker[1][0]*know_dis)/know_wid
    time.sleep(2)
    while ret:  
        ret,image=cap.read()
        marker=find_marker(image)
        cm=distance_to_camera(know_wid,focallength,marker[1][0])
        cv2.putText(image,"%.2fcm" % cm,(image.shape[1]-350,image.shape[0]-15),cv2.FONT_HERSHEY_SIMPLEX
                   ,2.0,(255,0,0),3)
        cv2.imshow("image",image)
        if cv2.waitKey(1)==27:
            return(cm)
            


#declaration of all the button function


#function for next_song button
nextsong=TRUE
def next_song():
    global played
    global current
    global index
    global first
    current=current+1
    if current==index:
        current =0
    else:
        pass
    first=TRUE
    played=TRUE
    play_it()


#function for previous_song button
def previous_song():
    global played
    global current
    global index
    global first
    if current==0:
        current =index-1
    else:
        current=current-1
    first=TRUE
    played=TRUE
    play_it()
    

#function for help on the menubar button
def show_off():
    tkinter.messagebox.showinfo('about project','first play the song take a bottle cap and first put it at 30 cm from camera and '
                                'after that press image button and know put the cap at any distance '
                                'what you want and press escape key so it will count that distance '
                                'and change the volume plase the distance of cap should ne below 150cm '
                                'thank you for taking our help')
    
 

#function for help play button for checking whether the song is stoped or
# is there anty song in the list or not button
def check_it():
    global stoped
    global index
    if stoped:
        if index==0:
            tkinter.messagebox.showerror('error','please add the songs')
        else:
            play_it()
    else:
        tkinter.messagebox.showerror('error','please unstop the songs')
        
#after cheking functinon to play the song      
played=TRUE
first=TRUE
current =0
def play_it():
    global first
    global current
    global played
    if played:
        if first:
            songname=playlist[current]
            mixer.music.load(songname)
            mixer.music.play()
            first=FALSE
        else:
            mixer.music.unpause()
        play_butn.configure(text='paused')
        played=FALSE
    else:
        mixer.music.pause()
        play_butn.configure(text='play')
        played=TRUE


#function for sop function      
stoped=TRUE
def stop_it():
    global stoped
    if stoped:
        mixer.music.stop()
        stop_butn.configure(text='unstop')
        stoped=FALSE
    else:
        if played:
            stop_butn.configure(text='stop')
            stoped=TRUE
        else:
            mixer.music.play()
            stop_butn.configure(text='stop')
            stoped=TRUE


#for volume button
def set_vol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)
        
        
#for distance buttonn or can say image button
def distance_working():
    volume=distance_finder()
    cv2.destroyAllWindows()
    cap.release()
    vol=(volume*1.0)/150
    volume=(volume*100)/150
    mixer.music.set_volume(vol)
    scale.set(volume)       
        


#function for add song button
def add_song():
    global file_path
    file_path=filedialog.askopenfilename()
    added(file_path)


def added(filename):
    global index
    filename=os.path.basename(filename)
    list_box.insert(index,filename)
    playlist.insert(index,file_path)
    index=index+1




#function for delete song button from list
deleted=TRUE
notpass=TRUE
def del_song():
    global index
    global current
    global deleted
    global notpass
    if index==1:
        filedialog.messagebox.showerror('error','playlist will become empty')
        return
    else :
        pass
    index=index-1
    if current==index:
        current=current-1
        songname=playlist[current]
        mixer.music.load(songname)
        mixer.music.play()
        first=FALSE
        play_butn.configure(text='paused')
        played=FALSE
        list_box.delete(index)
        playlist.pop(index)
    else:
        list_box.delete(index)
        playlist.pop(index)

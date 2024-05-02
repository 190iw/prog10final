import PainterD1
import time
import os
import sys # to access the system
import cv2

# IMG STUFF
image = cv2.imread("pubkept.png")
image2 = cv2.imread("fight.png")
image3 = cv2.imread("runafter.png")

# PUBLISH OR KEPT IMG
def display_pubkept():
    cv2.imshow("CONSIENCE", image)
    cv2.waitKey(1)

# FGIHT
def display_fight():
    cv2.imshow("CONSIENCE", image2)
    cv2.waitKey(1)

# RUN AFTER
def display_runafter():
    cv2.imshow("INSTINCT", image3)
    cv2.waitKey(1)

# for vids/cutscenes
def display_cutscene(video_file):
    cap = cv2.VideoCapture(video_file)

    #FULLSCREEEN
    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)


    while cap.isOpened(): # shows the video
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'): # used to skip the cutscenes by pressing q
            break

    cap.release()
    cv2.destroyAllWindows() #destroys all cv2 windows afer use


## variable
pub = 0 
kept = 0

### MAIN GAME

time.sleep (2)
display_pubkept()
input = input("Moments after I had... ").lower() #Published or Kept in attic
while True:
    if input == "published":
        pub += 1
        os.system('cls')
        cv2.destroyAllWindows()  # Close the window
        import PbD1
        break
    elif input == "kept":
        kept += 1
        os.system('cls')
        cv2.destroyAllWindows()  # Close the window
        import KD1
        break

time.sleep(4)
print ('''
       
░▒▓███████▓▒░   ░▒▓██████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░       ░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░              ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░              ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓████████▓▒░  ░▒▓██████▓▒░         ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░           ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░           ░▒▓█▓▒░        
░▒▓███████▓▒░  ░▒▓█▓▒░░▒▓█▓▒░    ░▒▓█▓▒░           ░▒▓████████▓▒░ 
                                                                  
                                                                  
''')
time.sleep(3)
import PainterD2

if pub == 1:
    os.system('cls')
    import PbD2
elif kept == 1:
    os.system('cls')
    import KD2
   
os.system('cls')
print ("I didn't eat today.")
time.sleep(3)
print ("I can’t look at the pack of noodles in my cupboard the same")
time.sleep(3)
print ("so I threw it out")
time.sleep(3)
print ("It was probably expired")
time.sleep(2)
print ("I hope.")

time.sleep(4)
print ('''

░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░        ░▒▓██████▓▒░ ░▒▓██████▓▒░ ░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░          ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                       
                                                                                       
                                                            
''')
time.sleep(3)
import PainterDX
time.sleep(3)
print ('''
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░▒▓███████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░     ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░     ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░░▒▓██████▓▒░          ░▒▓████▓▒░  ░▒▓████▓▒░  ░▒▓████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                                                 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░                                                 
░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░             ░▒▓█▓▒░     ░▒▓█▓▒░     ░▒▓█▓▒░     
                                                                                     
                                                                                     
''')
time.sleep(5)
os.system('cls')
import PainterDZ

if pub == 1:
    os.system('cls')
    import PbD3
elif kept == 1:
    os.system('cls')
    import KD3

time.sleep(5)
os.system('cls')
import PainterDY

display_fight()
input = str(input("You decide to ")).lower()
while True:
    if input == "fight":
        os.system('cls')
        cv2.destroyAllWindows()
        print ("You run down the hallway in a fit of screams.")
        time.sleep(3)
        print ("It must’ve scared the intruder and forced them to run away.")
        break
    elif input == "run away":
        os.system('cls')
        cv2.destroyAllWindows()
        print("You can't run away.")
        os.system('cls')
        time.sleep(1)
        print ("You run down the hallway in a fit of screams.")
        time.sleep(3)
        print ("It must’ve scared the intruder and forced them to run away.")
        break

display_runafter()
final_choice = input("You know what to do. ").lower()
if final_choice == "run after them":
    os.system('cls')
    cv2.destroyAllWindows()
    print ("You run out the house,")
    time.sleep(3)
    print ("waving your arms wildly over your head.")
    time.sleep(3)
    print ("You feel the tip of the knife a few times and the feeling of blood,")
    time.sleep(3)
    print ("trickling down your arm.")

time.sleep(3)
os.system('cls')
display_cutscene("finalend.mp4")

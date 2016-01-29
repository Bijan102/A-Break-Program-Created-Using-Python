#Author                 -- Bijan Fazeli
#Program title          -- Break

#Import necessary modules
import time
import webbrowser
import tkMessageBox

#Create a counter variable called count and initialized it to 0
count = 0

#Time stamp when the program started
print("This program started on " + time.ctime())

#Create a while loop that will run the program 3 times after idling for 2 hours
while (count < 3):
    #Idle for 2 hrs
    time.sleep(2*60*60)
    #Display a message to the user that it is time to take a break
    tkMessageBox.showinfo(title="Break Time", message="Please stop what you are doing"
                          + " and enjoy this music video during your break, you have 10 mins.")
    #Idle for 5s post message box popup
    time.sleep(5)
    #Open default browser to the specified youtube link
    webbrowser.open("https://www.youtube.com/watch?v=emnTorIXVhk")
    #Idle for 10 mins, so that user can enjoy full 10 minutes of his/her break
    time.sleep(10*60)
    #Incr count by 1
    count += 1

import time
import webbrowser
import tkMessageBox

i = 0

print("This program started on " + time.ctime())
while (i < 3):
    time.sleep(2*60*60)
    tkMessageBox.showinfo(title="Break Time", message="Please stop what you are doing"
                          + " and enjoy this music video during your break, you have 10 mins.")
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=emnTorIXVhk")
    time.sleep(10*60)
    i = i + 1

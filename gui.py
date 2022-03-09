import tkinter as tk

#Create the window we will be working with
window = tk.Tk()
#Create the message log to hold all our said messages
messageLog = []
#Create a function to save what is typed into the submission bar
def handle_click(event):
    messageLog.append(typeEntry.get())
    typeEntry.delete(0,tk.END)

#Create two frames: main frame, to contain the chat log, and the type frame for entering new messages
mainFrame = tk.Frame(window,width=1500,height=400,relief=tk.GROOVE,borderwidth=5,bg="white")
typeFrame = tk.Frame(width=1000,height=50,relief=tk.GROOVE,borderwidth=5,bg="white")
mainFrame.pack()
typeFrame.pack()
#Set the main frame to not change shape automatically
mainFrame.pack_propagate(False)

#Create the entry widget for the user to enter in their responses
typeEntry = tk.Entry(master=typeFrame,width=100,highlightbackground="black",highlightthickness=1)
#Put 5 pixels between the entry line and the submission button to make space
typeEntry.pack(pady=5)
#Create a button labelled "Submit Response" for the user to press after writing their response
submitButton = tk.Button(master=typeFrame,text="Submit Response",bg="black",fg="white")
#Create a bind on the button for when it is clicked
submitButton.bind("<Button-1>", handle_click)
submitButton.pack()

#Function to update the chat log as it is written in
def update():
    #First remove everything in the frame already so that it is not duplicated
    for widget in mainFrame.winfo_children():
        widget.destroy()
    #Check if the length of messages is more than 18, as only 18 total messages can be displayed. If the length is greater than or equal to 18, delete messages till it is less than
    if len(messageLog) >= 18:
        diff = len(messageLog)-18
        for i in range(diff):
            del messageLog[0]
    #Go through each message in the message log and orient it left or right depending on which user said it
    for x in range(len(messageLog)):
        if x%2 == 0:
            newLabel = tk.Label(master=mainFrame,text=messageLog[x],bg="grey",fg="black")
            newLabel.pack(anchor="w")
        else:
            newLabel = tk.Label(master=mainFrame,text=messageLog[x],bg="blue",fg="white")
            newLabel.pack(anchor="e")
    #Call the update again after 100ms
    window.after(100,update)

#Call update
update()

#Create the window loop
window.mainloop()
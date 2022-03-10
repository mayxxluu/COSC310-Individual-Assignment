#Import all needed classes from the other files
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList
#Import tkinter to create the GUI
import tkinter as tk

#Create the window we will be working with
window = tk.Tk()
window.title("Helperbot 9000 Chat")

#Create global variable for state of conversation
conState = 0

#Create the message log to hold all our said messages
messageLog = []

#Create a function to save what is typed into the submission bar
def handle_click(event):
    global conState
    databaseInList = DatabaseToList.database_to_list()
    if conState == 0:
        userInput = typeEntry.get()
        messageLog.append([userInput,"user"])
        typeEntry.delete(0,tk.END)
        if(not userInput.replace(' ','').isalpha()):
            messageLog.append(["Please try again, remember to use only letters.","bot"])
        elif(len(userInput.split()) != 1):
            messageLog.append(["Please try again, remember to only use one word for the greeting.","bot"])
        else:
            messageLog.append([GettingStarted.gettingStarted(),"bot"])
            conState = 1
    elif conState == 1:
        userInputSentence = typeEntry.get()
        messageLog.append([userInputSentence,"user"])
        typeEntry.delete(0,tk.END)
        if((not userInputSentence.replace(' ','').isalpha()) or (len(userInputSentence) == 0) ):
            messageLog.append(["Please try again, remember to use only letters.","bot"])
        elif(len(userInputSentence.split())<=2):
            messageLog.append([GoodbyeMessage.goodbyeMessage(),"bot"])
            typeFrame.destroy()
            exitButton.pack()
        else:
            botAnswer,correctnessValue = BotRespons.bot_respons(userInputSentence,databaseInList)
            if correctnessValue > 1 or correctnessValue <= (1/3):
                messageLog.append(["I'm sorry, I cannot understand that sentence. Could you say it a little more simply please?","bot"])
            else:
                messageLog.append([botAnswer,"bot"])
            correctnessValue = 0

#Function to close the window
def closeWindow(event):
    window.destroy()

#Create two frames: main frame, to contain the chat log, and the type frame for entering new messages
mainFrame = tk.Frame(window,width=1250,height=400,relief=tk.GROOVE,borderwidth=5,bg="white")
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

#Create a button to close the window
exitButton = tk.Button(text="Exit Window",bg="black",fg="white")

#Create a bind on the button for when it is clicked
submitButton.bind("<Button-1>",handle_click)
submitButton.pack()

#Create a bind on the exit button for when it is clicked
exitButton.bind("<Button-1>",closeWindow)

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
        if messageLog[x][1] == "bot":
            newLabel = tk.Label(master=mainFrame,text=messageLog[x][0],bg="grey",fg="black")
            newLabel.pack(anchor="w")
        else:
            newLabel = tk.Label(master=mainFrame,text=messageLog[x][0],bg="blue",fg="white")
            newLabel.pack(anchor="e")
    #Call the update again after 100ms
    window.after(100,update)

#Call update to begin recursion
update()

#Begin the conversation between bot and user
messageLog.append([GreetMessage.greetMessage(),"bot"])

#Create the window loop
window.mainloop()
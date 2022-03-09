#Import all needed classes from the other files
from GreetMessage import GreetMessage
from GoodbyeMessage import GoodbyeMessage
from GettingStarted import GettingStarted
from BotRespons import BotRespons
from DatabaseToList import DatabaseToList
#Import tkinter to create the GUI
import tkinter as tk

class Main:
    ##SETTING UP GUI
    #Create the window we will be working with
    window = tk.Tk()
    #Create the message log to hold all our said messages
    messageLog = []
    #Create a function to save what is typed into the submission bar
    def handle_click(event):
        userMessage = Main.typeEntry.get()
        Main.messageLog.append(userMessage)
        Main.typeEntry.delete(0,tk.END)
        return userMessage
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
    submitButton.bind("<Button-1>",handle_click)
    submitButton.pack()
    #Function to update the chat log as it is written in
    def update():
        #First remove everything in the frame already so that it is not duplicated
        for widget in Main.mainFrame.winfo_children():
            widget.destroy()
        #Check if the length of messages is more than 18, as only 18 total messages can be displayed. If the length is greater than or equal to 18, delete messages till it is less than
        if len(Main.messageLog) >= 18:
            diff = len(Main.messageLog)-18
            for i in range(diff):
                del Main.messageLog[0]
        #Go through each message in the message log and orient it left or right depending on which user said it
        for x in range(len(Main.messageLog)):
            if x%2 == 0:
                newLabel = tk.Label(master=Main.mainFrame,text=Main.messageLog[x],bg="grey",fg="black")
                newLabel.pack(anchor="w")
            else:
                newLabel = tk.Label(master=Main.mainFrame,text=Main.messageLog[x],bg="blue",fg="white")
                newLabel.pack(anchor="e")
        #Call the update again after 100ms
        Main.window.after(100,Main.update)
    update()

    ##CREATE CONVERSATION BETWEEN USER AND BOT
    messageLog.append(GreetMessage.greetMessage())
    userInput = input("User: ")
    while((not userInput.replace(' ','').isalpha()) or (len(userInput.split()) == (not 1)) ):
        print("Bot: Please try again, remember to use only letters.")
        userInput = input("User: ")
    print(f"Bot: {GettingStarted.gettingStarted()}")
    userWantsToTalk = True
    databaseInList = DatabaseToList.database_to_list()
    while(userWantsToTalk):        
        userInputSentence = input("User: ")
        while((not userInputSentence.replace(' ','').isalpha()) or (len(userInputSentence) == 0) ):
            print("Bot: Please try again, remember to use only letters.")
            userInputSentence = input("User: ")
        if(len(userInputSentence.split())<=2):
            print(f"Bot: {GoodbyeMessage.goodbyeMessage()}")
            userWantsToTalk = False
        else:
            botAnswer,correctnessValue = BotRespons.bot_respons(userInputSentence,databaseInList)
            if correctnessValue > 1 or correctnessValue <= (1/3):
                print("Bot: I'm sorry, I cannot understand that sentence. Could you say it a little more simply please?")
            else:
                print(f"Bot: {botAnswer}")
            correctnessValue = 0
            
    #Create the window loop
    window.mainloop()
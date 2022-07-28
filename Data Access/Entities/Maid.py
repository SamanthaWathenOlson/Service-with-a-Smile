class Maid:

    def __init__(self, myfunct, change_dress, maid_id, maid_name, customer_id, read_message, send_message, message_star, message_delete):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.customer_id = customer_id
        self.read_message = read_message
        self.send_message = send_message

    def myFunct(self): #The maid will introduce herself.
        print("Hello, master. My name is " + maid_name)
    
    def changeDress(): #This will cause the maid to change into what dresses you have avilable for her.
        pass

    def readLetter(self): #This willread the letter to the customer.
        print("Your message says " + read_message)

    def sendLetter(self): #This will send the message to the person it is addressed too.
        print("I send this messaage to " + send_message)
        
    def starLetter(self): #This will place message in an archive.
        print("Shall I place a star on this message?")



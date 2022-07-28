class Maid:

    def __init__(self, maid_id, maid_name, my_funct, change_dress, customer_id, read_message, send_message, message_star, message_delete):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.my_funct = my_funct
        self.change_dress = change_dress
        self.customer_id = customer_id
        self.read_message = read_message
        self.send_message = send_message
        self.message_star = message_star
        self.message_delete = message_delete

    def getMaidId():
        pass
    
    def getCustomerId():
        pass
    
    def getMaidName():
        pass
   
    def myFunct(): #The maid will introduce herself.
        print("Hello, master. My name is " + maid_name)
    
    def changeDress(): #This will cause the maid to change into what dresses you have avilable for her.
        pass

    def readLetter(): #This willread the letter to the customer.
        print("Your message says " + read_message)

    def sendLetter(): #This will send the message to the person it is addressed too.
        print("I send this messaage to " + send_message)
        
    def starLetter(): #This will place message in an archive.
        print("Shall I place a star on this message?")



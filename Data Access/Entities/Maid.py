class Maid:

    def __init__(self, maid_id, maid_name, my_funct, change_dress, customer_id, read_letter, write_letter, send_letter, star_ letter, message_delete):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.my_funct = my_funct
        self.change_dress = change_dress
        self.customer_id = customer_id
        self.read_letter = read_letter
        self.write_letter = write_letter
        self.send_letter = send_letter
        self.star_letter = star_letter
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

    def writeLetter(): # This will write a letter to the recipient.
        pass

    def sendLetter(): #This will send the message to the person it is addressed too.
        print("I send this messaage to " + send_message)
        
    def starLetter(): #This will place message in an archive.
        print("Shall I place a star on this message?")

    def message_delete(): # This will delete the message.
        pass

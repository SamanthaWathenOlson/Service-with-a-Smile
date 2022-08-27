class Message:

    def __init__(self, read_letter, write_letter, send_letter, star_letter, message_delete):
        self.read_letter = read_letter
        self.write_letter = write_letter
        self.send_letter = send_letter
        self.star_letter = star_letter
        self.message_delete = message_delete

    def readLetter(self):  #This willread the letter to the customer.
        print("Your message says " + read_letter)

    def writeLetter(self):  #This will write a letter to the recipient.
        pass

    def sendLetter(self):  #This will send the message to the person it is addressed too.
        print("May I send this message to " + customer_name)

    def starLetter(self):  #This will place message in an archive.
        print("Shall I place a star on this message?")

    def message_delete(self):  #This will delete the message.
        pass


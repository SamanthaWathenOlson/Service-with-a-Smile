class Maid:

    def __init__(self, maid_id, maid_name, customer_id, read_message, send_message):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.customer_id = customer_id
        self.read_message = read_message
        self.send_message = send_message

    def myfunct(self):
        print("Hello, master. My name is" + maid_name)

    def readletter(self):
        print("Your message says" + read_message)

    def sendletter(self):
        print("Your message says" + send_message)



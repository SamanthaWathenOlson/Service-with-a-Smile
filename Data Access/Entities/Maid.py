class Maid:

    def __init__(self, maid_id: int, maid_name: str, customer_id: int, my_funct: str):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.customer_id = customer_id
        self.my_funct = my_funct

    def getMaidId(self):
        return {
            "maidId": self.maid_id
        }
    
    def getCustomerId(self):
        return {
            "customerId": self.customer_id
        }
    
    def getMaidName(self):
        return {
            "maidName": self.maid_name
        }
   
    def myFunct(self): #The maid will introduce herself. This will cover all the phrases she says. I will over load
        print("Hello, master. My name is " + maid_name)

    def myFunct(self): #The maid will introduce herself. This will cover all the phrases she says. I will over load
        print("Hello, master. It is such a nice day!")
    
    def changeDress(self): #This will cause the maid to change into what dresses you have avilable for her.
        pass



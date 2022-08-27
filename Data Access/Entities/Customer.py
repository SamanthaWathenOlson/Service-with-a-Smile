class Customer:

    def __init__(self, maid_id: int, maid_name: str, change_dress: str, customer_name: str, customer_id: int):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.change_dress = change_dress
        self.customer_name = customer_name
        self.customer_id = customer_id
    
    def findMaidId(self):
        return {
            "maidId": self.maid_id
                 }
   
    def findMaidName(self):
        return {
            "maidName": self.maid_name
        }
    
    def maidName(self):
        print("Please input my new name: " + maid_name)

    def findCustomerId(self):
        return {
            "customerId": self.customer_id
        }

    def findCustomerName():
        return {
            "customerName": self.customer_name
        }

    
    

    





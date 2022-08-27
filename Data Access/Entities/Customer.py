class Customer:

    def __init__(self, maid_id: int, maid_name: str, change_dress: str, customer_name: str, customer_id: int):
        self.maid_id = maid_id
        self.maid_name = maid_name
        self.change_dress = change_dress
        self.customer_name = customer_name
        self.customer_id = customer_id
    
    def find_maid_id(self):
        return {
            "maidId": self.maid_id
                 }
   
    def find_maid_name(self):
        return {
            "maidName": self.maid_name
        }
    
    def create_maid_name(self):
        print("Please input my new name: " + self.maid_name)

    def find_customer_id(self):
        return {
            "customerId": self.customer_id
        }

    def find_customer_name(self):
        return {
            "customerName": self.customer_name
        }

    
    

    






   class BankUser:
    def __init__(self, user_name, password, bank):
        #save users user_name hellloo
        self.user_name = user_name
        #save users password
        self.__password = password
        #save the bank the user belongs to
        self.bank = bank
        #call create user that will add the user to the bank database
        self.__create_user(bank)
    
    def __create_user(self, bank):
        bank.create_user(self.user_name, self.__password) #this is automatically added #since bank data is aprivate variable we arent able to call it here
        """
        TODO: complete this function that adds the current user to the bank database
        """
        ...
    
    def check_balance(self):#self is the bank user its the object we're refering to.
        """
        TODO: complete this function that returns the balance of the current user
        """
        
        return self.bank.get_balance(self.user_name , self.__password)#literally break down the code
    
    def deposit(self, amount):
        if amount <= 0:
            print("invalid amount")
        else:
            print("Deposite Valid")
        self.bank.deposit(self.user_name, self.__password, amount)#same logic as above
            
        """
        TODO: complete this function that deposits money into the current users account
        """
        
        ...
    
    def withdraw(self, amount):
        self.bank.withdraw(self.user_name, self.__password,-1* amount)
        """
        TODO: complete this function that 
        """

class ATM:
    def __init__(self,atmCard,pinNumber):
        self.atmCard=atmCard
        self.pinNumber=pinNumber  

    def bankEnquiry(self):     
        print("Your current balance is ₹50,000")
        
    def amountAfterWithdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn this amount : "+str(amount) +". Your remaining balance is this amount : "+ str(new_amount))

def main():
    card_no=input("Insert your Card Number here :  ")
    pin_no=input("Insert your Pin Number here :  ")
    new_user=ATM(card_no,pin_no)
    print("Which of the following activity do you want to do ? : ")
    print("1. Balance Enquriy(Press 1)  2. Withdrawl(Press 2)")
    activity=int(input("Enter your activity :- "))
        
    if (activity == 1):
        new_user.bankEnquiry() 
    elif (activity == 2):
        amount = int(input("Enter the amount which you wish to withDraw : "))
        new_user.amountAfterWithdrawl(amount)    
    else:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
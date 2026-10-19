expenses = []

def add_expense():
    try:
        amount = int(input("enter the amount:"))
    except ValueError:
        print("Please enter a valid number!")
        return
    if amount <=0:
        print("Amount must be greater than zero.")
        return
    category = input("Enter the category:")
    desc = input("Enter the description to remeber:")
    expenses.append({"amount":amount, "category":category, "description":desc})
    
def show_expenses():
    for expense in expenses:
        for key, value in expense.items():
            print(f"{key}: {value}")
        print()
            
def calculate_total(expenses):
    amount=0
    for expense in expenses:
        amount +=expense["amount"]
    return amount
    
    
while(True):
    print(f"""
          {"="*6} EXPENSE TRACKER {"="*6}
          1. Add Expense
          2. show all expenses
          3. calculate total spending
          4. exit
          """)
    try:
        user = int(input("enter the option you want to perform!:"))
        if user == 1:
            add_expense()
        elif user == 2:
            if (expenses == []):
                print("add your expenses first!")
            else:
                show_expenses()
        elif user == 3:
            a=calculate_total(expenses)
            
            if not expenses:
                print("add your expenses first ")
            else:
                print(f"total money spent: {a} ")
            
        elif user == 4:
            break
        
        else:
            print("Please choose an option between 1 and 4.")
      
    except ValueError:
        print("Enter a valid integer")




import json
#class to store the expenses and display them
class Expense:
    def __init__(self,amount,category,description):
        self.amount = amount
        self.category = category
        self.description = description
        
    def display(self):
        print(f"amount: {self.amount}\ncategory: {self.category}\ndescription: {self.description}\n" )
        
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
               
    def add_expense(self, expense):
        self.expenses.append(expense)
        
        
    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        
        for  expense in self.expenses:
            expense.display()
            print("-" * 25)
            
    def calculate_total(self):
        total = 0
        for i in self.expenses:
                total += i.amount
        return total   
#DAY_3     
    def save_expenses(self):
            list_objects = []
            for expense in self.expenses:
                expense_data = {"amount": expense.amount, "category": expense.category, "description":expense.description}       
                list_objects.append(expense_data)
               
            with open("expenses.json","w") as f:
                json.dump(list_objects,f, indent=2)
                
                
    
#DAY_3        
def main():
    tracker = ExpenseTracker()
    
    while(True):
        print(f"{"="*5} EXPENSE TRACKER {"="*5}") 
        print("1. Add Expense")          
        print("2. show Expense")          
        print("3. Calculate Total")         
        print("3. Save Expenses")         
        print("5. Exit")         
        
        choice = int(input("Enter your choice: "))
                
        if choice == 1:
            try:
                amount = float(input("Enter amount: "))
                
                if amount <= 0:
                    print("Amount must be greater than zero.")
                    continue
                
                category = input("Enter Category: ")
                description = input("Enter Description: ")
                
                expense = Expense(amount, category, description)
                tracker.add_expense(expense)
                
                print("Expense added successfuly!")
                
            except ValueError:
                print("Please enter a valid numeric amount.")
        
        elif choice == 2:
            tracker.show_expenses()
            
        elif choice == 3:
            total = tracker.calculate_total()
            print(f"Total expenses: {round(total,2)}") 
            
        elif choice == 4:
            tracker.save_expenses()
            
        elif choice == 5:
            print("Thank you for using Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, or 5 .")
            
if __name__ == "__main__":
    main() 
# tracker = ExpenseTracker()

# expense1 = Expense(250, "Food", "Lunch")
# expense2 = Expense(150, "Recharge", "Metro card")
# expense3 = Expense(550, "Recharge", "Mobile-recharge")

# tracker.add_expense(expense1)
# tracker.add_expense(expense2)
# tracker.add_expense(expense3)

# tracker.show_expenses()
# print("Total spending:", tracker.calculate_total())
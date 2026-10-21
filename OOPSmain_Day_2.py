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
        self.save_expenses()
        
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
    
    
tracker = ExpenseTracker()

expense1 = Expense(250, "Food", "Lunch")
expense2 = Expense(150, "Recharge", "Metro card")
expense3 = Expense(550, "Recharge", "Mobile-recharge")

tracker.add_expense(expense1)
tracker.add_expense(expense2)
tracker.add_expense(expense3)

tracker.show_expenses()
print("Total spending:", tracker.calculate_total())
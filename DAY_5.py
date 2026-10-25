import json
import math
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
        self.save_expenses() #DAY4 after every expense added successfully it is also saved
        
        
    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        #DAY4 : updated the show_expense method to store index value also
        for index, expense in enumerate(self.expenses):
            print(f"\nIndex: {index}")
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
                
#DAY_4    
    # to load the data from json back to the pyton list so that json data doesn't get overwritten
    def load_expenses(self):
            try:
               with open("expenses.json","r") as f:
                          data = json.load(f)
            except FileNotFoundError:
                print("No saved expenses found. Starting with an empty list.")  
                return 
            #this block is for code error in json. if json data is not properly stored or error in syntax this code block will handle
            except json.JSONDecodeError:
                print("Error: expenses.json contains invalid JSON") 
                print("The existing files has not been changed.")
                return 
            #this loop helps the json data convert into the object again and stored in the list
            for expense_data in data:
                data_obj = Expense(expense_data["amount"], expense_data["category"], expense_data["description"])
                self.expenses.append(data_obj)
                
            print("Expenses loaded successfully.") 
                       
    # this function lets user apply filter according to the category and let them see the total spent on that category            
    def filter_by_category(self, category):
            filtered_expenses = []
            #this loop lets appends the matching category in the filtered_Expenses list
            for expense in self.expenses:
                if expense.category == category:
                    filtered_expenses.append(expense)
                  
            return filtered_expenses
        
    #this function lets user delete the expense based on the index     
    def delete_expense(self,index):
        if index not in range(0,len(self.expenses)):
            print(f"the index must be greater than or equal to 0\nand less than {len(self.expenses)}")
        else:
            self.expenses.pop(index)
            self.save_expenses()
            print(f"Expense on index {index} has been deleted successfully!")  
    #DAY_5
    #this function is made so that our code repetetion will be less and we can directly use this where needed          
    def get_Valid_amount(self, prompt="Enter Amount: "):
            while True:
                try:
                    amount = float(input(prompt)) 
                    
                    if not math.isfinite(amount):
                        print("Amount must be a finite number.")
                        continue
                    
                    if amount <= 0:
                        print("Amount must be greater than zero.")
                        continue
                    return amount
                except ValueError:
                    print("Please enter a valid numeric amount.")
         #helper funciton           
    def get_non_empty_text(self,prompt):
        while True:
            value = input(prompt).strip()
            
            if value:
                return value
            
            print("This field cannot be empty.")
            #let user edit expenses at index level
    def edit_expense(self, index):
            if index not in range(0,len(self.expenses)):
                print(f"the index must be greater than or equal to 0\nand less than {len(self.expenses)}")
            else:
                expense =  self.expenses[index]
                while(True):
                    print(f"{"="*5} EXPENSE EDITOR {"="*5}") 
                    print("1. Update Amount")          
                    print("2. Update Category")          
                    print("3. Update Description")          
                    print("4. Update ALL")
                    print("5. Exit")
                    
                    choice = input("Choose an option: ")
                    
                    if choice == "1":                    
                        expense.amount = self.get_Valid_amount("Enter new Amount: ")
                        self.save_expenses()
                        print("Amount updated successfully!")
    
                    elif choice == "2":
                        expense.category = self.get_non_empty_text("Enter new category: ").lower()
                        self.save_expenses()
                        print("Category updated successfully!")
    
                    elif choice == "3":
                        expense.description = self.get_non_empty_text("Enter new description: ")
                        self.save_expenses()
                        print("Descriotion updated successfully!")
    
                    elif choice == "4":
                        expense.amount = self.get_Valid_amount("Enter new Amount: ")                        
                        expense.category = self.get_non_empty_text("Enter new category: ").lower()
                        expense.description = self.get_non_empty_text("Enter new description: ")
                            
                        self.save_expenses()
                        print("Updated Successfully!!")
                                           
                    elif choice == "5":
                        print("Exiting expense editor...")
                        break
                    else:
                        print("Enter valid choice: 1,2,3,4 or 5")
    def category_summary(self):
            category_totals = {}
            for expense in self.expenses:
                if expense.category in category_totals:
                    category_totals[expense.category] += expense.amount
                else:
                    category_totals[expense.category] = expense.amount
                    
            if not category_totals:
                print("No expenses available.")
                return
            
            print(f"{"-"*5} CATEGORY-WISE SUMMARY {"-"*5}")
            
            for category, total in category_totals.items():
                print(f"{category}: ₹{round(total,2)}")
            
            
            highest_category = max(category_totals,key=category_totals.get)
            print(f"Highest-spending category is {highest_category}: {category_totals[highest_category]}")
            
#DAY_3        
def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()
    
    while(True):
        print(f"{"="*5} EXPENSE TRACKER {"="*5}") 
        print("1. Add Expense")          
        print("2. show Expense")          
        print("3. Calculate Total")  
        print("4. Filter by Category")
        print("5. Delete at index")  
        print("6. Edit Expense")
        print("7. Category-wise Summary")             
        print("8. Exit")         
        
        choice = int(input("Enter your choice: "))
                
        if choice == 1:
                    
            amount = tracker.get_Valid_amount("Enter Amount: ")
            category = tracker.get_non_empty_text("Enter category: ").lower()
            description = tracker.get_non_empty_text("Enter description: ")
            
            expense = Expense(amount, category, description)
            tracker.add_expense(expense)
            
            print("Expense added successfuly!")
        
        elif choice == 2:
            tracker.show_expenses()
            
        elif choice == 3:
            total = tracker.calculate_total()
            print(f"Total expenses: {round(total,2)}") 
        #DAY4    
        elif choice == 4:
                    cat = input("Enter your category to filter out: ").lower().strip()
                    filtered_expenses = tracker.filter_by_category(cat)
                    
                    if not filtered_expenses:
                        print("No expenses found in this category.")
                    else:
                        for expense in filtered_expenses:
                            expense.display()
                            print("-" * 25)
                    #calculat total category wise
                    total_spent = 0    
                    for i in filtered_expenses:
                        total_spent += i.amount
                    print(f"\nTotal spent on {cat} :{total_spent}")
                    
                        
        elif choice == 5:
            tracker.show_expenses()
            
            if not tracker.expenses:
                continue  
            try:
                ind = int(input("Enter the index you want to delete: "))
                tracker.delete_expense(ind)
            except ValueError:
                print("please enter a valid integer index.")
        #DAY_5    
        elif choice == 6:
            tracker.show_expenses()
            
            if not tracker.expenses:
                continue
            
            try:
                ind = int(input("Enter the index you want to edit: "))
                tracker.edit_expense(ind)
            except ValueError:
                print("please enter a valid integer index.")
                
        elif choice == 7:
            tracker.category_summary()
                       
        elif choice == 8:
            print("Thank you for using Expense Tracker!")
            break
        
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, 7, or 8 .")
            
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
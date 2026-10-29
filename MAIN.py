import json
import math
from datetime import date
#class to store the expenses and display them
class Expense:
    def __init__(self,amount,category,description, expense_date=None):
        self.amount = amount
        self.category = category
        self.description = description
        #day_7
        if expense_date is None:
            self.date = date.today().isoformat()
        else:
            self.date = expense_date
        
    def display(self):
        print(f"amount: {self.amount}\ncategory: {self.category}\ndescription: {self.description}\ndate: {self.date}" )
 
        
#ExpenseTracker class to add,show,calculate total, save expenses in json file and to load back objects after the code is terminated and recalled
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        #we can add load_expenses() here but if we dont want to store all the values in the new tracker we wont do it.
        self.budgets = {} #day_7
        
    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()
        
    def show_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        
        for index, expense in enumerate(self.expenses):
            print(f"\nIndex: {index}")
            expense.display()
            print("-" * 25)
            
    def calculate_total(self):
        total = 0
        for i in self.expenses:
                total += i.amount
        return total
    
    def save_expenses(self):
        list_objects = []
        for expense in self.expenses:                                                                                  #day_7
            expense_data = {"amount": expense.amount, "category": expense.category, "description":expense.description, "date":expense.date}       
            list_objects.append(expense_data)
        try:   #day_7
            with open("expenses.json","w") as f:
                json.dump(list_objects,f, indent=2)
        except PermissionError:
            print("Python doesn't have permission to access this file")
            return
        except OSError:
            print("File system error occurs, check your path or directory!")
            return
                
    def load_expenses(self):
        try:
           with open("expenses.json","r") as f:
                      data = json.load(f)
        except FileNotFoundError:
            print("No saved expenses found. Starting with an empty list.")  
            return 
        
        except json.JSONDecodeError:
            print("Error: expenses.json contains invalid JSON") 
            print("The existing files has not been changed.")
            return 
        
        except PermissionError: #day_6
            print("Python doesn't have permission to access this file")
            return
        except OSError: #day_6
            print("File system error occurs, check your path or directory!")
            return
        if not isinstance(data, list): #day_6
            print("Invalid expense data format.")
            return
        loaded_count = 0
        skipped_count = 0
        for expense_data in data:
            #Day_6
            if not isinstance(expense_data, dict):
                print("Skipping invalid expense record not a dictionary.")
                skipped_count += 1
                continue

            required_keys = ("amount", "category", "description")

            if not all(key in expense_data for key in required_keys):
                print("Skipping expense with missing fields.")
                skipped_count += 1
                continue
            
            amount = expense_data["amount"]
            if isinstance(amount, bool) or not isinstance(amount, (int, float)):
                print("Amount must be a number.")
                continue
            #if someone added a very large int in amount to handle that
            try:
                finite_amount = math.isfinite(amount)
            except OverflowError:
                finite_amount = False

            if not finite_amount:
                print("skipping expense: Amount must be a finite number.")
                skipped_count +=1
                continue
            if amount <= 0:
                print("skipping expense: Amount must be greater than zero.")
                skipped_count +=1
                continue
            
            category = expense_data["category"]
            description = expense_data["description"]
            
            if not isinstance(category, str) or not category.strip():
                print("skipping expense: category must be non-empty text.")
                skipped_count +=1
                continue
            
            if not isinstance(description, str) or not description.strip():
                print("skipping expense: description must be non-empty text.")
                skipped_count +=1
                continue
            #to load cleaner version of them in memmory
            category = category.strip().lower()
            description = description.strip()
            
            #day_7
            expense_date = expense_data.get("date")
            data_obj = Expense(amount, category, description, expense_date)
            self.expenses.append(data_obj)
            loaded_count +=1
            
        print(f"loaded {loaded_count} expenses.")
        print(f"skipped {skipped_count} invalid records.")
        
    def filter_by_category(self, category):
        filtered_expenses = []
        
        for expense in self.expenses:
            if expense.category == category:
                filtered_expenses.append(expense)
              
        return filtered_expenses
    
    def delete_expense(self,index):
        if index not in range(0,len(self.expenses)):
            print(f"the index must be greater than or equal to 0\nand less than {len(self.expenses)}")
        else:
            self.expenses.pop(index)
            self.save_expenses()
            print(f"Expense on index {index} has been deleted successfully!")
    #helper function
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
        
        #Day_6
        highest_category = max(category_totals,key=category_totals.get)
        print(f"Highest-spending category is {highest_category}: {category_totals[highest_category]}")
              
        
    def show_dashboard(self):
        if not self.expenses:
            print("You need to add expenses first!")
            return
        print(f"{"="*5} EXPENSE DASHBOARD {"="*5}")
        total_spending = self.calculate_total()
        total_expenses = len(self.expenses)
        print(f"Total spending : ₹{total_spending}")
        print(f"Total Expenses : {total_expenses}")
        average_spending = round(total_spending / total_expenses,2)
        print(f"Your average spending is : ₹{average_spending}")
        self.category_summary()
    #day_7    
    def monthly_summary(self, year, month):
        month_prefix = f"{year}-{month:02d}"
        total = 0
        for expense in self.expenses:
            if expense.date.startswith(month_prefix):
                total += expense.amount
            
        return total
    
    #helper fucntion #day_8
    def validate_budget(self, year, month, amount):
        if not isinstance(year, int) or isinstance(year, bool) or not 1900 <= year <= 9999:
            print("Enter a valid year.\n")
            return False

        if not isinstance(month, int) or isinstance(month, bool) or not 1 <= month <= 12:
            print("Month must be between 1 and 12.\n")
            return False

        if isinstance(amount, bool) or not isinstance(amount, (int, float)):
            print("Budget must be a valid number.\n")
            return False

        if not math.isfinite(amount) or amount <= 0:
            print("\nBudget must be finite and greater than zero.\n")
            return False

        return True
               
    def set_monthly_budget(self, year, month, amount):
        if not self.validate_budget(year, month, amount):
            return
             
        month_key = f"{year}-{month:02d}"
        self.budgets[month_key] = amount

        print(f"Budget set for {month_key}: ₹{amount}")
        self.save_budgets()
           
       
         
    def save_budgets(self):
        try:
            with open("budgets.json", "w") as f:
                json.dump(self.budgets, f, indent =2)
            
            print("Budgets save successfully.")
        except OSError:
            print("Could not save budgets. Check the file path or permissions.")
                
    def load_budgets(self):
        try:
            with open("budgets.json", "r") as f:
                loaded_budgets = json.load(f)
            
            if not isinstance(loaded_budgets, dict):
                print("Indvalid budget file format.")
                return
            
           
            #day_8
            skip_load = 0
            successfull_load = 0
            valid_budgets = {}
            for month_key, amount in loaded_budgets.items():
                if not isinstance(month_key, str):
                    skip_load +=1
                    continue
                    
                try:
                    year_text, month_text = month_key.split("-")
                    year = int(year_text)
                    month = int(month_text)
                except ValueError:
                    print(f"skipping the malformed keys:{month_key}\n")
                    skip_load +=1
                    continue
                if not self.validate_budget(year, month, amount):
                    print(f"skipping invalid budget:{month_key}\n")
                    skip_load +=1
                    continue
                valid_budgets[month_key] = amount
                successfull_load += 1
            self.budgets = valid_budgets
                    
            print(f"Budgets skipped: {skip_load}.")
            print(f"Budgets loaded: {successfull_load} successfully.")
        
        except FileNotFoundError:
            print("No saved budgets found starting with an empty budget list.")
            
        except json.JSONDecodeError:
            print("The budget file contains invalid JSON.")

        except PermissionError:
            print("Python does not have permission to read the budget file.")

        except OSError:
            print("A file system error occurred while loading budgets.")
                
    
    def check_monthly_budget(self, year, month):
        month_key = f"{year}-{month:02d}"

        if month_key not in self.budgets:
            print("No budget set for this month.")
            return

        budget = self.budgets[month_key]
        spent = self.monthly_summary(year, month)

        remaining = budget - spent

        percentage = round((spent / budget) * 100,2)

        print(f"Monthly budget: ₹{budget}")
        print(f"Total spent: ₹{spent}")
        print(f"Remaining: ₹{remaining}")
        print(f"Budget used: {percentage:.2f}%")

        #warning for the user
        if spent >= 0.8*budget :
            print(f"Warning: spending reaches {percentage}% of the budget.!")
        if spent > budget:
            print("Warning: You have exceeded your monthly budget!")
        
           
            
            
            
                        
                                               
def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()
    tracker.load_budgets()
    
    while(True):
        print(f"{"="*5} EXPENSE TRACKER {"="*5}") 
        print("1. Add Expense")          
        print("2. show Expense")          
        print("3. Calculate Total")          
        print("4. Filter by Category")
        print("5. Delete at index")
        print("6. Edit Expense")
        print("7. Category-wise Summary")
        print("8. Show_dashboard")
        print("9. Set Budget")
        print("10. Monthly summary")
        print("11. Check monthly_Budget")
        print("12. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            
            amount = tracker.get_Valid_amount("Enter Amount: ")
            category = tracker.get_non_empty_text("Enter category: ").lower()
            description = tracker.get_non_empty_text("Enter description: ")
            
            expense = Expense(amount, category, description)
            print(expense.date) #day_8
            tracker.add_expense(expense)
            
            print("Expense added successfuly!")
                   
        elif choice == 2:
            tracker.show_expenses()
            
        elif choice == 3:
            total = tracker.calculate_total()
            print(f"Total expenses: {round(total,2)}")
        
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
            tracker.show_dashboard()
            
        elif choice == 9:
            year = int(input("Enter year in format -YYYY- :"))
            month = int(input("Enter month in format -MM-(1-12) :"))
            amount = tracker.get_Valid_amount("Enter Amount: ")
            tracker.set_monthly_budget(year,month,amount)
                                
        elif choice == 10:
            year = int(input("Enter year in format -YYYY- :"))
            month = int(input("Enter month in format -MM-(1-12) :"))
            monthly_spending = tracker.monthly_summary(year, month)
            print(f"Total spending for {year}/{month}: ₹{monthly_spending}")
            
         
        
        elif choice == 11:
            year = int(input("Enter year in format -YYYY- :"))
            month = int(input("Enter month in format -MM-(1-12) :"))
            tracker.check_monthly_budget(year,month)    
        
        elif choice == 12:
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 or 12.")  
            
if __name__ == "__main__":
    main()               
   
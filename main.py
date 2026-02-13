import sys
from datetime import datetime

class Expense:
    def __init__(self):
        date = datetime.now().strftime("%Y/%m/%d")

        self.id = 0
        self.date = date
        self.expense = []
    
    def add(self, amount, description):
        new_record = {}
        self.id += 1
        if not description:
            description = ""
        new_record.update({"id": self.id, "date": datetime.now(), "description": description, "amount": float(amount)})
        self.expense.append(new_record)
        return f"Expense add successfully (ID: {self.id})"

    def list(self):
        print("ID:\t Date:\t Description:\t Amount:")
        for record in self.expense:
            print(f"{record["id"]} \t{record["date"].strftime("%Y/%m/%d")}\t {record["description"]}\t  {record["amount"]}")
    
    
    def update(self, id, new_amount, new_desc):
        for record in self.expense:
            if record["id"] == id:
                record["amount"] = new_amount
                record["description"] = new_desc
                return f"Expense at id: {id} updated successfully"

        return "Record not exist"
    
    def delete(self, id):
        for record in self.expense:
            if record["id"] == id:
                self.expense.remove(record)
                return f"Expense at id: {id} deleted successfully"
        return "Record not exist"
            
    def summary(self):
        total_expense = sum(amount.get("amount", 0) for amount in self.expense)
        return f"Total expenses: ${total_expense}"

    def monthly_summary(self, month_num):
        month_num = int(month_num) 
        result = sum(record["amount"] for record in self.expense if record["date"].month == month_num)
        return f"Total expenses: ${result}"


def main():
    expense = Expense()
    print("="*15 + "EXPENSE TRACKING PROGRAM" + "="*15)
    print("Enter 'exit' or 'quit' to escape")

    while True:
        user_input = input("expense-tracker: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            sys.exit()
        
        command = user_input.split()
        if not command:
            continue

        if command[0] == "add":
            desc_index = command.index("--description") + 1
            amount_index = command.index("--amount") + 1
            description = command[desc_index]
            amount = command[amount_index]
            print(expense.add(amount, description))
        
        elif command[0] == "update":
            id_index = command.index("--id") + 1
            amount_index = command.index("--amount") + 1
            if "--description" in command:
                desc_index = command.index("--description") + 1
            else:
                description = ""
            id = int(command[id_index])
            updated_amount = command[amount_index]
            updated_desc = command[desc_index]

            print(expense.update(id, updated_amount, updated_desc))

        elif command[0] == "delete":
            id_index = command.index("--id") + 1
            id = int(command[id_index])
            print(expense.delete(id))
        
        elif command[0] == "list":
            print(expense.list())

        elif command[0] == "summary":
            if "--month" in command:
                month_summary_index = command.index("--month") + 1
                month_summary = command[month_summary_index]
                print(expense.monthly_summary(month_summary))
            else:
                print(expense.summary())

        else: 
            print("Invalid command")

        print("="*30)

if __name__ == "__main__":
    main()

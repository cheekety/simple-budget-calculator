import tkinter as tk

class MainWindow:
    def __init__(self):
        self.root = tk.Tk() # Initiate new tkinter object
        self.root.geometry("920x540") # Set dimension size
        self.root.resizable(width=False, height=False) # Lock app dimension
        self.root.title("Budget Tool") # Window title
        self.style = ('Monospace', 18)
        self.draw('Welcome to the Budget App!\n\nThis calculator uses the 5:3:2 rule of spending by default.\n\nPlease enter your budget to continue...')
        self.buttons()
        self.root.mainloop() # Keep UI alive

###############
#   WIDGETS   #
###############

    def draw(self, msg):
        self.frameText = tk.Frame(self.root, height=19, width=50)
        self.textBox = tk.Text(self.frameText, height=19, width=50, relief='flat', bg='light yellow', font=self.style)
        self.textBox.insert(1.0, msg)
        self.textBox.config(state='disabled')
        self.frameText.grid(row=0, column=0)
        self.textBox.pack(padx=3, pady=3)

    def buttons(self):
        self.frame = tk.Frame(self.root, height=1, width=50)
        self.frame.grid(row=0, column=1)
        self.label = tk.Label(self.frame, text='Your Budget:')
        self.entry = tk.Entry(self.frame, font=12)
        self.calBudget = tk.Button(self.frame, text='Calculate Budget', command=self.calculateBudget, width=20)
        self.viewBudget = tk.Button(self.frame, text='View Budget Plan', command=self.viewBudgetPlan, width=20)
        self.viewSpending = tk.Button(self.frame, text='View Spending Budget', command=self.popUp, width=20)
        items = [self.label, self.entry, self.calBudget, self.viewBudget, self.viewSpending]
        for item in items: item.pack(padx=10, pady=20)

    def popUp(self):
        self.popUp = tk.Tk()
        self.popUp.geometry("200x200")
        self.popUp.title("Rent & Bills")
        self.popUp.resizable(width=False, height=False)
        self.rentLabel = tk.Label(self.popUp, text="Rent/Mortgage:")
        self.rentEntry = tk.Entry(self.popUp, width=25)
        self.billsLabel = tk.Label(self.popUp, text="Total Monthly Bills:")
        self.billsEntry = tk.Entry(self.popUp, width=25)
        self.done = tk.Button(self.popUp, text='Done', command=self.calculateSpending)
        items = [self.rentLabel, self.rentEntry, self.billsLabel, self.billsEntry, self.done]
        for item in items: item.pack(pady=5)

#################
#   FUNCTIONS   #
#################

    def calculateBudget(self):
        self.budget = float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.draw(f"Total Budget: ${'{:.2f}'.format(self.budget)}\nSpending Money: ${'{:.2f}'.format(self.spending)}")
    
    def viewBudgetPlan(self):
        self.budget = float(self.entry.get() or 0)
        self.spending = self.budget * 0.5
        self.savings = self.budget * 0.3
        self.extra = self.budget - self.spending - self.savings
        self.draw(f"Total Budget\t\t: ${'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ${'{:.2f}'.format(self.spending)} \
            \nTo Save\t\t: ${'{:.2f}'.format(self.savings)}\nExtra\t\t: ${'{:.2f}'.format(self.extra)}")

    def calculateSpending(self):
        self.rent = float(self.rentEntry.get() or 0)
        self.bills = float(self.billsEntry.get() or 0)
        self.popUp.destroy()
        self.budget = float(self.entry.get() or 0)
        self.food = (self.budget * 0.5) - self.rent - self.bills
        self.draw(f"### TOTAL BUDGET ###\nTotal\t\t: ${'{:.2f}'.format(self.budget)}\nSpending Money\t\t: ${'{:.2f}'.format(self.budget*0.5)} \
            \n\n### EXPENSES ###\nRent\t\t: ${'{:.2f}'.format(self.rent)}\nBills\t\t: ${'{:.2f}'.format(self.bills)}\nFood\t\t: ${'{:.2f}'.format(self.food)}")

if __name__ == '__main__':
    MainWindow()
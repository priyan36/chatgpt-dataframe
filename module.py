import random
import pandas as pd

class bank:
    def _init_(self):
        self.data = [["Suresh", 123, 2000, 5000], ["Raina", 124, 400, 1000], ["Virat", 125, 6000, 2000]]
        self.trans = pd.DataFrame(columns=["AccNo", "Transaction Type", "Amount"])
        self.creditscr = pd.DataFrame(columns=["AccNo", "Credit", "Membership"])

    def chkbal(self, accno):
        for i in self.data:
            if i[1] == accno:
                print("Your Bal: ", i[2])
                return
        print("Invalid AccNO")

    def create(self, name, bal, fd):
        accno = self.data[-1][1] + 1
        new = [name, accno, bal, fd]
        self.data.append(new)
        print("Name: ", name)
        print("AccNo: ", accno)
        print("Balance: ", bal)
        print("Fixed Dep: ", fd)
        print("Your Account Created")

    def deposit(self, accno, depamt):
        idx = None
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break

        if idx is None:
            print("Invalid Account No.")
            return

        if depamt > 100000:
            pan = input("Enter Pan No.: ")
            if len(pan) != 5:
                print("Invalid Pan")
                return

        self.data[idx][2] += depamt
        print("Your Balance: ", self.data[idx][2])
        self.trans = self.trans.append({
            "AccNo": accno,
            "Transaction Type": "Deposit",
            "Amount": depamt
        }, ignore_index=True)

        nooftrans = self.trans[self.trans["AccNo"] == accno]["AccNo"].count()
        if nooftrans == 0:
            self.creditscr = self.creditscr.append({
                "AccNo": accno,
                "Credit": 10,
                "Membership": "None"
            }, ignore_index=True)
        else:
            crdpts = nooftrans * 10
            if crdpts < 50:
                memship = "None"
            elif crdpts >= 50:
                memship = "Silver"
            elif crdpts >= 100:
                memship = "Gold"
            elif crdpts >= 150:
                memship = "Diamond"
            self.creditscr = self.creditscr.append({
                "AccNo": accno,
                "Credit": crdpts,
                "Membership": memship
            }, ignore_index=True)

    def withdraw(self, accno, witamt):
        idx = None
        for i in self.data:


#File "c:\Users\priya\Desktop\VS Code\chatgpt\module.py", line 77, in withdraw
    #for i in self.data:
             #^^^^^^^^^
#AttributeError: 'bank' object has no attribute 'data'

            if i[1] == accno:
                idx = self.data.index(i)
                break

        if idx is None:
            print("Invalid Account No.")
            return

        if witamt > self.data[idx][2]:
            print("Insufficient Fund.")
        else:
            self.data[idx][2] -= witamt
            print("Your Balance: ", self.data[idx][2])
            self.trans = self.trans.append({
                "AccNo": accno,
                "Transaction Type": "Withdraw",
                "Amount": -witamt
            }, ignore_index=True)

    def fd(self, accno, fdamt, yrs):
        idx = None
        for i in self.data:
            if i[1] == accno:
                idx = self.data.index(i)
                break

        if idx is None:
            print("Invalid Account No.")
            return

        if fdamt > 50000:
            rtn = (10000 * yrs) + self.data[idx][3]
            print("Your Return is: ", rtn)
        else:
            print("FD should be above Rs.50000.")

    def transaction(self):
        print(self.trans)


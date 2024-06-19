from module import bank

bank = bank()

while True:
    serv = int(input("Service Provided:\n1. Acc Creation\n2. Deposit\n3. Withdraw\n4. Fixed Deposit\n5. Exit\n"))
    if serv == 1:
        name = input("Enter Name: ")
        bal = int(input("Enter Deposit Amt: "))
        fd = int(input("Enter FD Amt: "))
        bank.create(name, bal, fd)
    elif serv == 2:
        accno = int(input("Enter Accno: "))
        isacc = False
        for i in bank.data:
            if i[1] == accno:
                isacc = True
                break
        if isacc:
            depamt = int(input("Enter Deposit amt: "))
            bank.deposit(accno, depamt)
        else:
            print("Invalid Account No.")
    elif serv == 3:
        accno = int(input("Enter Accno: "))
        witamt = int(input("Enter Withdraw Amount: "))
        bank.withdraw(accno, witamt)

    #Traceback (most recent call last):
  #File "c:\Users\priya\Desktop\VS Code\chatgpt\menu.py", line 27, in <module>
   # bank.withdraw(accno, witamt)
#Same error comes in deposit fd as well 

    elif serv == 4:
        accno = int(input("Enter Accno: "))
        fdamt = int(input("Enter FD Amount: "))
        yrs = int(input("Enter FD Years: "))
        bank.fd(accno, fdamt, yrs)
    elif serv == 5:
        bank.transaction()
        break
    else:
        print("Invalid option. Please try again.")
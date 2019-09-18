import pickle
import time
from datetime import datetime


class Transaction:

    def __init__(self, transactionType, amount):
        self.transactionType = transactionType
        #self.accountNumber = accountNumber
        self.amount = amount
        self.date = datetime.now()

class Account:

    transactionLogg = []


    def __init__(self, accountNumber):
        self.accountNumber = accountNumber
        self.saldo = 0

    def getAccountNumber(self):
        return self.accountNumber

    def getSaldo(self):
        return self.saldo

    def deposit(self,amount):
        self.saldo += amount

    def withdraw(self,amount):
        if amount > self.saldo:
            print(f"Du kan inte ta ut {amount} kr")
            return False
        else:
            self.saldo -= amount
            return True


def GetMoneyAmount():
    while True:
        try:
            money = int(input("Ange summan: "))
            if money >= 0:
                return money
            else:
                print("Summan måste vara större än 0")
        except:
            print("Du måste ange summan i siffror")


def GetMenySelection(min,max):
    while True:
        try:
            inValue = int(input("<< "))
            break
        except:
            print ("Ange bara ett tal, försök igen")
    while True:
        if inValue >= min and inValue <= max:
            break
        else:
            print(f"Talet måste vara mellan {min} och {max}")
    return inValue



def CreateAccount():
    accountNumber = input("Ange konto nr: ")
    accountList.append(Account(accountNumber))



def WithdrawFromAccount(accountNumber):
    for account in accountList:
        if accountNumber == account.getAccountNumber():
            sumToWithdraw = GetMoneyAmount()
            if sumToWithdraw < account.getSaldo():
                account.withdraw(sumToWithdraw)
                account.transactionLogg.append(Transaction("Withdraw", sumToWithdraw))
            else:
                print("Du har för lite på saldot")

def DepositToAccount(accountNumber):
    for account in accountList:
        if accountNumber == account.getAccountNumber():
            amountToDeposit = GetMoneyAmount()
            account.deposit(amountToDeposit)
            account.transactionLogg.append(Transaction("Deposit", amountToDeposit))
        

def ShowSaldo(accountNumber):
    for account in accountList:
        if accountNumber == account.getAccountNumber():
            print(f"Ditt saldo är {account.getSaldo()}")

def ListTransactions(accountNumber):
    for account in accountList:
        if accountNumber == account.getAccountNumber():
            for trans in account.transactionLogg:
                print(f"Transaktionstyp: {trans.transactionType}")
                print(f"Belopp: {trans.amount}")
                dateTimeString = trans.date.strftime("%Y-%m-%d  %H:%M:%S")
                print(f"Transaktions datum och tid {dateTimeString}")
               
                

def adminAccount(accountNumber):
    while True:
        print("***KONTOMENY***")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Visa transationer")
        print("5. Gå tillbaka till HUVUDMENY")


        selection = GetMenySelection(1,5)

        if selection == 1:
            WithdrawFromAccount(accountNumber)
        elif selection == 2:
            DepositToAccount(accountNumber)
        elif selection == 3:
            ShowSaldo(accountNumber)
        elif selection == 4:
            ListTransactions(accountNumber)
        elif selection == 5:
            break
        else:
            print("ERROR!! This can not happen")


def LogInToAccount():
    while True:
        accountNumber = input("Ange kontonumret du vill logga in på: ")
        for account in accountList:
            if accountNumber in account.getAccountNumber():
                adminAccount(accountNumber)         
            else:
                print("Fel konto nummer")
        break


def OpenAccountList(filename):
    with open("filename", "rb") as input:
        accountList = pickle.loads(input)



def SaveAccounts(accountList, filename):
    with open(filename, "wb") as output:
        pickle.dump(accountList, output, pickle.HIGHEST_PROTOCOL)
    output.close()

accountList = []
#FILENAME = "kontofil2.pkl"

FILENAME = "C:\\Users\\larsb\\source\\repos\\OBJP_AccountSaldo\\OBJP_AccountSaldo\\kontofil3.pkl"
filnamn = "C:\\Users"\


while True:
    #accountList = []

    print("1 Läs in")
    print("2 Skapa konto")
    print("3 Logga in")
    print("4 Spara")
    print("5 Avsluta")

    selection = GetMenySelection(1,5)

    if selection == 1:
        OpenAccountList(FILENAME)
    elif selection == 2:
        CreateAccount()
    elif selection == 3:
        LogInToAccount()
    elif selection == 4:
        SaveAccounts(accountList, FILENAME)
    elif selection == 5:
        break     
    else:
        print("Du ska inte vara här !!!!!!")


    
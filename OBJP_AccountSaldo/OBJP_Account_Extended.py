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

   # transactionLogg = []

    def __init__(self, accountNumber):
        self.accountNumber = accountNumber
        self.saldo = 0
        self.transactionLogg = []

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


def ListAllAccountNumbers(listOfAllAccounts):
    print("***Alla kontonummer skapade***")
    for account in listOfAllAccounts:
        print(f"Kontonummer: {account.getAccountNumber()}")


def WithdrawFromAccount(account):
    sumToWithdraw = GetMoneyAmount()
    if sumToWithdraw < account.getSaldo():
         account.withdraw(sumToWithdraw)
         account.transactionLogg.append(Transaction("Withdraw", sumToWithdraw))
    else:
         print("Du har för lite på saldot")

def DepositToAccount(account):
    amountToDeposit = GetMoneyAmount()
    account.deposit(amountToDeposit)
    account.transactionLogg.append(Transaction("Deposit", amountToDeposit))
        

def ShowSaldo(account):
    print(f"Ditt saldo är {account.getSaldo()}")



def ListTransactions(account):
    for trans in account.transactionLogg:
        print(f"Transaktionstyp: {trans.transactionType}")
        print(f"Belopp: {trans.amount}")
        dateTimeString = trans.date.strftime("%Y-%m-%d  %H:%M:%S")
        print(f"Transaktions datum och tid {dateTimeString}")
               
                

def adminAccount(account):
    while True:
        print(f"***KONTOMENY för konto {account.getAccountNumber()}***")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Visa transationer")
        print("5. Gå tillbaka till HUVUDMENY")


        selection = GetMenySelection(1,6)

        if selection == 1:
            WithdrawFromAccount(account)
        elif selection == 2:
            DepositToAccount(account)
        elif selection == 3:
            ShowSaldo(account)
        elif selection == 4:
            ListTransactions(account)
        elif selection == 5:
            break
        else:
            print("ERROR!! This can not happen")


def LogInToAccount():
    while True:
        accountNumber = input("Ange kontonumret du vill logga in på: ")
        for account in accountList:
            if accountNumber == account.getAccountNumber():
                adminAccount(account)         
            else:
                print("Fel konto nummer")
        break


def OpenAccountList(filename):
    input = open(filename, "rb")
    savedAccountList = pickle.load(input)
    input.close()
    return savedAccountList



def SaveAccounts(accountList, filename):
    output = open(filename, "wb")
    pickle.dump(accountList, output, pickle.HIGHEST_PROTOCOL)
    output.close()

accountList = []

FILENAME = "kontofil.pickle"


while True:

    print("1 Läs in kontot från fil")
    print("2 Skapa konto")
    print("3 Lista alla konton")
    print("4 Logga in")
    print("5 Spara alla kontot till fil")
    print("6 Avsluta")

    selection = GetMenySelection(1,5)

    if selection == 1:
        accountList = OpenAccountList(FILENAME)
    elif selection == 2:
        CreateAccount()
    elif selection == 3:
        ListAllAccountNumbers(accountList)
    elif selection == 4:
        LogInToAccount()
    elif selection == 5:
        SaveAccounts(accountList, FILENAME)
    elif selection == 6:
        break     
    else:
        print("Du ska inte vara här !!!!!!")


    
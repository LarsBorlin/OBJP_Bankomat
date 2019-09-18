


def GetMoneyValue():
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





#Kontomeny val #1
def WithdrawFromAccount(accountNumber):
    while True:
        sumToWithdraw = GetMoneyValue()
        if sumToWithdraw <= accounts[accountNumber]:
            accounts[accountNumber] -= sumToWithdraw
            break
        else:
            print(f"Du har för lite pengar på kontot")


#Kontomeny val #2
def DepositToAccount(accountNumber):
    while True:
        accounts[accountNumber] += GetMoneyValue()
        break


#Kontomeny val #3
def ShowSaldo(accountNumber):
    print(f"Ditt saldo är {accounts[accountNumber]}")



def AdminAccount(accountNumber):
    while True:
        print("***KONTOMENY***")
        print("1. Ta ut pengar")
        print("2. Sätt in pengar")
        print("3. Visa saldo")
        print("4. Gå tillbaka till HUVUDMENY")

        selection = GetMenySelection(1,4)

        if selection == 1:
            WithdrawFromAccount(accountNumber)
        elif selection == 2:
            DepositToAccount(accountNumber)
        elif selection == 3:
            ShowSaldo(accountNumber)
        elif selection == 4:
            break
        else:
            print("ERROR !!! This can not happen")

#Huvudmeny val #1
def CreateAccount():
    accountNumber = input("Ange kontonummer: ")
    if accountNumber in accounts:
        print(f"Kontonummer {accountNumber} är redan skapat. Försök med ett annat kontonummer")
    else:
        accounts[accountNumber] = 0


#Huvudmeny val #2
def LogInToAccount():
    accountNumber = input("Ange kontonummer: ")
    if accountNumber in accounts:
        AdminAccount(accountNumber)
    else:
        print(f"Kontonummer {accountNumber} existerar inte, försök igen")


def ListAccountsNumber():
    for accountNumber in accounts:
        print(f"Kontonummer: {accountNumber}")


accounts = {}

while True:
    print("***HUVUDMENY***")
    print("1. Skapa konto")
    print("2. Administrera konto")
    print("3. Avsluta")
    print("4. Lista konton")
    
    selection = GetMenySelection(1,4)

    if selection == 1:
        CreateAccount()
    elif selection == 2:
        LogInToAccount()
    elif selection == 3:
        break
    elif selection == 4:
        ListAccountsNumber()
    else:
        print("ERROR!!. This can not happen")

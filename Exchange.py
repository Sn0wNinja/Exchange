
from pyfiglet import figlet_format
from termcolor import colored

continue_ = True

class BIT:

    def __init__(self, amount):
        self.amount = amount
        BIT.BIT_to_CHF = 17133.17
        BIT.BIT_to_USD = 19139.30

    def BITtoCHF(self):
    	print("")
    	print(f"฿ {self.amount} was converted to ₣ {round((self.amount * BIT.BIT_to_CHF))}")

    def BITtoUSD(self):
    	print("")
    	print(f"฿ {self.amount} was converted to $ {round((self.amount * BIT.BIT_to_USD))}")

class CHF:

    def __init__(self, amount):
        self.amount = amount
        CHF.CHF_to_BIT = 0.000059
        CHF.CHF_to_USD = 1.12

    def CHFtoBIT(self):
    	print("")
    	print(f"₣ {self.amount} was converted to ฿ {round((self.amount *  CHF.CHF_to_BIT))}")

    def CHFtoUSD(self):
    	print("")
    	print(f"₣ {self.amount} was converted to $ {round((self.amount * CHF.CHF_to_USD))}")

class USD:

    def __init__(self, amount):
        self.amount = amount
        USD.USD_to_BIT = 0.000052
        USD.USD_to_CHF = 0.90

    def USDtoBIT(self):
    	print("")
    	print(f"$ {self.amount} was converted to ฿ {round((self.amount *  USD.USD_to_BIT))}")

    def USDtoCHF(self):
    	print("")
    	print(f"$ {self.amount} was converted to ₣ {round((self.amount * USD.USD_to_CHF))}")


while continue_:

	title = figlet_format("EXCHANGE")
	title = colored(title, color = "blue")
	print("")
	print(title)
	print("")

	print("Would you like to Exchange money? \n1 Exchange \n2 Exit")
	q1 = input()
	
		
	if q1 == "1":
		print("What currency do you hold? \n1 BIT \n2 CHF \n3 USD")
		currency_hold = input().upper()
			
		if currency_hold == "1" or currency_hold == "BIT":
			print("Exhange to: \n1 CHF \n2 USD")
			to_which = input()

			if to_which == "1" or to_which == "CHF":
				print("Please insert amount: ")
				amount = int(input())
				bit = BIT(amount)
				print("")
				bit.BITtoCHF()

			elif to_which == "2" or to_which == "USD":
				print("Please insert amount: ")
				amount = int(input())
				bit = BIT(amount)
				bit.BITtoUSD()
				
			else:
				print("")
				print("Invalid characters, please try again")
			
		elif currency_hold == "2" or currency_hold == "CHF":
			print("Exhange to: \n1 BIT \n2 USD")
			to_which = input()
				
			if to_which == "1" or to_which == "BIT":
				print("Please insert amount: ")
				amount = int(input())
				chf = CHF(amount)
				print("")
				chf.CHFtoBIT()

			elif to_which == "2" or to_which == "USD":
				print("Please insert amount: ")
				amount = int(input())
				chf = CHF(amount)
				chf.CHFtoUSD()

			else:
				print("")
				print("Invalid characters, please try again")

			
		elif currency_hold == "3" or currency_hold == "USD":
			print("Exhange to: \n1 BIT \n2 CHF")
			to_which = input()
				
			if to_which == "1" or to_which == "BIT":
				print("Please insert amount: ")
				amount = int(input())
				usd = USD(amount)
				print("")
				usd.USDtoBIT()

			elif to_which == "2" or to_which == "CHF":
				print("Please insert amount: ")
				amount = int(input())
				usd = USD(amount)
				usd.USDtoCHF()

			else:
				print("")
				print("Invalid characters, please try again")
				
		else:
			print("")
			print("Invalid characters, please try again")

	elif q1 == "2":
		print("Thank you for using our App \nHave a great time!")
		continue_ = False

	else:
		print("")
		print("Invalid characters, please try again")

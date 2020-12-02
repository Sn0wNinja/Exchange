from pyfiglet import figlet_format
from termcolor import colored

continue_ = True

class BTC:

    def __init__(self, amount):
        self.amount = amount
        BTC.BTC_to_CHF = 17133.17
        BTC.BTC_to_USD = 19139.30

    def BTCtoCHF(self):
    	print("")
    	print(f"฿ {self.amount} was converted to ₣ {round((self.amount * BTC.BTC_to_CHF))}")

    def BTCtoUSD(self):
    	print("")
    	print(f"฿ {self.amount} was converted to $ {round((self.amount * BTC.BTC_to_USD))}")

class CHF:

    def __init__(self, amount):
        self.amount = amount
        CHF.CHF_to_BTC = 0.000059
        CHF.CHF_to_USD = 1.12

    def CHFtoBTC(self):
    	print("")
    	print(f"₣ {self.amount} was converted to ฿ {round((self.amount *  CHF.CHF_to_BTC))}")

    def CHFtoUSD(self):
    	print("")
    	print(f"₣ {self.amount} was converted to $ {round((self.amount * CHF.CHF_to_USD))}")

class USD:

    def __init__(self, amount):
        self.amount = amount
        USD.USD_to_BTC = 0.000052
        USD.USD_to_CHF = 0.90

    def USDtoBTC(self):
    	print("")
    	print(f"$ {self.amount} was converted to ฿ {round((self.amount *  USD.USD_to_BTC))}")

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
		print("What currency do you hold? \n1 BTC \n2 CHF \n3 USD")
		currency_hold = input().upper()
			
		if currency_hold == "1" or currency_hold == "BTC":
			print("Exhange to: \n1 CHF \n2 USD")
			to_which = input()

			if to_which == "1" or to_which == "CHF":
				print("Please insert amount: ")
				amount = int(input())
				btc = BTC(amount)
				print("")
				btc.BTCtoCHF()

			elif to_which == "2" or to_which == "USD":
				print("Please insert amount: ")
				amount = int(input())
				btc = BTC(amount)
				btc.BTCtoUSD()
				
			else:
				print("")
				print("Invalid characters, please try again")
			
		elif currency_hold == "2" or currency_hold == "CHF":
			print("Exhange to: \n1 BTC \n2 USD")
			to_which = input()
				
			if to_which == "1" or to_which == "BTC":
				print("Please insert amount: ")
				amount = int(input())
				chf = CHF(amount)
				print("")
				chf.CHFtoBTC()

			elif to_which == "2" or to_which == "USD":
				print("Please insert amount: ")
				amount = int(input())
				chf = CHF(amount)
				chf.CHFtoUSD()

			else:
				print("")
				print("Invalid characters, please try again")

			
		elif currency_hold == "3" or currency_hold == "USD":
			print("Exhange to: \n1 BTC \n2 CHF")
			to_which = input()
				
			if to_which == "1" or to_which == "BTC":
				print("Please insert amount: ")
				amount = int(input())
				usd = USD(amount)
				print("")
				usd.USDtoBTC()

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

from time import time

class blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def new_block(self):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pending_transactions,
        }
        self.pending_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, receiver, amount, coin):
        transaction = {
            "sender": sender.address,
            "receiver": receiver.address,
            "amount": amount,
            "coin": coin
        }

        if coin == "SDC":
            sender.SDC -= amount
            receiver.SDC += amount
        elif coin == "USD":
            sender.USD -= amount
            receiver.USD += amount

        self.pending_transactions.append(transaction)

        if len(self.pending_transactions) == 3:
            self.new_block()


class wallet():
    def __init__(self, SDC, USD, address):
        self.SDC = SDC
        self.USD = USD
        self.address = address


bc = blockchain()

# Wallets

Starda = wallet(1000, 1000, "starda.wallet")

francis = wallet(10, 10, "francis.wallet")
micheal = wallet(10, 10, "micheal.wallet")
jake = wallet(10, 10, "jake.wallet")
alex = wallet(10, 10, "alex.wallet")
john = wallet(10, 10, "john.wallet")
jason = wallet(10, 10, "jason.wallet")

people = [francis, micheal, jason, alex, john, jason]

words = ["apple", "fruit", "boat", "pickaxe", "axe", "wood", "noodles"]

askReplay = True

finish = False
finishToo = False
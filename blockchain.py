# Name: M. Sheheryar Tariq
# StudentID: 24819196

import hashlib
import time


class Block:
    def __init__(self, index, data, prev_hash):
        self.index = index
        self.timestamp = time.ctime()
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.make_hash()

    def make_hash(self):
        info = str(self.index) + self.timestamp + self.data + self.prev_hash
        return hashlib.sha256(info.encode()).hexdigest()

    def show_block(self):
        print(f"Block #{self.index}")
        print(f"Time: {self.timestamp}")
        print(f"Data: {self.data}")
        print(f"Previous Hash: {self.prev_hash}")
        print(f"Current Hash: {self.hash}")
        print("-" * 40)


class MyBlockchain:
    def __init__(self):
        self.chain = [self.create_first_block()]

    def create_first_block(self):
        return Block(0, "Genesis Block", "0")

    def add_new_block(self, data):
        prev_block = self.chain[-1]
        new_block = Block(len(self.chain), data, prev_block.hash)
        self.chain.append(new_block)

    def print_chain(self):
        for block in self.chain:
            block.show_block()

    def check_validity(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]

            if curr.hash != curr.make_hash():
                print(f"⛔ Block {i} has been changed!")
                return False

            if curr.prev_hash != prev.hash:
                print(f"⛔ Block {i} is not linked properly!")
                return False

        print("✅ Blockchain is valid.")
        return True


def run_app():
    my_chain = MyBlockchain()

    while True:
        print("\n==== Simple Blockchain ====")
        print("1. Add Block")
        print("2. Show Chain")
        print("3. Check Blockchain Validity")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            data = input("Enter some data for the block: ")
            my_chain.add_new_block(data)
            print("✅ New block added!")
        elif choice == "2":
            my_chain.print_chain()
        elif choice == "3":
            my_chain.check_validity()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    run_app()

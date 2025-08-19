import hashlib
import datetime

# Define a Block class
class Block:
    def __init__(self, index, task, timestamp, previous_hash):
        self.index = index
        self.task = task
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.task}{self.timestamp}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


# Define a Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", str(datetime.datetime.now()), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, task):
        new_block = Block(
            len(self.chain),
            task,
            str(datetime.datetime.now()),
            self.get_latest_block().hash
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print("-------------")
            print(f"Index: {block.index}")
            print(f"Task: {block.task}")
            print(f"Timestamp: {block.timestamp}")
            print(f"Previous Hash: {block.previous_hash}")
            print(f"Hash: {block.hash}")
            print("-------------\n")


# User Interface
def main():
    blockchain = Blockchain()

    while True:
        print("\n===== Blockchain To-Do List =====")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Validate blockchain")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter your task: ")
            blockchain.add_block(task)
            print("✅ Task added successfully!")

        elif choice == "2":
            print("\n📋 Your To-Do Blockchain:")
            blockchain.display_chain()

        elif choice == "3":
            if blockchain.is_chain_valid():
                print("✅ Blockchain is valid.")
            else:
                print("❌ Blockchain is not valid!")

        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break

        else:
            print("⚠ Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

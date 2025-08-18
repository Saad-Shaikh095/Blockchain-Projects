import hashlib
import time
import json

class Block:
    def __init__(self, index, timestamp, data, previous_hash, difficulty=2):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def calculate_hash(self):
        return hashlib.sha256(
            (str(self.index) + str(self.timestamp) + str(self.data) +
             str(self.previous_hash) + str(self.nonce)).encode()
        ).hexdigest()

    def mine_block(self):
        while True:
            hash_value = self.calculate_hash()
            if hash_value.startswith("0" * self.difficulty):
                return hash_value
            self.nonce += 1

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.voters = set()  # prevent double voting

    def create_genesis_block(self):
        return Block(0, time.time(), {"type": "genesis", "msg": "Voting chain started"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_vote(self, voter, candidate):
        if voter in self.voters:
            print(f"[X] {voter} has already voted!")
            return False
        new_block = Block(len(self.chain), time.time(),
                          {"type": "vote", "voter": voter, "candidate": candidate},
                          self.get_latest_block().hash)
        self.chain.append(new_block)
        self.voters.add(voter)
        print(f"✅ Vote mined: {voter} -> {candidate}")
        return True

    def tally_votes(self):
        results = {}
        for block in self.chain:
            if block.data["type"] == "vote":
                candidate = block.data["candidate"]
                results[candidate] = results.get(candidate, 0) + 1
        return results

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            curr = self.chain[i]
            prev = self.chain[i - 1]
            if curr.hash != curr.calculate_hash():
                return False
            if curr.previous_hash != prev.hash:
                return False
        return True

    def print_chain(self):
        print(json.dumps([block.__dict__ for block in self.chain], indent=2, default=str))

# ------------- Interactive Menu ----------------
if __name__ == "__main__":
    blockchain = Blockchain()

    while True:
        print("\n--- Voting Blockchain ---")
        print("1. Cast a vote")
        print("2. Show results")
        print("3. Print blockchain")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            voter = input("Enter your voter ID: ")
            candidate = input("Enter candidate name: ")
            blockchain.add_vote(voter, candidate)

        elif choice == "2":
            print("📊 Current Results:", blockchain.tally_votes())

        elif choice == "3":
            blockchain.print_chain()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again!")

🗳️ Blockchain Voting System

A simple Python-based voting system that uses blockchain technology to securely record votes.
Each vote is stored as a block, ensuring transparency, immutability, and integrity of the election process.

🚀 Features

Cast Votes — securely add votes to the blockchain

Immutable Records — once stored, votes cannot be altered

View Blockchain — see the full chain of votes with timestamps and hashes

Vote Counting — tally votes for each candidate

Chain Validation — ensures no tampering in the blockchain

📂 File

voting_blockchain.py — main script with blockchain-based voting logic

▶️ How to Run
# Run with Python 3
python voting_blockchain.py

🖥️ Example Usage
--- Blockchain Voting System ---
1. Cast a vote
2. Show Blockchain
3. Count votes
4. Exit


Choose 1 → Cast your vote (stored in the blockchain)

Choose 2 → Display the blockchain with all votes

Choose 3 → Show live vote counts per candidate

Choose 4 → Exit the program

📊 Sample Output
✅ Vote added: Alice voted for Bob

--- Voting Results ---
Bob: 1 votes


Blockchain storage for votes looks like this:

Block 1
Timestamp: Mon Aug 19 15:34:22 2024
Data (Vote): Alice voted for Bob
Hash: 2f93f91a2b8...
Previous Hash: 0000a1c93b...

💡 What You Learn

Basics of blockchain data structure

How immutability and hashing ensure election integrity

Securely recording votes with linked blocks

⚠️ Disclaimer

This is an educational project only.
It is not meant for real elections and does not implement features like encryption, authentication, or large-scale security.
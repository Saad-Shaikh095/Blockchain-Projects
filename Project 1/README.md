🧱 Basic Interactive Blockchain in Python

A very simple blockchain implementation written in pure Python.
This project demonstrates the core idea of blockchains — chaining blocks using hashes — in an easy-to-understand way.

✨ Features

Blocks linked together using SHA-256 hashes

A genesis block (first block in the chain)

Interactive CLI:

Add new blocks with custom data

Print the full blockchain

No external libraries required (just Python's built-in hashlib and time)

▶️ How to Run
# Windows (PowerShell / CMD) or macOS/Linux
python main.py


You will see a menu like this:

1. Add a block
2. Print blockchain
3. Exit

📂 File Structure

main.py — contains the Block and Blockchain classes + interactive menu.

💡 Example Usage

Run the program

Choose 1 and enter some text → adds a block with your data

Choose 2 → prints the blockchain:

Index: 1
Timestamp: 1723547890.123
Data: Hello Blockchain
Hash: 2f8c9d6e...
Previous Hash: 1a3b4c5d...
----------------------------------------

🧪 What You Can Try

Add multiple blocks and see how each one is connected via previous_hash.

Change the data stored (try transactions, notes, or messages).

Modify the code to include a simple Proof-of-Work (mining).

⚠️ Disclaimer

This is an educational project only.
It is not secure and should not be used as a real blockchain implementation.

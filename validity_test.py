from blockchain import Blockchain

#describing our mempool
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}
block_four_transactions = {"sender":"Ralph", "receiver":"Tian", "amount":"75"}
block_five_transactions = {"sender":"Alice", "receiver":"Ralph", "amount":"30"}

fake_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"20"}

#initializing our Blockchain
local_blockchain = Blockchain()
local_blockchain.print_blocks() #we only have the genesis_block now

#inserting three blocks of transactions
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
#printing the current blockchain
local_blockchain.print_blocks()
#validating our Blockchain
print(local_blockchain.validate_chain())

#Now Modifying our Blockchain by inserting fake_transactions
print("Now modifying the second block's transactions to fake_transactions. ")
local_blockchain.chain[2].transactions = fake_transactions
#validating our Blockchain
print(local_blockchain.validate_chain()) #This should give False/Invalid signal

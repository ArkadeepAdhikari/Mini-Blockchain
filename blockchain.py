from block import Block

class Blockchain:
  def __init__(self):
    """
    This function initializes our Blockchain
    Inputs Desc:
    chain: collection of objects of type Block
    unconfirmed_transactions:mempool i.e. pool of transactions yet to be confirmed
    and inserted in the Blockchain chain
    genesis_block:the first block of the Blockchain
    """
    self.chain = []
    self.unconfirmed_transactions = []
    self.genesis_block()

  def genesis_block(self):
    """
    Defines the first block of our Blockchain
    This block will have no transactions and will have a previous_hash value of 0
    """
    transactions = []
    genesis_block = Block(transactions, "0")
    genesis_block.generate_hash()
    self.chain.append(genesis_block)

  def add_block(self, transactions):
    """
    Used to add blocks to the Blockchain
    Input: Transactions taken from the mempool to be confirmed into the chain after verification by the participant
    Output: Proof of work and added block
    Every miner needs to generate a hash requiring some constraints called the proof_of_work
    Miners compete to find this hash!
    """
    previous_hash = (self.chain[len(self.chain)-1]).hash
    new_block = Block(transactions, previous_hash)
    new_block.generate_hash()
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

  def print_blocks(self):
    """
    This is used to print the contents of the entire Blockchain
    """
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()

  def validate_chain(self):
    """
    This function checkes the validity of the Blockchain.
    For the chain to be valid, the hash value for each block must be computed
    correctly and the previous_hash of each block should be mapped correctly.
    If we find a broken chain we return False.
    """
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("Finding Validity.. \nBlockchain invalid!")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("Finding Validity.. \nBlockchain invalid!")
        return False
    print("Finding Validity.. \nBlockchain is valid")
    return True

  def proof_of_work(self,block, difficulty=4):
    """
    This block defines the proof of work to be computed by the miners to add a block
    into the chain. For this we increase the nonce value until a hash with required
    difficulty is generated.
    For our chain we want a hash whose first 4 digits are 0000
    The level of hardness and constaints on the hash can be increased for more larger chains
    """
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof

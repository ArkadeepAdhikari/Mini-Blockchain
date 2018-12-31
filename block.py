import datetime
from hashlib import sha256
#sha256 generates a 256 bit (32 byte) signature or hash for a given text data

class Block:
  """
  Defines variables and functions for a block of transactions of the Blockchain
  """
  def __init__(self, transactions, previous_hash):
    """
    Initializes the essential components of a block
    Each block will have a unique hash or digital footprint which can be found
    using the function generate_hash
    Also each block has the previous_hash value stored in it for validation
    """
    self.time_stamp = datetime.datetime.now()
    self.transactions = transactions
    self.previous_hash = previous_hash
    self.nonce = 0
    self.hash = self.generate_hash()

  def generate_hash(self):
    """
    This function calculates the hash value using the time_stamp,transaction details,
    previous_hash, and nonce and returns the value of the block's hash
    """
    block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
    block_hash = sha256(block_header.encode())
    return block_hash.hexdigest()

  def print_contents(self):
    """
    This prints the details of the block
    """
    print("timestamp:", self.time_stamp)
    print("transactions:", self.transactions)
    print("current hash:", self.generate_hash())
    print("previous hash:", self.previous_hash)

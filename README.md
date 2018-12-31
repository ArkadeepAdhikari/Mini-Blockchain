# Mini-Blockchain

# Description

Mini-Blockchain is a small sized implementation of Blockchain. It can be used to store data such as transactions between senders and receivers. 
It is based on the idea of blockchain and keeps a record of transactions in chronological order.
The implementation has two main components:
<br></br>1.Block: This can be thought of an individual transaction or piece of data that can be stored within the blockchain
2.Blockchain: This is a continuously growing list of records (blocks) that are linked chronologically and secured using cryptography methods

# Implementation and Testing

The Mini-Blockchain has been tested with transaction data of the following form:
transaction1 = {
  'amount': '50',
  'sender': 'Ron',
  'receiver': 'Harry'}
In this transaction, Ron sends 50 units of some currency to Harry.

The hashing function used in this implementation is sha-256 which can be easily imported using hashlib library
The Mini-Blockchain also has a proof-of-work implemented where the miners must compete to get 0000 as the first 4 digits as the hash to broadcast 
their unconfirmed work in the network. This difficulty can be easily modified later using the difficulty variable.

# Requirements

Python3 is required for this implementation

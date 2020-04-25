


# =============================================================================
# # Problem 5: Blockchain
# # A Blockchain is a sequential chain of records, similar to a linked list. 
# # Each block contains some information and how it is connected related to the 
# # other blocks in the chain. Each block contains a cryptographic hash of the 
# # previous block, a timestamp, and transaction data. For our blockchain we will 
# # be using a SHA-256 hash, the Greenwich Mean Time when the block was created, 
# # and text strings as the data.
# =============================================================================



class Block:

    def __init__(self, data):
        
        from datetime import datetime
        self.timestamp = datetime.utcnow()
        self.data = data
        self.previous_hash = None
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        import hashlib
        sha = hashlib.sha256()  # creat a SHA-256 hash object
        hash_str = self.data.encode('utf-8') # convert data to a bytes-like object
        sha.update(hash_str) # feed the sha hash object         
        return sha.hexdigest() # the digest of the concatenation of the data fed to it so far


class BlockChain:
    
    def __init__(self, data): # block needs to be a Block
        block = Block(data)
        self.head = block
        self.tail = block

    def add_block(self, new_data): # new_block needs to be a Block
        new_block = Block(new_data)
        self.tail.next = new_block
        new_block.previous_hash = self.tail.hash
        self.tail = new_block        

    def print_blockchain(self):
        current_block = self.head
        while current_block:
            print(current_block.data)
            print('(block created at: {})\n'.format(current_block.timestamp))
            current_block = current_block.next

# Test:

data1 = 'My name is Delong Meng, and '
data2 = 'I am working on my Data Structure and Algorithms NanoCourse. I want to tell you that '
data3 = 'I think Udacity rocks!'

blockchain = BlockChain(data1) # creat a blockchain

blockchain.add_block(data2) # add a new block
blockchain.add_block(data3) # add a new block

blockchain.print_blockchain() # print/visit a block chain

# Output:
# My name is Delong Meng, and 
# (block created at: 2020-04-24 00:52:47.544353)

# I am working on my Data Structure and Algorithms NanoCourse. I want to tell you that 
# (block created at: 2020-04-24 00:52:47.544415)

# I think Udacity rocks!
# (block created at: 2020-04-24 00:52:47.544454)




data1 = 'Hello?'
data2 = ' '     # the second string is just a space
data3 = 'Hey!'

blockchain = BlockChain(data1) # creat a blockchain

blockchain.add_block(data2) # add a new block
blockchain.add_block(data3) # add a new block

blockchain.print_blockchain() # print/visit a block chain

# Output:
# Hello?
# (block created at: 2020-04-24 00:53:40.013867)

# 
# (block created at: 2020-04-24 00:53:40.013942)

# Hey!
# (block created at: 2020-04-24 00:53:40.014000)




data1 = 'Hello?'
data2 = ''     # the second string is an empty string
data3 = 'Hey!'

blockchain = BlockChain(data1) # creat a blockchain

blockchain.add_block(data2) # add a new block
blockchain.add_block(data3) # add a new block

blockchain.print_blockchain() # print/visit a block chain

# Output:
# Hello?
# (block created at: 2020-04-24 00:54:37.178628)

#
# (block created at: 2020-04-24 00:54:37.178677)

# Hey!
# (block created at: 2020-04-24 00:54:37.178712)



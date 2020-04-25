# Blockchain


A Blockchain is a sequential chain of records, similar to a linked list. 
Each block contains some information and how it is connected related to the 
other blocks in the chain. Each block contains a cryptographic hash of the 
previous block, a timestamp, and transaction data. For our blockchain we will 
be using a SHA-256 hash, the Greenwich Mean Time when the block was created, 
and text strings as the data.


Here I implemented a blockchain structure based on a linked list. Each block is a node, and has several attributes: timestamp, data, previous hash, its own hash, and a 'next' pointer. In the blockchain, we have a head and a tail. When we initiate the blockchain, within the blockchain class, we first create a block using the input data, and assign it to both head and tail. Then every time we add a new data, we creat a new block containing that data, put it at the tail of the linked list, point the old tail to it, and set its previous hash as the hash of the previous tail. When we visit the blockchain, we just need to traverse the whole blockchain from the head to the tail. The time complexity of creating a new block, a new blockchain, or adding a new block to a blockchain are all O(1), and printing out a whole blockchain is O(n), where n is the length of the blockchain. Space complexity for operations is O(1) because we add one block at a time.


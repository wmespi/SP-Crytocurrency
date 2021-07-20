import importlib
## import blockchain code
blockchain_lib = input('blockchain:')
importlib.import_module(blockchain_lib)

## creating instance of blockchain
blockchain = bc.Blockchain()

## transactions
t1 = blockchain.new_transaction('timmy','billy','1 SP')
t2 = blockchain.new_transaction('billy','timmy','10 SP')
t3 = blockchain.new_transaction('sally','billy','20 SP')

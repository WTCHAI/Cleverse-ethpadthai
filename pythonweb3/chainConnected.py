from web3 import Web3 as web3Lib , EthereumTesterProvider


# w3 = Web3(EthereumTesterProvider())
w3Eth = web3Lib(web3Lib.HTTPProvider("https://eth-pokt.nodies.app"))

isConnected = w3Eth.is_connected()
print(isConnected)

W3Binance = web3Lib(web3Lib.HTTPProvider("https://bsc.drpc.org"))
BinanceBlockNumber = W3Binance.eth.block_number

print(f"Eth blocknumber binance is {BinanceBlockNumber}")

Sepolia = web3Lib(web3Lib.HTTPProvider('https://1rpc.io/sepolia'))
SepoliaAddress = "0xc3c52B4977937065bb8806065D71b832c0c6c8b7"
SepoliaBlockNumber = Sepolia.eth.get_balance(SepoliaAddress)

print(SepoliaBlockNumber)




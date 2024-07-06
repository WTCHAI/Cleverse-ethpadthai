from web3 import Web3 as web3Lib , EthereumTesterProvider



# w3 = Web3(EthereumTesterProvider())
w3Eth = web3Lib(web3Lib.HTTPProvider("https://1rpc.io/sepolia"))

wallet = w3Eth.eth.account.create()

wallAddr = wallet.address
wallPriv = wallet.key

print (f"Wallet Address: {wallAddr}")
print (f"Wallet Private Key: {w3Eth.to_hex(wallPriv)}")
# print (f"Wallet Public Key: {wallPublic}")

# walletAccount = w3Eth.eth.account.from_key(wallPriv)
print (f"Wallet Account: {wallet.address}")
eth_balnce = w3Eth.eth.get_balance("0x41649a1F8B2499e2F7884184D062639CEF9d0601")

print(f"Wallet balance : {eth_balnce/10**18}")
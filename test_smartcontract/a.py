from web3 import Web3
from b import show_address

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:26701'))
print("smartcontract")
print(f'connected {w3.isConnected()}')
w3.eth.account.enable_unaudited_hdwallet_features()
mnemonics="night renew tonight dinner shaft scheme domain oppose echo summer broccoli agent face guitar surface belt veteran siren poem alcohol menu custom crunch index"
account = w3.eth.account.from_mnemonic(mnemonics)    
print(account.address)

show_address(mnemonics,10)
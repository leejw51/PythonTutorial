#pip install py-solc-x
from web3 import Web3
from b import show_address
from solcx import compile_source,install_solc
import  json
 
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:26701'))
print("smartcontract")
print(f'connected {w3.isConnected()}')
w3.eth.account.enable_unaudited_hdwallet_features()
mnemonics="night renew tonight dinner shaft scheme domain oppose echo summer broccoli agent face guitar surface belt veteran siren poem alcohol menu custom crunch index"
account = w3.eth.account.from_mnemonic(mnemonics)    
print(account.address)

addr = account.address
#show_address(mnemonics,10)
print( w3.eth.accounts)
c=w3.eth.get_balance(addr)
print(f"account={addr} balance={c}")

install_solc(version='latest')

compiled_sol = compile_source(
     '''
    pragma solidity >0.5.0;

     contract Greeter {
         string public greeting;

         constructor() public {
             greeting = 'Hello';
         }

         function setGreeting(string memory _greeting) public {
             greeting = _greeting;
         }

        function greet() view public returns (string memory) {
             return greeting;
         }
     }
     '''
 )
contract_id, contract_interface = compiled_sol.popitem()
print(f'contraid_id {contract_id}')
bytecode = contract_interface['bin']
abi = contract_interface['abi']
chainid=777
print(f'bytecode={bytecode}')
print(f'abi={abi}')
w3.eth.defaultAccount = account

Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce=w3.eth.get_transaction_count(account.address) 
gas=3000000000
print(f'account ${account.address}')
print(f'nonce {nonce}')
tx_hash = Greeter.constructor().transact({'from':account.address,'nonce':nonce,'gas':gas, 'chainId':chainid})
#print(f'txhash ={tx_hash}')

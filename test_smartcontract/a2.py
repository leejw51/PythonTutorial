#pip install py-solc-x
from web3 import Web3
from b import show_address
from solcx import compile_source,install_solc
import  json
 
MYNODE='http://127.0.0.1:8545'
MYCHAINID=9000
MYGAS=3000000000
 
w3 = Web3(Web3.HTTPProvider(MYNODE))
print("smartcontract")
print(f'connected {w3.isConnected()}')
w3.eth.account.enable_unaudited_hdwallet_features()
#mnemonics="night renew tonight dinner shaft scheme domain oppose echo summer broccoli agent face guitar surface belt veteran siren poem alcohol menu custom crunch index"
mnemonics="frequent hood goddess egg copy area truth nest scissors hurdle early domain false march theory hip evolve vast wall sentence foil bubble beef movie"
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
# prepare contract
contract_id, contract_interface = compiled_sol.popitem()
print(f'contraid_id {contract_id}')
bytecode = contract_interface['bin']
abi = contract_interface['abi']
print(f'bytecode={bytecode}')
print(f'abi={abi}')
w3.eth.defaultAccount = account

# deploy
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)
nonce=w3.eth.get_transaction_count(account.address) 
info={'from':account.address,'nonce':nonce,'gas':MYGAS, 'chainId':MYCHAINID}
print(f"account={addr} balance={c} nonce={nonce}")
print(f'nonce {nonce}')
tx_hash = Greeter.constructor().transact(info)
print(f'txhash ={tx_hash}')
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"txreceipt={tx_receipt}")

# call contract
greeter = w3.eth.contract(
     address=tx_receipt.contractAddress,
     abi=abi
)
print(f"contract adddress {tx_receipt.contractAddress}")
a1=greeter.functions.greet().call(info)
print(f'result={a1}')

# change
nonce=w3.eth.get_transaction_count(account.address) 
info['nonce'] = nonce
tx_hash = greeter.functions.setGreeting('good morning').transact(info)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(f"txreceipt={tx_receipt}")


# call contract
a1=greeter.functions.greet().call(info)
print(f'result={a1}')

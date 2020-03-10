# Contract-Contract Calls
The following example shows how to invoke a function from an already deployed contract.

The `Caller` contract will invoke functions in the `Callee` contract. 

Inside `Caller.sol` you'll notice these specific lines.

One is for importing the definitions inside `Callee.sol` to `Caller.sol` while the statement `Callee c = Callee(addr)` instantiates an existing instance of the Callee contract on the blockchain by using its deployment address.

```
import "./Callee.sol";
...
Callee c = Callee(addr);
```

## Usage
### ethers.js Interace
Install ethers.js
```
npm install -g ethers
```
Interact with Contract
```
const ethers = require('ethers')

const url = "http://localhost:8545";
const provider = new ethers.providers.JsonRpcProvider(url);
const signer0 = provider.getSigner(0);

var contract_abi = [...]
var contract_addr = "0x1234....."
var contract = new ethers.Contract(contract_addr, contract_abi, provider);

var contract_with_signer = contract.connect(signer0);

contract_with_signer.setCalleeAddr("0xABCD.....");
contract_with_signer.CallerSetNum(1000);
contract_with_signer.CallerGetNum().then(console.log);
```

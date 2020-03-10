# BaD Token Demo
## Post-Deployment
Web3 setup
```
var web3 = require('web3')

// confirm proper import
Web3.version

// point to ganache-cli
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"))

// get accounts
web3.eth.getAccounts().then(accounts)
```
Contract Setup
```
// get address
var token_addr = "0x...."

// get ABI
var token_abi = [...]

// create instance
var bad_token = new web3.eth.Contract(token_abi, token_addr)
```

Usage
```
// get name
bad_token.methods.name().call().then(console.log)

// get symbol
bad_token.methods.symbol().call().then(console.log)
```
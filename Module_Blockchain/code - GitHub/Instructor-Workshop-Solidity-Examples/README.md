# Instructor Workshop: Your First Smart Contract (and Library!)
The folders and code here give an example of a minimal Truffle setup for deploying and interacting with a very simple smart contract.

You'll note there are two folders, one for each self-contained project. The instructions below are mostly applicable for both. If anything differs, it will be explicitly noted. 

# Set Up
## Dependencies
---
You will need:
* node.js
* npm
  * truffle
* Ganache
* Text Editor (your choice, personally recommend VSCode)

### `node.js` and `npm`

`node.js` allows us to run javascript code outside the browser (a sandboxed version of the Chrome V8 Javascript engine). `npm` or the `node package manager` allows us to install lots of neat packages made with node (like truffle, our Ethereum development environment). 

To install npm and node you can use the following link:
https://www.npmjs.com/get-npm

Node and npm will be installed at the same time. Verify successful installation by running the following commands in your terminal

```
node -v
```
which gives the version of node.js you have as well as :
```
npm -v
```
which gives the version of npm you have.

### Truffle
As stated above, Truffle will provide us with our full smart contract development environment

Run the following to install:
```
npm install -g truffle
```

Verify proper installation by trying the following command
```
truffle --help
```

### Ganache
Ganache is an Etheruem blockchain simulator, meaning you don't have to run an entire Ethreum node just to test your smart contracts! 

You can install it here: https://www.trufflesuite.com/ganache

### Text Editor
I personally prefer VSCode for the ease of use.

You can download it here: https://code.visualstudio.com/

and make sure to install the `solidity` extension for awesome syntax highlighting! 

## Firing Up Truffle
With our toolbelt ready, we have to fire up Truffle and get our code into position.

```
mkdir simple_contract
cd simple_contract 
```

Then we initialize a truffle environment like so
```
truffle init
```

You should see three directories and one file:
* `contracts`
  * This is where we'll be putting all of our actual contract code.
  * You'll see a file called `Migrations.sol`. __DO NOT TAMPER WITH THIS FILE__, this is used internally by Truffle
* `migrations`
  * This holds configurations files that tell Truffle how to move your contract from the local environment onto the network 
  * You'll see a file called `1_initial_migrations.js`. __DO NOT TAMPER WITH THIS FILE__, this is used internally by truffle
* `test`
  * This holds code for unit testing. We'll get to that on a future lesson
* `truffle-config.js`
  * configuration file for the entire environment, lets us "point" Truffle to our development network (Ganache)

## Putting Everything in Place

Inside the `simple_contract` folder of this repository, you'll notice the layout is very similar to what Truffle already offers.

This is a skeleton structure for what future projects should look like.

Go ahead and copy the `Simple.sol` file over to the `contracts` folder you just made as well as the `2_simple_deploy.js` file into your `migrations` folder. Feel free to poke around, both have comments to help you understand what's going on.

Also swap your existing `truffle-config.js` with the one in this directory. However, keep note of the `port` field in the file as that may have to change depending on your Ganache configuration.

## Deploying

With everythin in place, run the following:
```
truffle build
```
If everything is successful, you'll see the something like the following 
```
Compiling your contracts...
===========================
> Compiling ./contracts/Migrations.sol
> Compiling ./contracts/Simple.sol
> Artifacts written to /Users/jzl/Desktop/dummy/build/contracts
> Compiled successfully using:
   - solc: 0.5.8+commit.23d335f2.Emscripten.clang
```
Now lets go ahead and get this onto our Ganache instance.

Make sure you have Ganache running in the background. Ganache may prompt you to "Create a Workspace". Just hit the "Quickstart" option. 

Note the port number in the top bar, under the field that says "RPC SERVER". 

For example, if it says 
```
HTTP://127.0.0.1:8545
```
your port number is 8545. If this number is NOT 7545, you need to go into `truffle-config.js` and change the `port` field to whatever number you see.

With this all set, run the following command
```
truffle migrate
```
If all goes well you should see something like this wall of text
```
Compiling your contracts...
===========================
> Everything is up to date, there is nothing to compile.



Starting migrations...
======================
> Network name:    'development'
> Network id:      8888
> Block gas limit: 0x6691b7


1_initial_migration.js
======================

   Deploying 'Migrations'
   ----------------------
   > transaction hash:    0x285da7ffe7f86349f7af87125715fa46a7a23c49eccbc2d6809043f790d47973
   > Blocks: 0            Seconds: 0
   > contract address:    0x8fe62D6534F3eE1142eF09a8dd31694a60aafAe6
   > block number:        1
   > block timestamp:     1572547443
   > account:             0xa60e4B2e7b460dA30eb6018e68C07d0f0cf8471B
   > balance:             99.99477214
   > gas used:            261393
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00522786 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.00522786 ETH


2_simple_deploy.js
==================

   Deploying 'Simple'
   ------------------
   > transaction hash:    0xc8e286e890ecb998693ef7b867642854358e9b1036c2bf09981a68a515595e80
   > Blocks: 0            Seconds: 0
   > contract address:    0x10bE4E6cA8FAbD2E21007da619c28c8943914310
   > block number:        3
   > block timestamp:     1572547444
   > account:             0xa60e4B2e7b460dA30eb6018e68C07d0f0cf8471B
   > balance:             99.99145422
   > gas used:            123873
   > gas price:           20 gwei
   > value sent:          0 ETH
   > total cost:          0.00247746 ETH


   > Saving migration to chain.
   > Saving artifacts
   -------------------------------------
   > Total cost:          0.00247746 ETH


Summary
=======
> Total deployments:   2
> Final cost:          0.00770532 ETH

```

To be doubly sure, you can look at the Ganache UI and you should see that your main account has a reduced balance (99.99 ETH vs 100 ETH) and that there are 4 blocks instead of 0 in existence.

## Interacting with your Contract
To interact with our contract, we'll be using the `web3` javascript library which acts as a bridge between our development environment and the Ganache environment, facilitating communication between the two.

With `node.js` on our side, we can use `web3` on the fly through our command line instead of 

Go to the root directory of your folder and run the following:
```
npm install web3 solc --save
```
Start up node by doing :
```
node
```
In your terminal. This will bring up the node CLI.
This is where we'll be interacting with our smart contract

Run the following commands:
```javascript
// import the Web3 library
var Web3 = require('web3')
// check that it was imported properly, should give a number like
// 1.2.2
Web3.version;
// create an instance of web3 object, pointed to our Ganache node
// 
// Make sure you change the port number to whatever it is in your Ganache setup!
var web3 = new Web3(new Web3.providers.HttpProvider("http://localhost:8545"))
// Check that we are actually, in fact, pointed to the Ganache instance
web3.eth.getAccounts().then(console.log)
```
We ned to create an instance of an object that will represent our deployed contract and actually communicate with it.

To do so we need three things:
* main account address
  * Remember, if we invoke a contract function that changes state, we need to pay!
* address of the contract
  * Contracts, like individual users, have addresses!
  * Think of it as the house address of a friend
* contract ABI (Application Binary Interface)
  * This describes the interface to the contract
  * If your friend speaks another language, this is almost like a dictionary you can use to translate back and forth

To get the main account address:
```javascript
// Extract the first address returned from the promise through callback
web3.eth.getAccounts().then(accts => {main_acct = accts[0]})
// verify the address was obtained
main_acct
```
You can also manually verify by making sure the `main_acct` string is the same as whatever Ganache has as its first wallet address.

To get the address of the contract, we need to go back to our text editor. 

You'll note that after you ran `truffle build`, there's another folder called `build`. Inside `build` (and through the `contracts` folder inside it), you'll see two `.json` files, one called `Migrations.json` and `Simple.json`.

Open `Simple.json` and scrolling down (or you can use search), find this part of the file 
```javascript
  "networks": {
    "8888": {
      "events": {},
      "links": {},
      "address": "0x10bE4E6cA8FAbD2E21007da619c28c8943914310",
      "transactionHash": "0xc8e286e890ecb998693ef7b867642854358e9b1036c2bf09981a68a515595e80"
    }
```
Copy the value of the `address`, with the quotes and paste it into your node CLI like so:
```javascript
var contract_addr = "0x10bE4E6cA8FAbD2E21007da619c28c8943914310"
```

Now for the last part, the ABI. The ABI is also located in the `Simple.json` near the beginning but you'll want to copy and paste the whole thing into a JSON minifier, which strips the stuff of spaces/tabs and makes it nice to move around in our CLI environment.

It should look like this in `Simple.json`:
``` javascript
[
    {
      "constant": false,
      "inputs": [
        {
          "name": "x",
          "type": "uint256"
        }
      ],
      "name": "set_num",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "inc_num",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": false,
      "inputs": [],
      "name": "dec_num",
      "outputs": [],
      "payable": false,
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "constant": true,
      "inputs": [],
      "name": "reveal_num",
      "outputs": [
        {
          "name": "",
          "type": "uint256"
        }
      ],
      "payable": false,
      "stateMutability": "view",
      "type": "function"
    }
  ]
```
You can use this online minifier: https://codebeautify.org/jsonminifier

After "minifying" you get the following:
```javascript
[{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"inc_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"dec_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"reveal_num","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]
```

Copy and paste the minified stuff as the following into your node CLI
```javascript
var contract_abi = [{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"inc_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"dec_num","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"reveal_num","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]
```
If you type `contract_abi` by itself into the terminal you'll note that node does a nice job of color coding and "pretty-pretting" it, which means that the ABI was properly formatted and inputted.

Now put it all together like so:
```javascript
var simple_contract = new web3.eth.Contract(contract_abi, contract_addr)
```

To see all the contract functions you can invoke, write the following:
```javascript
simple_contract.methods
```

Lets go ahead and set a number:
```javascript
simple_contract.methods.set_num(88).send({from: main_acct}).then(res => {console.log(res)})
```

And lets see the value set:
```javascript
simple_contract.methods.reveal_num().call().then(console.log)
```

You'll note that for contracts that only `view` variables and data, you can just use the `call()` method whereas those that change state need `send()` invoked on them.

## `simple_lib` Setup
the `simple_lib` folder contains another project that shows how libraries in solidity work. 

The setup is very similar to that for `simple_contract` with some nuances.

When you grab the ABI and address, you need to grab it from the MAIN contract, which is `SafeMathExtern.json`. 

As with `simple_lib` please do explore the contents. 
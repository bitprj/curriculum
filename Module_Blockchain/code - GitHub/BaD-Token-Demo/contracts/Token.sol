
pragma solidity 0.5.12;

contract BaDToken {
    // Track how many tokens are owned by each address
    mapping (address => uint256) public balanceOf;
    //
    mapping(address => mapping(address => uint256)) public allowance;

    // ERC20 defines optional functions name() and symbol() to give
    // people outside contract info about the token
    //
    // Solidity automatically creates a corresponding getter if you
    // declare variables as `public`. The getter has the same name as the
    // variable so name getter is `name()`.
    string public name = "B.a.D Token";
    string public symbol = "BDT";
    // mandatory, totalSupply() provides the total amount in circulation
    uint256 public totalSupply = 1000;

    // an event is similar to a struct which is "emitted" after a certain
    // action occurs. You set the proper fields in the event and emit it.
    // web3 can pick this information up and unpack it for external use.
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    constructor() public {
        // Initially assign all tokens to the contract's creator.
        // `msg.sender` is a special variable that has the address of whoever
        // is currently interacting with the contract
        //
        // constructor function can only be invoked upon creation of contract
        balanceOf[msg.sender] = totalSupply;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    function transfer(address to, uint256 value) public returns (bool success) {
        // require() vs assert()
        // assert() uses up gas, require does not, performs refund
        // require() refunds gas, returns value explaining error
        require(balanceOf[msg.sender] >= value, "Insufficient Tokens");

        balanceOf[msg.sender] -= value;  // deduct from sender's balance
        balanceOf[to] += value;          // add to recipient's balance
        emit Transfer(msg.sender, to, value); // emit Transfer event with proper data
        return true;                     // balance transfer occured successfuly
    }

    // DELEGATED TRANSFER
    // grant permission to another user to send tokens from personal account
    // to another account

    // DELEGATED TRANSFER FUNCTION
    // allow other address to spend certain amount
    function approve(address spender, uint256 value) public returns (bool success)
    {
        allowance[msg.sender][spender] = value;
        emit Approval(msg.sender, spender, value);
        return true;
    }

    // DELEGATED TRANSFER FUNCTION
    // invoked by delegated-to function to transfer tokens to other account
    //
    // frm
    function transferFrom(address from, address to, uint256 value) public returns (bool success)
    {
        // delegator must own enough tokens to satisfy request
        require(value <= balanceOf[from], "Not enough tokens under ownership");
        // ensure delegator is authorized to spend amount from delegatee
        require(value <= allowance[from][msg.sender], "Not authorized to execute transaction");

        balanceOf[from] -= value; // deduct balance of delegatee
        balanceOf[to] += value;   // increase balance of "to" account
        allowance[from][msg.sender] -= value; // decrease amount delegator can spend
        emit Transfer(from, to, value); // emit proper transfer
        return true;
    }
}
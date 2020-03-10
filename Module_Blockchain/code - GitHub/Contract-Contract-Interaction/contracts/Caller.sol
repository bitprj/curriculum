pragma solidity ^0.5.8;

import "./Callee.sol";

contract Caller {

    address callee_addr;

    function setCalleeAddr(address _addr) public {
        callee_addr = _addr;
    }

    function CallerSetNum(uint _new_num) public {
        Callee c = Callee(callee_addr);
        c.set_num(_new_num);
    }

    function CallerGetNum() public view returns (uint) {
        Callee c = Callee(callee_addr);
        return c.get_num();
    }
}
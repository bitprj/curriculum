pragma solidity ^0.5.8;

contract Callee {
    uint256 public num;

    function get_num() public view returns (uint){
        return num;
    }

    function set_num(uint _new_num) public {
        num = _new_num;
    }
}
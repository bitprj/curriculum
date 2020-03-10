pragma solidity ^0.5.8;

// import the library (in the same directory)
import "./SafeMathLib.sol";

contract SafeMathExtern {
    // the library functions get applied to all instances
    // of the type `uint`
    using SafeMathLib for uint;

    uint num;

    // set the number
    function set_num(uint x) public {
        num = x;
    }

    // show the number
    function show_num () public view returns (uint) {
        return num;
    }

    // invoke library function to perform safe addition
    function add_num(uint x) public {
        num = num.plus(x);
    }

    // invoke library function to perform safe subtraction
    function sub_num(uint x) public {
        num = num.minus(x);
    }

    // invoke library function to perform safe multiplication
    function times_num(uint x) public {
        num = num.times(x);
    }

}
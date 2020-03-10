pragma solidity >=0.4.21 <0.6.0;
pragma experimental ABIEncoderV2;

contract MarriageRegister {

    // Structure for the marriage
    struct Marriage {
        string husband;
        string wife;
        uint date;
    }
    
    uint totalMarriages;
    Marriage[] register;

    // Add a new marriage to the register
    function newMarriage (string husband, string wife) public returns (uint uid) {
        uid = totalMarriages++;
        register.push(Marriage(husband, wife, now));
    }

    // Get all marriages from the register
    function getMarriages () public view returns (Marriage[]) {
        return register;
    } 
}


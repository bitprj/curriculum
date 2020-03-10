pragma solidity ^0.5.8;

// note the declaration as 'library' instead of 'contract'.
// Libraries are much more limited in what they can do than
// a normal contract.
library SafeMathLib {
  // perform safe multiplication
  function times(uint a, uint b) public pure returns (uint) {
    uint c = a * b;
    assert(a == 0 || c / a == b);
    return c;
  }

  // perform safe subtraction
  function minus(uint a, uint b) public pure returns (uint) {
    assert(b <= a);
    return a - b;
  }

  // perform safe addition
  function plus(uint a, uint b) public pure returns (uint) {
    uint c = a + b;
    assert(c>=a && c>=b);
    return c;
  }
}
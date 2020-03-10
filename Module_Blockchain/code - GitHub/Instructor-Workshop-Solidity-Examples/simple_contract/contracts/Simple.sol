// State which vesion of the solidity compiler will be used
pragma solidity ^0.5.8;

// Create a contract named "simple"
contract Simple
{
	// Create an unsigned integer
	uint num;


	// The `external` keyword defines the function as callable from other contracts
	// and does not copy its argument
	// NOTE: `external` functions cannot be called internaly!

	// Take an unsigned integer as its argument and set the internal variable to the
	// same value
	function set_num(uint x) external
	{
		num = x;
	}

	// Increment the internal number variable by 1
    function inc_num () external
    {
        ++num;
    }

	// Decrement the internal number variable by 1
    function dec_num () external
    {
        --num;
    }

	// Return the current state of the internal number variable
	function reveal_num () external view returns (uint)
	{
		return num;
	}
}
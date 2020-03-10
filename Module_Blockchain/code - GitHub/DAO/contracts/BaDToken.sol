pragma solidity ^0.5.8;

import "./BaseERC20.sol";
import "./MembershipDB.sol";

contract BaDToken is BaseERC20 {

    MembershipDB membership_contract;

    constructor(
        uint256 _totalSupply,
        uint8 _decimals,
        string memory _name,
        string memory _symbol,
        address _membership_db_addr
    ) BaseERC20(_totalSupply, _decimals, _name, _symbol) public
    {
        membership_contract = MembershipDB(_membership_db_addr);
    }

    function mint(address _recipient, uint256 _amount) public {
        (MembershipDB.Rank member_rank,,,,bool member_active,,) = membership_contract.get_member_stats(msg.sender);

        require(member_active == true, "You are not an active member of BaD");
        require(member_rank == MembershipDB.Rank.Board, "You have insufficient authority to mint tokens.");
        require(totalSupply + _amount >= totalSupply, "Requested mint amount must contribute to total supply");

        totalSupply += _amount;
        balanceOf[_recipient] += _amount;
        emit Transfer(address(0), _recipient, _amount);
    }

    function burn(uint256 _amount) public {
        (MembershipDB.Rank member_rank,,,,bool member_active,,) = membership_contract.get_member_stats(msg.sender);
        require(member_active == true, "You are not an active member of BaD");
        require(member_rank == MembershipDB.Rank.Board, "You have insufficient authority to burn tokens.");
        require(_amount <= balanceOf[msg.sender], "Requested burn amount exceeds amount under account");

        totalSupply -= _amount;
        balanceOf[msg.sender] -= _amount;
        emit Transfer(msg.sender, address(0), _amount);
    }

    function burnFrom(address _from, uint256 _amount) public {
        (MembershipDB.Rank member_rank,,,,bool member_active,,) = membership_contract.get_member_stats(msg.sender);
        require(member_active == true, "You are not an active member of BaD");
        require(member_rank == MembershipDB.Rank.Board, "You have insufficient authority to delegate burning ability.");

        require(_amount <= balanceOf[_from], "Not enough tokens under ownership");
        require(_amount <= allowance[_from][msg.sender], "Not authorized to execute transaction");

        totalSupply -= _amount;
        balanceOf[_from] -= _amount;
        allowance[_from][msg.sender] -= _amount;
        emit Transfer(_from, address(0), _amount);
    }
}
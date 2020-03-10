pragma solidity ^0.5.8;

contract MembershipDB {
    enum Rank {Board, Member}

    struct Identification {
        string name;
        address addr;
        string email;
        string major;
        uint8 year;
    }

    struct Member {
        Identification id;
        Rank rank;
        string position;
        string date_joined;
        string date_left;
        bool is_active;
        uint256 meetings_attended;
        uint256 tokens_awarded;
    }


    // Map member names to strings
    mapping (string => address) public name_to_addr_db;
    // Core Map, get member data usingthe address
    mapping (address => Member) membership_db;

    // create the board
    constructor() public {
        // bootstrap, create founders
        Identification memory jzlong_id = Identification("John Long", 0xa60e4B2e7b460dA30eb6018e68C07d0f0cf8471B,
                                                         "jzlong@ucdavis.edu", "CSE", 2);
        Member memory jzlong_member = Member(jzlong_id, Rank.Board, "Head Instructor", "01012000", "11192018", true, 25, 0);
        membership_db[0xa60e4B2e7b460dA30eb6018e68C07d0f0cf8471B] = jzlong_member;

    }

    // BOARD ACCESS
    function add_member(address _member_addr, string memory _name, string memory _email, string memory _major,
                        uint8 _year, Rank _rank, string memory _position, string memory _date_joined) public returns (bool)
    {
        require(membership_db[msg.sender].rank == Rank.Board, "You have insufficient authority to add members");
        require(membership_db[msg.sender].is_active == true, "You are not an active member of BaD");

        Identification memory new_member_id = Identification(_name, _member_addr, _email, _major, _year);
        name_to_addr_db[_name] = _member_addr;

        Member memory new_member_details = Member(new_member_id, _rank, _position, _date_joined, 0, true, 0, 0);
        membership_db[_member_addr] = new_member_details;

        return true;
    }

    // BOARD ACCESS
    function remove_member(address _member_addr, string memory _date_left, string memory _reason_left) public returns (bool)
    {
        require(membership_db[msg.sender].rank == Rank.Board, "You have insufficient authority to remove members");
        require(membership_db[msg.sender].is_active == true, "you are not an active member of BaD");
        membership_db[_member_addr].date_left = _date_left;
        membership_db[_member_addr].is_active = false;
        return true;
    }

    // PUBLIC AND BOARD
    function get_member_id(address _member_addr) public view returns (string memory, address, string memory, string memory, uint8)
    {
        Identification storage member_id = membership_db[_member_addr].id;
        return (member_id.name, member_id.addr, member_id.email, member_id.major, member_id.year);
    }

    // PUBLIC AND BOARD
    function get_member_stats(address _member_addr) public view returns (Rank, string memory, string memory, string memory,
                                                                         bool, uint256, uint256)
    {
        Member storage member_stats = membership_db[_member_addr];
        return (member_stats.rank, member_stats.position, member_stats.date_joined, member_stats.date_left, member_stats.is_active,
                member_stats.meetings_attended, member_stats.tokens_awarded);

    }

    // BOARD ONLY
    function promote_rank(address _member_addr) public {
        require(membership_db[msg.sender].rank == Rank.Board, "You have insufficient authority to promote members");
        require(membership_db[_member_addr].rank == Rank.Member, "The member selected is not suitable for promotion");
        require(membership_db[_member_addr].is_active == true, "The member selected is no longer part of BaD");

        membership_db[_member_addr].rank = Rank.Board;
    }

    // BOARD ONLY
    function demote_rank(address _member_addr) public {
        require(membership_db[msg.sender].rank == Rank.Board, "You have insufficient authority to promote members");
        require(membership_db[_member_addr].rank == Rank.Member, "The member selected is not suitable for demotion");
        require(membership_db[_member_addr].is_active == true, "The member selected is no longer part of BaD");

        membership_db[_member_addr].rank = Rank.Member;
    }


    // ProjectDB?

}
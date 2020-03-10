pragma solidity ^0.5.8;

import "./MembershipDB.sol";

contract ProposalsDB is MembershipDB {

    struct Vote {
        Member voter;
        bool vote;
        bool exists;
    }

    struct Proposal {
        uint256 id;
        Member proposee;
        string name;
        string description;
        string url;
        uint256 proposal_date;
        uint256 decision_date;
        bool pass;
        bool allow_voting;
        mapping (address => Vote) votes;
        uint256 votes_in_favor;
        uint256 votes_against;
        uint256 total_votes;
    }

    // Mapping that maps a proposal id to a proposal
    mapping (uint256 => Proposal) proposal_db;
    // Total Number of proposals
    uint256 total_proposals;

    // Intitalize the total number of proposals to 0
    constructor() public {
        total_proposals = 0;
    }

    // Function to create a new proposal
    function create_new_proposal (string memory _name, string memory _description, 
        string memory _url, uint256 _proposal_date) public returns (bool)
    {
        // Require that voter is a member and exists
        require (membership_db[msg.sender].id.year > 0, "Proposee isn't a member or doesn't exist");

        // Get the Member of proposee from the membership database
        Member _proposee = membership_db[msg.sender];
        // Create the proposal and add it to the proposal databse
        Proposal memory _proposal = Proposal (total_proposals, _proposee, _name, _description, _url, 
            _proposal_date, _proposal_date + 1000 , false, true, 0, 0, 0);
        proposal_db[total_proposals] = _proposal;
        // Increment the total number of proposals
        total_proposals++;
        return true;
    }

    function vote_on_proposal (uint256 _proposal_id, bool _vote) public returns (bool)
    {
        // Require that the proposal id is correct
        require (_proposal_id < total_proposals, "Proposal id is incorrect");
        // Require that the proposal is open for voting
        require (proposal_db[_proposal_id].allow_voting, "Proposal is not open for voting");
        // Require that voter is a member and exists
        require (membership_db[msg.sender].id.year > 0, "Voter isn't a member or doesn't exist");
        // Require that the voter hasn't voted before
        require (proposal_db[_proposal_id].votes[msg.sender].exists, "Voter has voted before");

        Proposal storage _proposal = proposal_db[_proposal_id];

        if (_vote == true)
        {
            _proposal.votes_in_favor++;
        }
        else 
        {
            _proposal.votes_against++;
        }

        _proposal.votes[msg.sender] = Vote(membership_db[msg.sender], _vote, true);
        proposal_db[_proposal_id].allow_voting = true;

        _proposal.total_votes++;
        
        return true;
    }

    // Function that returns the total number of proposals
    function get_total_proposals () public returns (uint256) {
        return total_proposals;
    }

    // Function that returns the proposal by corresponding to the given id
    // [NOT ABLE TO RETURN INDIVIDUAL VOTE] [NEEDS FURTHER DISCUSSION]
    function get_proposal_by_id (uint256 id) public returns (uint256, address, string memory, string memory,
        string memory, uint256, uint256, bool, bool, uint256, uint256, uint256) 
    {
        Proposal storage _proposal = proposal_db[id];

        // Return sequence - Proposee address, Name, Description, Url, Proposal Date, Decision Date,
        // Passing, Allow Voting, Votes in favor, Votes against, Total Votes
        return (id, _proposal.proposee.id.addr, _proposal.name, _proposal.description, _proposal.url, 
            _proposal.proposal_date, _proposal.decision_date, _proposal.pass, _proposal.allow_voting,
            _proposal.votes_in_favor, _proposal.votes_against, _proposal.total_votes);
    }

    /* 
        [UNIMPLEMENTED] [Needs further discussion]

        // Function that can allow voting for a proposal 
        function allow_voting_on_proposal (uint _proposal_id, bool allow) public returns (bool)
        {
            // Require that the proposal id is correct
            require (_proposal_id < total_proposals, "Proposal id is incorrect");
            // Require that the proposal is not open for voting
            require (proposal_db[_proposal_id].allow_voting == false, "Proposal is already open for voting");
            // Require that the person who can allow/dissalow be the person who introduced it
            require (proposal_db[_proposal_id].proposee.id.addr == msg.sender, "Only proposee can allow voting");

            proposal_db[_proposal_id].allow_voting = true;
        }

        // Function that can allow voting for a proposal
        function disallow_voting_on_proposal (uint _proposal_id, bool allow) public returns (bool)
        {
            // Require that the proposal id is correct
            require (_proposal_id < total_proposals, "Proposal id is incorrect");
            // Require that the proposal is not open for voting
            require (proposal_db[_proposal_id].allow_voting == true, "Proposal is already not open for voting");
            // Require that the person who can allow/dissalow be the person who introduced it
            require (proposal_db[_proposal_id].proposee.id.addr == msg.sender, "Only proposee can disallow voting");

            proposal_db[_proposal_id].allow_voting = false;
        }    
    */
}
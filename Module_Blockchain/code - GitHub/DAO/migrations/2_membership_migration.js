const Migrations = artifacts.require("Membership");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
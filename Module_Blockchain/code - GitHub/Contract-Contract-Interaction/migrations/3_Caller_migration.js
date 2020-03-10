const Migrations = artifacts.require("Caller");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
const Migrations = artifacts.require("BaDToken");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
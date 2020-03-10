const Migrations = artifacts.require("Callee");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
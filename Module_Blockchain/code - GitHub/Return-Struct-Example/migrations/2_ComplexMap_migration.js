const Migrations = artifacts.require("ComplexMap");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
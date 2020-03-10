var Migrations = artifacts.require("./show_num.sol");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};

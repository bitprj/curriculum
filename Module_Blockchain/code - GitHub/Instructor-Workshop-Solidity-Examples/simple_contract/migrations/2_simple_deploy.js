// 2_simple_deploy.js: Facilitates migration of your contract onto the
//                     development network of your choice

// NOTE: The only difference between this file and the "1_initial_migration.js"
// file that Truffle automatically generates is the argument to `.require()` 
// is our contract instead of the Migration.sol contract

var Migrations = artifacts.require("Simple");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
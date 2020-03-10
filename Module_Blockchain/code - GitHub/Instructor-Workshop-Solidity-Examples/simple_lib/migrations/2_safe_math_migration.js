var SafeMathLib = artifacts.require("SafeMathLib");
var SafeMathExtern = artifacts.require("SafeMathExtern");

module.exports = function(deployer) {
    deployer.deploy(SafeMathLib);
    deployer.link(SafeMathLib, SafeMathExtern);
    deployer.deploy(SafeMathExtern);
}
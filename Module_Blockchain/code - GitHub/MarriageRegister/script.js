var app = angular.module('marriageApp', []);

var contract_address = "0x3fc066B19562b43b86dcf07a7a0E7bb5c336fd92";
var abi = [{"constant":false,"inputs":[{"internalType":"string","name":"husband","type":"string"},{"internalType":"string","name":"wife","type":"string"}],"name":"newMarriage","outputs":[{"internalType":"uint256","name":"uid","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"getMarriages","outputs":[{"components":[{"internalType":"string","name":"husband","type":"string"},{"internalType":"string","name":"wife","type":"string"},{"internalType":"uint256","name":"date","type":"uint256"}],"internalType":"struct MarriageRegister.Marriage[]","name":"_resgister","type":"tuple[]"}],"payable":false,"stateMutability":"view","type":"function"}]

var provider =  new ethers.providers.EtherscanProvider('rinkeby');
var contract = new ethers.Contract(contract_address, abi, provider);

var privateKey = 'INSERT_PRIVATE_KEY';
var wallet = new ethers.Wallet(privateKey, provider);

app.controller('marriageCtrl', ['$scope', function($scope) {
	$scope.marriages = [];

	$scope.add_Marriage = function(husband, wife) {
		var contractWithSigner = contract.connect(wallet);
		contractWithSigner.newMarriage(husband, wife)
			.then(result => {
				console.log(result)
				$scope.get_Marriage()
			})
	}
	
	$scope.get_Marriage = function(husband, wife) {
		contract.getMarriages()
			.then(result => {
				$scope.marriages = result
				$scope.$apply();
			})
	}
	
	window.onload = $scope.get_Marriage()

  $scope.timestamp_To_Date = function(timestamp) {
		dateObj = new Date(timestamp * 1000); 
		console.log(timestamp)
    return dateObj.toDateString(); 
  }	

}]);
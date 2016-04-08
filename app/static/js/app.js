function tableData(data) {

	var app = angular.module('swestaurantApp', []);

	app.controller('sortTableCtrl', ['$scope', '$location', function($scope, $location) {
	    $scope.sortType = 'id'; // set the default sort type
	    $scope.sortReverse = false;  // set the default sort order
	    $scope.data = data;
	}]);

	app.config(['$interpolateProvider', function($interpolateProvider) {
	    $interpolateProvider.startSymbol('{[');
	    $interpolateProvider.endSymbol(']}');
	}]);
}
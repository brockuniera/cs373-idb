function setupAngSort (data) {
    var app = angular.module('sortApp', []);

    app.controller('mainController', function($scope) {
        $scope.sortType     = 'id'; // set the default sort type
        $scope.sortReverse  = false;  // set the default sort order

        $scope.data = data;

    });

    app.config(['$interpolateProvider', function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[');
        $interpolateProvider.endSymbol(']}');
    }]);
}

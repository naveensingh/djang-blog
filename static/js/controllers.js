articlesapp.controller("ArticleController", ["$scope", "$routeParams", "$http",
        function($scope, $routeParams, $http){
            $http.get('/api/v1/articles/view/?format=json', {msg:'hello word!'}).
                  then(function(response) {
                    $scope.posts = response.data;
                    console.log("Getting the data from api");
                  }, function(response) {
                    console.log(response.status);
                    console.log("getting an error with api");
                  });
        }
]);
articlesapp.controller('NewArticleController', ["$scope", "$rootScope", "Article", "$location",
    function ($scope, $rootScope, Article, $location) {
        $rootScope.PAGE = "new";
        $scope.article = new Article({
            title:      ['', 'text'],
            content:    ['', 'text'],
            category:   ['', 'text']
        });

        $scope.save = function () {
            if ($scope.newArticle.$invalid) {
                $scope.$broadcast('record:invalid');
            } else {
                $scope.article.$save();
                $location.url('/add');
            }
        };
    }]);
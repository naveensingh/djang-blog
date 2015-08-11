articlesapp.controller("ArticleController", ["$scope", "$routeParams", "$http",
        function($scope, $routeParams, $http){
            $http.get('/api/v1/articles/?format=json', {msg:'hello word!'}).
                  then(function(response) {
                    $scope.posts = response.data;
                    console.log("Getting the data from api");
                  }, function(response) {
                    console.log(response.status);
                    console.log("getting an error with api");
                  });
        }
]);
articlesapp.controller('NewArticleController', function ($scope, $rootScope, Article, $location) {
        $rootScope.PAGE = "new";
        $scope.article = new Article({
            firstName: ['', 'text'],
            lastName:  ['', 'text'],
            email:     ['', 'email'],
            homePhone: ['', 'tel'],
            cellPhone: ['', 'tel'],
            birthday:  ['', 'date'],
            website:   ['', 'url'],
            address:   ['', 'text']
        });

        $scope.save = function () {
            if ($scope.newContact.$invalid) {
                $scope.$broadcast('record:invalid');
            } else {
                $scope.contact.$save();
                $location.url('/contacts');
            }
        };
    })
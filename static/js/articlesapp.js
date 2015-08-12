var articlesapp = angular.module("ArticlesApp", ["ngRoute", "ngResource"]);

articlesapp.config(["$routeProvider", "$httpProvider", "$locationProvider",
    function($routeProvider, $httpProvider, $locationProvider) {
        $httpProvider.defaults.xsrfCookieName = "csrftoken";
        $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
        $routeProvider
            .when("/", {
                templateUrl: "/static/partials/list.html",
                controller: "ArticleController"
            })
            .when("/article/add", {
                controller: "NewArticleController",
                templateUrl:"/static/partials/articlesform.html"
            })
            .otherwise('/');
    }
]);

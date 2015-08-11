var articlesapp = angular.module("ArticlesApp", ["ngRoute"]);

articlesapp.config(["$routeProvider", "$httpProvider", "$locationProvider",
    function($routeProvider, $httpProvider, $locationProvider) {
        $httpProvider.defaults.xsrfCookieName = "csrftoken";
        $httpProvider.defaults.xsrfHeaderName = "X-CSRFToken";
        $routeProvider
            .when("/", {
                templateUrl: "/static/partials/list.html",
                controller: "ArticleController"
            })
            //.when("/add", {
            //    templateUrl:"/static/partials/articleform.html"
            //})
            .otherwise('/');
    }
]);

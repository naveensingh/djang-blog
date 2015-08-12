articlesapp.factory("Article", function($resource){
    console.log("logging resource");
    console.log($resource);
    console.log("logging resource");
    return $resource("/api/v1/articles/", {
        "update": {method:"PUT"}
    })
});
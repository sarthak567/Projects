var app = angular.module('movieModule', []);
app.controller('movieController', function ($scope) {
    $scope.movies = [
        {
            image: "images/captainamerica.jpg",
            moviename: "CAPTAIN AMERICA",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/martian.jpg",
            moviename: "MARTIAN",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/thor.jpg",
            moviename: "THOR",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/wonderwoman.jpg",
            moviename: "WONDER WOMAN",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/batmanvssuperman.jpg",
            moviename: "BATMAN VS SUPERMAN",
            like: 0,
            dislike: 0,
            notseen: 0
        },
    ]
    $scope.likeincrement = function (data) {
        data.like++;
    }

    $scope.dislikeincrement = function (data) {
        data.dislike++;
    }

    $scope.notseenIncrement = function (data) {
        data.notseen++;
    }
});

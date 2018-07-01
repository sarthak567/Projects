var app = angular.module('movieModule', []);
app.controller('movieController', function ($scope) {
    $scope.movies = [
        {
            image: "images/img1.jpg", //provide own image
            moviename: "abc",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/img2.jpg",
            moviename: "newmovie",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/img3.jpg",
            moviename: "check it",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/img4.jpg",
            moviename: "another movie",
            like: 0,
            dislike: 0,
            notseen: 0
        },
        {
            image: "images/img5.jpg",
            moviename: "final movie",
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

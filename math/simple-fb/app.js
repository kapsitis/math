'use strict';


//var app = angular.module('simpleApp', [ 'ngRoute', 'firebase']);

var app = angular.module("simpleApp", ['ngRoute', 'firebase']);

//app.constant('FIREBASE_GAME', 'https://nim-game.firebaseio.com/');

app.config(function ($routeProvider) {
  $routeProvider
    .when('/', {
      templateUrl: 'index.html', 
	  controller: 'SimpleCtrl'
    })
    .otherwise({
      redirectTo: '/'
    });
});








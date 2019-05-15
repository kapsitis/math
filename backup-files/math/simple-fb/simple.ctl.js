'use strict';


//var app = angular.module("simpleApp", ["firebase"]);
app.controller("SimpleCtrl", function($scope, $firebaseObject) {
  var ref = new Firebase("https://nim-game.firebaseio.com/1");
  // download the data into a local object
  var syncObject = $firebaseObject(ref);
  // synchronize the object with a three-way data binding
  // click on `index.html` above to see it used in the DOM!
  syncObject.$bindTo($scope, "data");
});

/*
app.controller("SimpleCtrl", function($scope, $firebaseObject) {
  var ref = new Firebase("https://nim-game.firebaseio.com/");

  // download the data into a local object
  //$scope.data = $firebaseObject(ref.child('profiles').child('physicsmarie'));
   $scope.profile = $firebaseObject(ref.child('nim-game').child('1'));

  // putting a console.log here won't work, see below
});

*/




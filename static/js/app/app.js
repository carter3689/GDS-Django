var app = angular.module("gdsMain", [])

app.controller("ourServices", function($scope){
  var services = {
    taxes:["Electronic Submittals","No Waiting","Detailed outline of required docs to expedite this service"],
    bookkeeping:["Pre approved tax loans up to $1,800.00","Direct Deposit Available","•	Annual book keeping and accounting services for your business"],
    team:["Family friendly","Willing to start at A and work with you all the way to Z covering all your needs","Dedicated to making sure you are in the best position","Always going to provide accurate data","Licensed","Proactive in our efforts for you at all times"]
  }
  $scope.services = services;
})

//CLIENT_ID = '262629809948-h9kbu2b9osj7k046hm3nuou0d6d70qsu.apps.googleusercontent.com'
//CLIENT_SECRET = '6QEOPqV3v6IrKGdVVfZxEG0h'
//API_KEY = 'AIzaSyBQypOZ4JK4gjGm4ywWQMlKAOpdEdPC-a4'

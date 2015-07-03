var PloneConfTalks = angular.module('PloneConfTalks', []);

PloneConfTalks
  .controller('PloneConfTalksSubmit', ['$scope', '$http', '$timeout', function ($scope, $http, $timeout) {
    $scope.talk = {};
    $scope.speakers = [];
    $scope.talk_disabled = false;
    $scope.number_of_speakers = 1;

    $scope.repeat = function(num) {
      return Array.apply(null, Array(num)).map(function (_, i) {return i;});
    };

    $scope.isTerminal = function(num) {
      return num == $scope.number_of_speakers - 1;
    };

    $scope.isCoSpeaker = function(num) {
      return $scope.number_of_speakers > 1 && $scope.isTerminal(num);
    };

    $scope.increaseNumberOfSpeakers = function() {
      $scope.number_of_speakers = $scope.number_of_speakers + 1;
    };

    $scope.decreaseNumberOfSpeakers = function() {
      $scope.number_of_speakers = $scope.number_of_speakers - 1;
      $scope.speakers.pop();
    };

    $scope.disableTalk = function() {
      $scope.talk_disabled = true;
    };

    $scope.enableTalk = function() {
      $scope.talk_disabled = false;
    };

    $scope.talkValid = function() {
      return $scope.submitTalk.talk_title.$valid &&
             $scope.submitTalk.talk_summary.$valid &&
             $scope.submitTalk.talk_audience.$valid;
    };

    $scope.tryGetGitPhotoLink = function(num) {
      if($scope.speakers[num] && $scope.speakers[num].git) {
        if($scope.speakers[num].git.indexOf("github.com") > -1) {
          var input = $scope.speakers[num].git.split("/");
          if(input[0].indexOf("http") > -1) {
            $scope.speakers[num].git = input[3];
          }
          else {
            $scope.speakers[num].git = input[1];
          }
        }
        $http.get("https://api.github.com/users/" + $scope.speakers[num].git).success(function(response) {
          $scope.speakers[num].git_image_url = response.avatar_url;
          if($scope.speakers[num].git_image_url && !$scope.speakers[num].image_url) {
            $scope.speakers[num].git_image_selected = "selected";
            $scope.speakers[num].git_image_deselected = "deslected";
            $scope.speakers[num].image_url = $scope.speakers[num].git_image;
          }
        });
      }
    };

    $scope.tryGetTwitterPhotoLink = function(num) {
      if($scope.speakers[num] && $scope.speakers[num].twitter) {
        if($scope.speakers[num].twitter.indexOf("twitter.com") > -1) {
          var input = $scope.speakers[num].twitter.split("/");
          if(input[0].indexOf("http") > -1) {
            $scope.speakers[num].twitter = input[3];
          }
          else {
            $scope.speakers[num].twitter = input[1];
          }
          $scope.speakers[num].twitter = $scope.speakers[num].twitter.replace('@', '');
          $scope.speakers[num].twitter = $scope.speakers[num].twitter.replace('#', '');
        }
        $scope.speakers[num].twitter_image_url = "http://avatars.io/twitter/" + $scope.speakers[num].twitter + "?size=large";
        if(!$scope.speakers[num].image_url) {
          $scope.speakers[num].twitter_image_selected = "selected";
          $scope.speakers[num].git_image_selected = "deselected";
          $scope.speakers[num].image_url = $scope.speakers[num].twitter_image_url;
        }
      }
    }

    $scope.selectTwitterImage = function(num) {
      $scope.speakers[num].git_image_selected = "deselected";
      $scope.speakers[num].twitter_image_selected = "selected";
      $scope.speakers[num].image_url = $scope.speakers[num].twitter_image_url;
    };

    $scope.selectGitImage = function(num) {
      $scope.speakers[num].git_image_selected = "selected";
      $scope.speakers[num].twitter_image_selected = "deselected";
      $scope.speakers[num].image_url = $scope.speakers[num].git_image_url;
    };
  }])

  .directive('validFile',function(){
  return {
    require:'ngModel',
    link: function(scope, el, attrs, ngModel){
      el.bind('change', function(){
        scope.$apply(function(){
          ngModel.$setViewValue(el.val());
          ngModel.$render();
        });
      });
    }
  }
});
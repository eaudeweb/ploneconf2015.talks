var PloneConfTalks = angular.module('PloneConfTalks', []);

PloneConfTalks
  .controller('PloneConfTalksSubmit', ['$scope', '$http', '$timeout', function ($scope, $http, $timeout) {
    $scope.talk = {};
    $scope.speakers = [];
    $scope.talk_disabled = false;
    $scope.number_of_speakers = 1;
    $scope.speakers_indexes = [0];
    $scope.default_image_url = "/++theme++ploneconf2015.theme/img/avatar-placeholder.svg";

    $scope.repeat = function(num) {
      return $scope.speakers_indexes;
    };

    $scope.isTerminal = function(num) {
      return num == $scope.number_of_speakers - 1;
    };

    $scope.isCoSpeaker = function(num) {
      return num > 0;
    };

    $scope.increaseNumberOfSpeakers = function() {
      $scope.speakers_indexes.push($scope.number_of_speakers);
      $scope.number_of_speakers = $scope.number_of_speakers + 1;
    };

    $scope.decreaseNumberOfSpeakers = function() {
      $scope.speakers_indexes.pop();
      $scope.number_of_speakers = $scope.number_of_speakers - 1;
      $scope.speakers.pop();
    };

    $scope.removeCoSpeaker = function(num) {
      delete $scope.speakers[num];
      delete $scope.speakers_indexes.splice($scope.speakers_indexes.indexOf(num), 1);
    };

    $scope.disableTalk = function() {
      $scope.talk_disabled = true;
    };

    $scope.enableTalk = function() {
      $scope.talk_disabled = false;
    };

    $scope.submitTalkValid = function() {
      return $scope.submitTalk.talk_title.$valid &&
             $scope.submitTalk.talk_summary.$valid &&
             $scope.submitTalk.talk_audience.$valid;
    };

    $scope.tryGetGitPhotoLink = function(num) {
      if($scope.speakers[num].git_image_selected) {
        $scope.speakers[num].image_url = "";
      }
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
            $scope.speakers[num].git_image_selected = "is_selected";
            $scope.speakers[num].twitter_image_selected = "";
            // $scope.speakers[num].default_image_selected = "";
            $scope.speakers[num].image_url = $scope.speakers[num].git_image_url;
          }
        });
      }
      if($scope.speakers[num] && !$scope.speakers[num].git) {
        $scope.speakers[num].git_image_url = "";
        $scope.speakers[num].selectAvailableImage(num);
      }
    };

    $scope.tryGetTwitterPhotoLink = function(num) {
      if($scope.speakers[num].twitter_image_selected) {
        $scope.speakers[num].image_url = "";
      }
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
          $scope.speakers[num].twitter_image_selected = "is_selected";
          $scope.speakers[num].git_image_selected = "";
          // $scope.speakers[num].default_image_selected = "";
          $scope.speakers[num].image_url = $scope.speakers[num].twitter_image_url;
        }
      }
      if($scope.speakers[num] && !$scope.speakers[num].twitter) {
        $scope.speakers[num].twitter_image_url = "";
        $scope.selectAvailableImage(num);
      }
    }

    $scope.selectAvailableImage = function(num) {
      if($scope.speakers[num] && $scope.speakers[num].git_image_url) {
        $scope.selectGitImage(num);
      }
      else if($scope.speakers[num] && $scope.speakers[num].twitter_image_url) {
        $scope.selectTwitterImage(num);
      }
      else {
        $scope.deselectImage(num);
      }     
    };

    $scope.selectTwitterImage = function(num) {
      $scope.speakers[num].git_image_selected = "";
      // $scope.speakers[num].default_image_selected = "";
      $scope.speakers[num].twitter_image_selected = "is_selected";
      $scope.speakers[num].image_url = $scope.speakers[num].twitter_image_url;
    };

    $scope.selectGitImage = function(num) {
      $scope.speakers[num].git_image_selected = "is_selected";
      // $scope.speakers[num].default_image_selected = "";
      $scope.speakers[num].twitter_image_selected = "";
      $scope.speakers[num].image_url = $scope.speakers[num].git_image_url;
    };

    $scope.deselectImage = function(num) {
      if(!$scope.speakers[num]) {
        $scope.speakers[num] = {};
      }
      $scope.speakers[num].git_image_selected = "";
      $scope.speakers[num].twitter_image_selected = "";
      $scope.speakers[num].image_url = "";
    };
    // $scope.selectDefaultImage = function(num) {
      // $scope.speakers[num].default_image_selected = "is_selected";
      // $scope.speakers[num].git_image_selected = "";
      // $scope.speakers[num].twitter_image_selected = "";
      // $scope.speakers[num].image_url = $scope.default_image_url;
    // };

    $scope.getImageURL = function(num) {
      if(!$scope.speakers[num] || !$scope.speakers[num].image_url) {
	return "";
      }
      // if(!$scope.speakers[num].image_url) {
      //   $scope.speakers[num].image_url = $scope.default_image_url;
      // }
      return $scope.speakers[num].image_url;
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

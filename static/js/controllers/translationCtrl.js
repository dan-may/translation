var translationApp = angular.module('translationApp', ['gettext', 'translationApp.controllers']);

translationApp.run(function (gettextCatalog) {
    gettextCatalog.debug = true;
    console.log(gettextCatalog.currentLanguage);
    gettextCatalog.currentLanguage = 'en';
    console.log(gettextCatalog.currentLanguage);
});

var translationAppControllers = angular.module('translationApp.controllers', []);

translationAppControllers.controller('TranslationCtrl', ['$scope', '$location', 'gettextCatalog', 'gettext', function($scope, $location, gettextCatalog, gettext) {

	/// This is a translator comment
	var comment = gettext("Hello");
    $scope.comment = comment;

    // Replicate settings strings from data
    var string = 'Another piece of text';
    $scope.another = gettextCatalog.getString(string);

    /// Another comment for the translator: translate as plural please
    var myString2 = gettextCatalog.getPlural(3, "One Bird", "{{$count}} Birds", {});

    console.log('Went into the controller');

    $scope.translateFR = function () {
        console.log('translating to french');
        console.log(gettextCatalog.currentLanguage);
        gettextCatalog.setCurrentLanguage('fr');
        console.log(gettextCatalog.currentLanguage);
        console.log(gettextCatalog);
    };

    $scope.translateEN = function () {
        console.log('translating to english');
        console.log(gettextCatalog.currentLanguage);
        gettextCatalog.setCurrentLanguage('en');
        console.log(gettextCatalog.currentLanguage);
        console.log(gettextCatalog);
    };


	if ($location.path() === '') {
		$location.path('/');
	}


    //// Language switcher
    //$scope.languages = {
    //    current: gettextCatalog.currentLanguage,
    //    available: {
    //    'fr': 'Francais',
    //    'en': 'English'
    //    }
    //};
    //
    //$scope.$watch('languages.current', function (lang) {
    //    if (!lang) {
    //        return;
    //    }
    //
    //    gettextCatalog.setCurrentLanguage(lang);
    //});
}]);

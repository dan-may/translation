angular.module('translationApp').run(['gettextCatalog', function (gettextCatalog) {
/* jshint -W100 */
    gettextCatalog.setStrings('fr', {"A big translatable list of fruit":"Une grande liste de fruit translatable","blueberries":"bleuberrie","cranberries":"cranberrie","Hello":"Allo","kiwi":"kioui","lychees":"lichee","One Bird":["Une bird","Des birds"],"raspberries":"raspberrie"});
/* jshint +W100 */
}]);
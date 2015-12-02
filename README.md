# Translation test project

1. setup a virtual environment
2. pip install from requirements.txt
3. bower install
4. install Grunt
5. npm install

Run from views.py (localhost:5000/fruits)

## Translating Flask templates:
```python
@babel.localeselector
def get_locale():
    return 'fr'
```

Switch between 'en' and 'fr'. Babel handles the installing of languages.

## Translating Angular templates

```javascript
$scope.translateFR = function () {
    console.log('translating to french');
    gettextCatalog.setCurrentLanguage('fr');
};

$scope.translateEN = function () {
    console.log('translating to english');
    gettextCatalog.setCurrentLanguage('en');
};
```

Go to localhost:5000/fruits-angular and click the EN and FR button to change between languages.
Languages are read from the translation.js file that is compiled by the Grunt task nggettext_compile (see Gruntfile.js)



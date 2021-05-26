# Learning Django
> Building a Polls application using Django

## Steps :
1. Creating a Project
1. Setup Models
1. Setup Admin
1. Setup Views
1. Setup/Map URLs
1. Write Tests

### Creating a Project
`$ django-admin startproject mysite`

#### Directory structure of mysite
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

### Setting up Views
A view should do one of the following :
- Return `HttpResponse`
- Raise `Http404`

#### Idioms and corresponding Shortcuts
#1\
\
Load a template > Fill a context > Render the template (with the context) > Return `HttpResponse`\
**_Shortcut_** : `render()`\
**_Syntax_** : `render( request, template, context )`\
**_Example_** : `render( request, 'polls/index.html', { 'latest_question_list' : latest_question_list } )`

#2\
\
Get an object from model > Raise `Http404` if object doesn't exist\
**_Shortcut_** : `get_object_or_404()`\
**_Syntax_** : `get_object_or_404( Model, Query )`\
**_Example_** :  `get_object_or_404( Question, pk='23' )`
> There’s also a `get_list_or_404()` function, which works just as `get_object_or_404()` – except using `filter()` instead of `get()`. It raises `Http404` if the list is empty.


### Setting up URLs
> Using URL Configuration objects (URLConf)


#### Directory Structure :
```
mysite/
	...
	urls.py #Maps url patterns to URLConfs in apps
	app/
		...
		urls.py #Maps url patterns to Views
```

#### Structure of urls.py
```
# Imports
urlpatterns = [
	url(regex, view [, kwargs[, name ]])
]
```
`view` : When a url matches the given regex, the `HttpRequest` object is passed to the view, along with captured values in the regex as arguments.
> **How to capture named args/values ?**
> Using the pattern `?P<argument_name>` inside a capture in the regex.
> Example : `r'(?P<q_id>[0-9]+)'`

`name` : Naming your URL lets you refer to it unambiguously from elsewhere in Django especially templates.\
Example : `<a href="{% url 'urlName' argName %}"></a>`

> **Notes**
> When somebody requests a page from your Web site – say, “/polls/34/”, Django will load the `mysite.urls` Python module because it’s pointed to by the `ROOT_URLCONF` setting. It finds the variable named urlpatterns and traverses the regular expressions in order. The `include()` functions we are using simply reference other URLconfs. Note that the regular expressions for the `include()` functions don’t have a `$` (end-of-string match character) but rather a trailing slash. Whenever Django encounters `include()`, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.
> The idea behind `include()` is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (`polls/urls.py`), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

### Namespacing URL names

How does Django differentiate the URL names between the different apps of a project? For example, the `polls` app has a `detail` view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the `{% url %}` template tag?\
Answer : Add namespaces to your root URLconf !
```
mysite/urls.py
--------------
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
```

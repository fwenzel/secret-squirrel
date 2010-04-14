Secret Squirrel
===============

Secret Squirrel is a [Django][Django]-based [Single Sign-on][SSO] server. It
uses [CAS][CAS] (version 1) as the client-side protocol and can be used with
any [CAS client library][CAS-libs].

Secret Squirrel is a [Mozilla][Mozilla] project and published under a BSD
license.

[Django]: http://www.djangoproject.com/
[SSO]: http://en.wikipedia.org/wiki/Single_sign-on
[CAS]: http://en.wikipedia.org/wiki/Central_Authentication_Service
[CAS-libs]: http://www.ja-sig.org/wiki/display/CASC
[Mozilla]: http://www.mozilla.org

Getting Started
---------------
### Python
You need Python 2.6. Also, you probably want to run this application in a
[virtualenv][virtualenv] environment.

Run ``easy_install pip`` followed by ``pip install -r requirements.txt``
to install the required Python libraries.

[virtualenv]: http://pypi.python.org/pypi/virtualenv

### Django
The Internet has plenty of of documentation on setting up a Django application
with any web server. If you need a wsgi entry point, you can find one in
``wsgi/squirrel.wsgi``.

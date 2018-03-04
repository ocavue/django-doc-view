django-doc-view: The simplest way to document your Django APIs.
===============================================================

`django-doc-view` find view's docsting and output them in shell after formatting.

Installation
------------

.. code:: bash

    pip3 install django-doc-view

Base Usage
----------

Add `django_doc_view` to your INSTALLED_APPS setting:

.. code:: python

    # settings.py

    INSTALLED_APPS = (
        ...
        'django_doc_view'
    )

Then you can get the result by doc_view command:

.. code:: bash

    python3 manage.py doc_view


Example
-------

.. code:: python

    def index(request):
        """
        A example of Function-based view
        """
        return HttpResponse("Hello, world. You're at the polls index.")


    class User(View):
        """
        A example of Class-based view

        method:
            get
        request:
            id
        """

        def get(self, request, *args, **kwargs):
            ...


.. code:: shell

    $ python3 manage.py doc_view

    ## polls/

        A example of Function-based view

    ## polls/user

        A example of Class-based view

        method:
            get
        request:
            id

You can find a runnable example from [here](https://github.com/ocavue/django-doc-view-emample).

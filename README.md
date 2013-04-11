Django-stripe-payments Example
==============================

This is an example site installation of [django-stripe-payments](https://github.com/eldarion/django-stripe-payments).

Installation
============

To install this example site, do the following (your mileage may vary).

	$ mkvirtualenv --distribute django-stripe-payments
	$ cd ~/Sites
	$ git clone git://github.com/epicserve/dsp-example.git
	$ cd dsp-example
    $ add2virtualenv .
	$ pip install -r config/requirements/base.txt
	$ export DJANGO_SETTINGS_MODULE=config.settings
	$ django-admin.py syncdb

Add your `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` in `config/settings/local.py` and then run the following management commands.

	$ django-admin.py init_customers
	$ django-admin.py init_plans

Django-stripe-payments Example
==============================

This is an example site installation of
[django-stripe-payments](https://github.com/eldarion/django-stripe-payments).

Installation
============

To install this example site, do the following (your mileage may vary).

	$ mkvirtualenv --distribute django-stripe-payments
	$ cd ~/Sites
	$ git clone git://github.com/epicserve/dsp-example.git
	$ cd dsp-example
    $ add2virtualenv .
	$ pip install -r config/requirements/base.txt
	$ workon django-stripe-payments
	$ export DJANGO_SETTINGS_MODULE=config.settings
	$ django-admin.py syncdb

Create the file `config/settings/local.py` and add following. Change the
`STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` to match what you have in your
stripe.com account settings. Also, change the email settings to work with
your SMTP server. The following `local.py` settings file shows the settings
if you want to use your Gmail account.

	LOCAL_SETTINGS_LOADED = True

	STRIPE_PUBLIC_KEY = 'pk_test_xxxxxxxxxxxxxxxxxxxxxxxx'
	STRIPE_SECRET_KEY = 'sk_test_xxxxxxxxxxxxxxxxxxxxxxxx'

	# Example Gmail settings if you need to send email from a local Django dev
	# site. Uncomment the following and change the username and password to
	# whatever they are for your Gmail account. Make sure don't use Gmail for
	# sending email on a production website.
	EMAIL_HOST = 'smtp.gmail.com'
	EMAIL_HOST_USER = 'username@gmail.com'
	EMAIL_HOST_PASSWORD = 'xxxxxxxxxxxxxxx'
	EMAIL_PORT = 587
	EMAIL_USE_TLS = True


Add your `STRIPE_PUBLIC_KEY` and `STRIPE_SECRET_KEY` in
`config/settings/local.py` and then run the following management commands.

	$ django-admin.py init_customers
	$ django-admin.py init_plans

Now you're ready to run the example site.

	$ django-admin.py runserver 0.0.0.0:8000

You'll also need to open up a different tab in your terminal and run a service
like [localtunnel](http://progrium.com/localtunnel/) (free service) or
[Forward](https://forwardhq.com/) (paid service). The following is an example
if you use Foward.

	$ forward 8000
	Forwarding port 8000 to https://username.fwd.wf
	Ctrl-C to stop forwarding

The last step is to add https://username.fwd.wf/payments/webhook/ as a
webhook under the Webhooks tab in your stripe.com account settings.

Now you should be ready to open your browser and go to
https://username.fwd.wf/payments/subscribe in order to test
django-strip-payments using this example website.


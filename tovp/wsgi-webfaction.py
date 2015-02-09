"""
WSGI config for project project.

This module contains the WSGI application used by Django's development server
and any production WSGI deployments. It should expose a module-level variable
named ``application``. Django's ``runserver`` and ``runfcgi`` commands discover
this application via the ``WSGI_APPLICATION`` setting.

Usually you will have the standard Django WSGI application here, but it also
might make sense to replace the whole Django WSGI application with a custom one
that later delegates to the Django one. For example, you could introduce WSGI
middleware here, or combine a Django application with an application of another
framework.

"""
import os
import site
# import newrelic.agent


# activates virtualenv
site.addsitedir(
    os.path.expanduser(
        "~/Envs/tovp/lib/python3.4/site-packages"
    )
)
activate_this = os.path.expanduser(
    "~/Envs/tovp/bin/activate_this.py"
)
exec(open(activate_this).read())

# run script to set all environment variables which are used in settings
exec(open(os.path.expanduser("~/Envs/tovp/bin/set_variables.py")).read())

# **new relic
# newrelic.agent.initialize(
#     os.path.expanduser("~/webapps/jpsarchives_org/newrelic.ini")
# )

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from configurations.wsgi import get_wsgi_application
application = get_wsgi_application()

# **new relic
# application = newrelic.agent.wsgi_application()(application)

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)

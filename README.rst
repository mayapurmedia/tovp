TOVP
==============================

Temple Of The Vedic Planetarium Fundraising Website. It is used to keep track
of all donors and their pledges, contributions and assigned promotions.

.. image:: https://travis-ci.org/mayapurmedia/tovp.svg?branch=master
    :target: https://travis-ci.org/mayapurmedia/tovp
.. image:: https://coveralls.io/repos/mayapurmedia/tovp/badge.png?branch=master
    :target: https://coveralls.io/r/mayapurmedia/tovp?branch=master
.. image:: http://img.shields.io/badge/django-v1.8.7-blue.svg
.. image:: http://img.shields.io/badge/license-MIT-green.svg


Configuration expect you to have set these environment variables before
running:

- `DJANGO_CONFIGURATION` - default is `production`
- `DATABASE_URL` - dj-database-url link to your database
- `DJANGO_SECRET_KEY` - your Django Secret Key
- `ELASTICSEARCH_SERVER` - your Elasticsearch (e.g. `http://localhost:9200/`)
- `ELASTICSEARCH_INDEX_NAME` - name of your Elasticsearch index

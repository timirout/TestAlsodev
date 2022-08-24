#!/bin/bash

echo "Hello TestAlsodev!"

python manage.py migrate --settings=test_alsodev.settings.${MODE}
python manage.py collectstatic --noinput --settings=test_alsodev.settings.${MODE}
python manage.py runserver --settings=test_alsodev.settings.${MODE} 0:${WSGI_PORT}
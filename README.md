# MrRobot scavenger hunt
Pa'l desorden


#### create postgres role
```
$ sudo -u postgres psql -c "create role mrrobot_scavenger_hunt  with login password 'mrrobot_scavenger_hunt';"
$ sudo -u postgres psql -c "alter user mrrobot_scavenger_hunt with superuser;"
```

#### create postgres database
```
$ sudo -u postgres createdb mrrobot_scavenger_hunt -O mrrobot_scavenger_hunt
```

### Environment

```
$ mkvirtualenv --python=/usr/bin/python3.6 mrrobot_scavenger_hunt
$ workon mrrobot_scavenger_hunt
```

### Run migrations
```
python manage.py migrate
```

### Run Project
```
python manage.py runserver
```

### Create Superuser
```
python manage.py createsuperuser
/admin -> to see the admin page, login
```

### Create/commit new models
```
python manage.py makemigrations
python manage.py migrate
```
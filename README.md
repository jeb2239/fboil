## fboil

Extension of the updated Flask-Boilerplate project found here: https://github.com/mjhea0/flask-boilerplate/tree/master/_updated

### getting started
first create a postgresql database called flask_boilerplate

then run

	make install

next you need to set these environment variables in config/env/bin/activate
(set APP_SETTINGS to config.your_deployment_config_file on deployment)

	export APP_SETTINGS = config.development
	export SECRET_KEY="really-long-good-random-key"
	export SECURITY_PASSWORD_SALT="different-long-good-random-key"
	export MAIL_USERNAME="username99"
	export MAIL_PASSWORD="p4ssw0rd"
	
then initialize the database

	make database

finally, run

	make server

to activate the virtualenv later, run

	source config/development/env/bin/activate

to run a shell with important stuff imported

	make shell

### additions to flask-boilerplate
+ user accounts
+ email confirmation
+ password reset

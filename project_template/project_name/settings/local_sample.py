from mongoengine import connect


# MongoEngine database connection.
connect('demep')

# Make this unique, and don't share it with anybody.
SECRET_KEY = '{{ secret_key }}'

# fcgi script name fix.
#FORCE_SCRIPT_NAME = ''

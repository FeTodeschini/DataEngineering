import os

#please note that the database user names and passwords are stored in the environment variables below, so you need to create the variables in your OS.
# if you do not want to use the variables, you can hardcore the string, replacing [os.environ.get('XXXXXXXX')] by its value (such as 'admin' or 'password123', for example)
# SOURCE_DB_USER
# SOURCE_DB_PASS
# TARGET_DB_USER
# TARGET_DB_PASS

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': '192.168.0.12',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('SOURCE_DB_USER'),
            'DB_PASS': os.environ.get('SOURCE_DB_PASS')
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': '192.168.0.12',
            'DB_NAME': 'retail_db',
            'DB_USER': os.environ.get('TARGET_DB_USER'),
            'DB_PASS': os.environ.get('TARGET_DB_PASS')
        }
    }
}
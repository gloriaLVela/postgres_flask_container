import os


# Generate the URI

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_POST']

DATABASE_CONNECTION_URI = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'

# POSTGRES = {
#     'user': 'postgres',
#     'pw': 'password',
#     'db': 'test_db',
#     'host': 'localhost',
#     'port': '5432'

# }

# DATABASE_CONNECTION_URI = 'postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
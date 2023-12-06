import os

DEBUG = False


if "WEBSITE_HOSTNAME" in os.environ:
    ALLOWED_HOSTS = [os.environ["WEBSITE_HOSTNAME"]]
else:
    ALLOWED_HOSTS = []

# The PostgreSQL service binding will always set env variables with these names.

dbuser = os.environ["POSTGRES_USERNAME"]
dbpass = os.environ["POSTGRES_PASSWORD"]
dbhost = os.environ["POSTGRES_HOST"]
dbname = os.environ["POSTGRES_DATABASE"]
dbport = os.environ.get("POSTGRES_PORT", 5432)
# The PostgreSQL service binding will typically set POSTGRES_SSL to disable.
sslmode = os.environ.get("POSTGRES_SSL")
DATABASE_URI = f"postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}:{dbport}/{dbname}"
if sslmode:
    DATABASE_URI = f"{DATABASE_URI}?sslmode={sslmode}"

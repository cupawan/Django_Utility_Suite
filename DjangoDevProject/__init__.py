import pymysql
from dotenv import load_dotenv

load_dotenv("./django_utility_suite/.env")
pymysql.install_as_MySQLdb()
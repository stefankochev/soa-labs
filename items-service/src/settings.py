import os

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

API_ROOT_PATH = os.environ.get("API_ROOT_PATH", "")

# inter-service communication config
NOTIFICATIONS_SERVICE_URL = os.environ.get("NOTIFICATIONS_SERVICE_URL")

KAFKA_BROKER_HOST = os.environ.get("KAFKA_BROKER_HOST")
KAFKA_BROKER_PORT = os.environ.get("KAFKA_BROKER_PORT")
ITEMS_TOPIC = os.environ.get("ITEMS_TOPIC")

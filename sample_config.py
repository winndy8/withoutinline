import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")

    # Authorized users to use this bot

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQGDMIkAvfdYWc-mTHLyC5V0RJ597VWB5VJnYjPlTncPPhn4VkoQAiZaBbBVJkFzLm84o5p9MORq5KH8X7I__yeC8F06DUkv33QgNNyok_MSOSolX0pcoo1chYnoUEH6HoNutchkh07UmzOejZ9B3wJEe5OS7zKtkdC3gGyFEJCnZaPsd-qV9K2mLirPMv9O49PMraivxTH4D2nyzfUwRF9bCukRAMo0QYuHf6ZBrVnMKHOf7RAQ0DcdxdxTHmJJfsPMF0rJIwvzx62j6xiGrPT96O_f3uRZe_lQJEHadKNMAxAvFHPm7tGbF8YolMzMf8J6DXkq4_KcWLYgLFlUesyb6PlNbwAAAAFUPt0PAA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

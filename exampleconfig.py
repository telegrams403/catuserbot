from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 778724
    API_HASH = "d846061f0c59281db28f4895635ae1dc"
    # the name to display in your alive message
    ALIVE_NAME = "UzMaxBoy"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://obaablza:PA4zEEgkR3ZLXpcotrWlDbuE-Rl9FhJ-@trumpet.db.elephantsql.com/obaablza"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1ApWapzMBu1cWWlBfegbgZSo9IMa5e1VbRJvDnt4eJaTYF9iwvwCxQoPCrX-99D86pqZjvN6CGVYwc5Ck5DWEdcKdpp969eTH6AujmPvXXK_9PXyLP-q0JmMjyXddn1TkHQWwBMWEnJ7vj9kGv-QVHKeHb3sR3wKx8wIt4KehnRvBbwLtW_j3e0NmomW4Wg7tydt8PFkecTO9Br5CMlF15DuG8nOwDcGb1jHXjbS67kNoMX6a02lz1yCOfejuNnvcpswLIcuU3CFKt2wEhS1EHsRoEWrxxJ46vJ24bIX5O_STWrXnbymxBHUBRbdGWzyI7kvcCfUYpGOo6EobE-kbAZoaPujKHJE="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6072768222:AAGHmduySdiCekx0xtFuwpzaKyk2iSXnLss"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001907456990
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"

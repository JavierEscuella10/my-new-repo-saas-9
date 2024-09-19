import boto3, psycopg2

from decouple import config


def identify_intent(user_request):
    try:
        client = boto3.client(
            "lexv2-runtime",
            region_name="us-east-1",
            aws_access_key_id=config("ACCESS_KEY"),
            aws_secret_access_key=config("SECRET_ACCESS_KEY"),
        )

        response = client.recognize_text(
            botId="",
            botAliasId="",
            localeId="",
            sessionId="",
            text=user_request,
        )
        return response
    except Exception as e:
        pg_connection = psycopg2.connect(
            dbname=config("DB_NAME"),
            user=config("USER_NAME"),
            password=config("PASSWORD"),
            host=config("HOST"),
            port=5432,
        )
        cursor = pg_connection.cursor()
        cursor.execute(
            "INSERT INTO error_logs (occurred_while, method_name, error_message)  VALUES (%s, %s, %s)",
            ["get_intent", "connectLex", e],
        )
        pg_connection.commit()
        pg_connection.close()
        raise "An Unexpected error occurred. Please try again later."

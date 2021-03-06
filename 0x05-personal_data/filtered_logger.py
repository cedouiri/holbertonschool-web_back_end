#!/usr/bin/env python3
'''
Regex-ing

'''


import logging
import re
import mysql.connector
import os
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    '''
    class Redacting Formatter

    '''

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        '''
        Returns a log msg

        '''

        msg = logging.Formatter(self.FORMAT).format(record)
        return filter_datum(self.fields, self.REDACTION,
                            msg, self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''
    Returns a log msg

    '''
    return (separator.join(x if x.split('=')[0] not in fields else re.sub(
        r'=.*', '=' + redaction, x) for x in message.split(separator)))


def get_logger() -> logging.Logger:
    '''
    get logger

    '''

    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to my_db database."""
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", 'root')
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", '')
    host = os.getenv("PERSONAL_DATA_DB_HOST", 'localhost')
    db_name = os.getenv("PERSONAL_DATA_DB_NAME")

    cnx = mysql.connector.connect(
        host=host,
        database=db_name,
        user=user,
        password=password
    )

    return cnx


def main() -> None:
    '''
    we using get_db to obtain a database connection

    '''
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    records = cursor.fetchall()
    logger = get_logger()
    fields = [x[0] for x in cursor.description]

    for row in records:
        msg = ''
        for i in range(len(fields)):
            msg += fields[i] + '=' + str(row[i]) + ';'
        logger.info(msg)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()

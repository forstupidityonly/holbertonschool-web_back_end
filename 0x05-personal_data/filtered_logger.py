#!/usr/bin/env python3
"""pii and non-pii"""
from typing import List
import re
import logging


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """init function"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """call filter_datum with init vals"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record),
                            self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
       fields: a list of strings representing all fields to obfuscate
       redaction: a string representing by what the field will be obf
       message: a string representing the log line
       separator: a string representing by which character is separating
       must use regex and be less than 5 lines long
    """
    for field in fields:
        message = re.sub(field + "=" + ".+?" + separator,
                         field + "=" + redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """create logger"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PPI_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Redacting Formatter class."""
    db = mysql.connector.connection.MySQLConnection(
            user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
            password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
            host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=getenv('PERSONAL_DATA_DB_NAME'))

    return db

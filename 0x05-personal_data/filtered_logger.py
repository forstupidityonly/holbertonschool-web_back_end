#!/usr/bin/env python3
"""pii and non-pii"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character is separating all
        must use regex and be less than 5 lines long
    """
    for field in fields:
        message = re.sub(field + "=" + ".+?" + separator,
                         field + "=" + redaction + separator, message)
    return message

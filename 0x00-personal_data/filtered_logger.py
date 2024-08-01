#!/usr/bin/env python3
"""a module that contains filltering log functions
"""
import re
from typing import List

patterns = {
    "extract": lambda fields, separator: f"({separator.join(fields)})",
    "replace": lambda redaction: "REDACTED",
}


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str, separator: str) -> str:
    extract, replace = (patterns["extract"], patterns["replace"])
    return re.sub(extract(fields, separator), replace(redaction), message)

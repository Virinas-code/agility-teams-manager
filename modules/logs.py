#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Advanced logging.
"""
import logging
import sys
from typing import Optional, TextIO


def custom_print(
    *values: object,
    sep: Optional[str] = " ",
    end: Optional[str] = "\n",
    file: TextIO = sys.stdout,
    flush: bool = False
):
    """
    Custom print function.

    :param Optional[str] sep: String inserted between values, defaults to " "
    :param Optional[str] end: String appended after the last value,
        defaults to "\n"
    :param TextIO file: A file-like object (stream), defaults to sys.stdout
    :param bool flush: Whether to forcibly flush the stream, defaults to False
    """
    separator: str = sep if sep is not None else " "
    end_character: str = end if end is not None else "\n"
    string: str = separator.join(str(value) for value in values)
    full_string: str = string + end_character
    if file == sys.stdout:
        logging.warning("custom")
        logging.debug(string)
    elif file == sys.stderr:
        logging.error(string)
    else:
        file.write(full_string)
        if flush:
            file.flush()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Exploit.

Home page.
"""
import os

from flask import send_from_directory


def public(filename):
    """
    Send a static file.

    Page /public/<path:filename>
    """
    bruh()
    return send_from_directory(os.path.abspath("./public"), filename)


def ui(filename):
    """
    Send a static file.

    Page /ui/<path:filename>
    """
    return send_from_directory(os.path.abspath("./ui"), filename)

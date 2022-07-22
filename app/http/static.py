#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Home page.
"""
import os

import verboselogs

from flask import send_from_directory

logger: verboselogs.VerboseLogger = verboselogs.VerboseLogger(__name__)


def public(filename):
    """
    Send a static file.

    Page /public/<path:filename>
    """
    logger.spam("Sending public file %s", filename)
    return send_from_directory(os.path.abspath("./public"), filename)


def ui(filename):
    """
    Send a static file.

    Page /ui/<path:filename>
    """
    logger.spam("Sending UI file %s", filename)
    return send_from_directory(os.path.abspath("./ui"), filename)


def data(filename):
    """
    Send a data file.

    Page /data/<path:filename>
    """
    return send_from_directory(os.path.abspath("./data"), filename)

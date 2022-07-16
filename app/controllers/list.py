#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Exploit.

Home page.
"""
from flask import render_template


def list():
    """
    Computers list page.

    Page /list.
    """
    return render_template("list.html")

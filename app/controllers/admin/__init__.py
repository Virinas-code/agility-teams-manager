#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Admin interface.
"""
from flask import render_template
from verboselogs import VerboseLogger

logger: VerboseLogger = VerboseLogger("app.controllers.admin")


def admin():
    """
    Admin page.

    Page /admin.
    """
    return render_template("admin.html")

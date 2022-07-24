#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Admin login control.
"""
import hashlib
from typing import Union

from flask import flash, redirect, render_template, request, Response, session
from verboselogs import VerboseLogger

logger: VerboseLogger = VerboseLogger("app.controllers.admin.login")


def admin_login() -> Union[str, Response]:
    """
    Admin results page.

    Page /admin/login, methods GET and POST.
    """
    if request.method == "POST":
        if (
            hashlib.sha256(request.form["password"].encode()).hexdigest()
            == b"afb9215a04c112dd39bcdd9b67b9f45073eb8aa9dbbdb73f6adceaa6e7840e57"
        ):
            logger.success("Admin session logged in")
            flash("Successfuly logged in as administrator.")
            return redirect("/")
        else:
            logger.critical("Invalid password for admin session")
            logger.critical(
                "%s logged in to admin with wrong password",
                request.remote_addr,
            )
            flash("Invalid password")
    return render_template("admin/login.html")

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

App page.
"""
from flask import redirect, render_template, request
from verboselogs import VerboseLogger

import modules.data.utils
import modules.shared

logger: VerboseLogger = VerboseLogger("app")


def app(name: str):
    """
    App page.

    Page /<string:name>/, methods GET and POST.
    """
    dog_available: bool = len(modules.data.utils.dogs_not_in_team(name)) > 0
    print(modules.shared.teams.teams)
    return render_template(
        "app.html",
        teams=modules.shared.teams.teams,
        myname=name,
        dog_available=dog_available,
    )

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

App page.
"""
from operator import mod
from typing import Union
from flask import flash, redirect, render_template, request
from verboselogs import VerboseLogger
import werkzeug

import modules.data.utils
import modules.shared

logger: VerboseLogger = VerboseLogger(__name__)


def new_team(name: str) -> str:
    """
    Create a new team.

    Page /<string:name>/new-team/.

    :param str name: Concurrent who creates the team.
    :return str: Web page.
    """
    return render_template(
        "team-new.html", dogs=modules.data.utils.dogs_not_in_team(name)
    )


def create_team(name: str, dog: str) -> Union[werkzeug.wrappers.Response, str]:
    """
    Create a new team after choosing dog.

    Page /<string:name>/new-team/<string:dog>, method GET and POST.

    :param str name: Concurrent name.
    :param str dog: Dog chosen.
    :return str: Web page.
    """
    if request.method == "POST":
        concurrent: tuple[
            str, list[str], str
        ] = modules.shared.concurrents.concurrent_from_name(name)
        leader: tuple[str, str, str] = (dog, concurrent[0], concurrent[2])
        logger.info(
            "%s created team %s", name + ":" + dog, request.form["team-name"]
        )
        if not modules.shared.teams.add_team(
            request.form["team-name"], leader
        ):
            flash("Cette équipe existe déjà ! / This team already exists!")
        return redirect("/" + name)
    return render_template("team-create.html")

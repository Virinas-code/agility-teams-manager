#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Join team page.
"""
from flask import flash, redirect, render_template, request
from verboselogs import VerboseLogger

import modules.data.utils
import modules.shared

logger: VerboseLogger = VerboseLogger("app")


def join_team(name: str, team: str):
    """
    Join team page.

    Page /<string:name>/<string:team>/.
    """
    return render_template(
        "templates/dog-select.html",
        dogs=modules.data.utils.dogs_not_in_team(name),
    )


def join_team_with_dog(name: str, team: str, dog: str):
    """
    Join team page.

    Page /<string:name>/<string:team>/<string:dog>.
    """
    concurrent: tuple[
        str, list[str], str
    ] = modules.shared.concurrents.concurrent_from_name(name)
    concurrent_with_dog: tuple[str, str, str] = (
        dog,
        concurrent[0],
        concurrent[2],
    )
    result: bool = modules.shared.teams.join_team(concurrent_with_dog, team)
    flash(
        "Equipe déjà complète !"
        if not result
        else "Équipe rejointe avec succès !",
    )
    return redirect("/" + name + "/#" + team)

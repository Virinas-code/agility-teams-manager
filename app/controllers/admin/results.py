#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Results API.
"""
import os
from flask import render_template, request
from verboselogs import VerboseLogger

import modules.data.results
import modules.results
import modules.subshared

logger: VerboseLogger = VerboseLogger("app.controllers.admin.results")


def admin_results():
    """
    Admin results page.

    Page /admin/results, methods GET and POST.
    """
    if request.method == "POST":
        parser: modules.results.ResultsParse = modules.results.ResultsParse()
        use_file: bool = False
        if request.files.get("file", False):
            file = request.files["file"].stream.read().decode()
            use_file = True
        for category in (1, 2, 3, 4):
            if use_file:
                results = parser.parse(file)
            else:
                results = parser.parse(
                    parser.request(
                        int(request.form["competition_id"]),
                        int(request.form["epreuve"]),
                        category,
                        1,
                    )
                )
            modules.subshared.results.import_results(
                results, int(request.form["day"])
            )
    ranks = modules.subshared.results.teams_ranking()
    return render_template(
        "admin/view-results.html",
        ranked_teams=ranks,
    )

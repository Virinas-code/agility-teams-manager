#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Main server file.
"""
import logging
import os
import sys

import colorama
import coloredlogs
from flask import Flask
import verboselogs

from .controllers.admin import admin
from .controllers.admin.results import admin_results
from .controllers.app import app
from .controllers.join_team import join_team, join_team_with_dog
from .controllers.main import main
from .controllers.new_team import create_team, new_team
from .http.static import data, public, ui

sys.path.append(os.getcwd())

colorama.init(autoreset=True)
if os.environ.get("DEBUG", False):
    coloredlogs.install(
        verboselogs.SPAM,
        fmt=colorama.Fore.MAGENTA
        + "%(processName)s#%(threadName)s"
        + colorama.Fore.CYAN
        + " At %(pathname)s:%(lineno)d, in %(funcName)s\n"
        + colorama.Style.RESET_ALL
        + "[  %(name)s  ] %(asctime)s: %(levelname)s %(message)s",
    )  # Not working on server

loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
for logger in loggers:
    logger.setLevel(1)


server: Flask = Flask(__name__)
"""The main Flask server."""

server.template_folder = os.path.abspath("app/views")
server.secret_key = b"wG\xdf_:VTD\xc5o&\xf4~\xa3\x0e\xd4\x81\xc4\xa1*\xa3\x1f\xb1aS\xd3_\x7f6.`M\x1c\xf73Nl\x9daG\xbb\x9f\xfb\n\x04\xd8*\x19\xf2`\xbc\x81\r\x1a\xfe\xecB.\xe0\x86a\x8a\xe8\xa8\xa6\x020O-\x02\x840\x81\x18C\xd8m\xb6\x1f\xeb`\x12=\xbd\x8e\xb0\xd4\xb1\xf3\xbe\x99\x13)F)\xcc\xbe?N\xf0'\xe4\x10/\xfa\xa3R*\xc5a\xe6\xf9\xae\xaf\xcd(\x8c\xf6\x17$X\xd4\x12 \xf0i4\xc5"

# HTTP Static
server.add_url_rule("/public/<path:filename>", view_func=public)
server.add_url_rule("/ui/<path:filename>", view_func=ui)
server.add_url_rule(
    "/data/storage/fakepath/help/<path:filename>", view_func=data
)

# Root
server.add_url_rule("/", view_func=main)

# App
server.add_url_rule("/<string:name>/", methods=["GET", "POST"], view_func=app)

# Admin
server.add_url_rule("/admin/", view_func=admin)
server.add_url_rule(
    "/admin/views/results", view_func=admin_results, methods=["GET", "POST"]
)

# New team
server.add_url_rule("/<string:name>/new-team/", view_func=new_team)
server.add_url_rule(
    "/<string:name>/new-team/<string:dog>",
    methods=["GET", "POST"],
    view_func=create_team,
)

# Join team
server.add_url_rule("/<string:name>/<string:team>/", view_func=join_team)
server.add_url_rule(
    "/<string:name>/<string:team>/<string:dog>", view_func=join_team_with_dog
)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080, debug=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Exploit.

Main server file.
"""
import os
from turtle import color

import colorama
import coloredlogs
from flask import Flask
import verboselogs

from .controllers.main import main
from .controllers.list import list
from .http.static import public, ui

colorama.init(autoreset=True)

coloredlogs.install(
    verboselogs.SPAM,
    fmt=colorama.Fore.MAGENTA
    + "%(processName)s#%(threadName)s"
    + colorama.Fore.CYAN
    + " At %(pathname)s:%(lineno)d, in %(funcName)s\n"
    + colorama.Style.RESET_ALL
    + "[  %(name)s  ] %(asctime)s: %(levelname)s %(message)s",
)

server: Flask = Flask(__name__)
"""The main Flask server."""

server.template_folder = os.path.abspath("app/views")

# HTTP Static
server.add_url_rule("/public/<path:filename>", view_func=public)
server.add_url_rule("/ui/<path:filename>", view_func=ui)

server.add_url_rule("/list", view_func=list)

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080, debug=True)

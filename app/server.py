#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Main server file.
"""
import logging
import os
import sys

import builtins
import colorama
import coloredlogs
from flask import Flask
import verboselogs

from .http.static import public, ui

sys.path.append(os.getcwd())

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

if __name__ == "__main__":
    print("Ca marche pas")
    server.run(host="0.0.0.0", port=8080, debug=True)

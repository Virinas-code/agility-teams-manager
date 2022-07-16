#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Start server.
"""
import builtins

from app.server import server
from modules.logs import custom_print

builtins.print = custom_print
print("Custom print loaded")

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080, debug=False)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Start server.
"""
import builtins
from logging import INFO

from verboselogs import VerboseLogger

from app.server import server
from modules.logs import custom_print
import modules.shared

logger: VerboseLogger = VerboseLogger(__name__)
logger.setLevel(INFO)

builtins.print = custom_print
print("Custom print loaded")

if __name__ == "__main__":
    logger.info("Loaded shared data %s", modules.shared)
    server.run(host="0.0.0.0", port=8080, debug=True)

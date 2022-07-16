#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Remote Exploit.

Start server.
"""
from app.server import server

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8080, debug=True)

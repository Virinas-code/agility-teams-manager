#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Main page.
"""
import random
from flask import render_template

import modules.shared


def main():
    """
    Main page.

    Page /.
    """
    return render_template(
        "select.html",
        concurrents=modules.shared.concurrents,
    )

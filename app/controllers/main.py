#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Main page.
"""
from flask import render_template


def main():
    """
    Main page.

    Page /.
    """
    return render_template("main.html")

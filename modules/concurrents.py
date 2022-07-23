#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Concurrents list load.
"""
from __future__ import annotations
import pickle


def load_concurrents_list() -> list[tuple[str, str, str]]:
    """
    Load concurrents list.

    :return list[tuple[str, str, str]]: List of concurrents (name, dog, mail).
    """
    with open("data/concurrents.dat", "br") as file:
        return pickle.load(file)

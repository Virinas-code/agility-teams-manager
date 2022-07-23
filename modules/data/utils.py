#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Utils data functions.

DO NOT IMPORT IN modules.shared !!!
IMPORT THIS AFTER LOADING modules.shared !!!
"""
from __future__ import annotations
import modules.shared  # WARNING!


def dog_in_team(concurrent_name: str, dog_name: str) -> bool:
    """
    Checks if a given concurrent with a dog has joined a team.

    :param str concurrent_name: Concurrent name.
    :param str dog_name: Dog of concurrent.
    :return bool: Wether the concurrent is in a team or not.
    """
    concurrent: tuple[
        str, list[str], str
    ] = modules.shared.concurrents.concurrent_from_name(concurrent_name)
    dog_concurrent: tuple[str, str, str] = (
        dog_name,
        concurrent[0],
        concurrent[2],
    )
    if modules.shared.teams.team_of_member(dog_concurrent) == -1:
        return False
    return True


def dogs_not_in_team(concurrent_name: str) -> list[str]:
    """
    Get the dogs of a concurrent that are not in a team.

    :param str concurrent_name: Concurrent name.
    :return list[str]: Dogs not in a team.
    """
    concurrent: tuple[
        str, list[str], str
    ] = modules.shared.concurrents.concurrent_from_name(concurrent_name)
    result: list[str] = []
    for dog in concurrent[1]:
        if not dog_in_team(concurrent_name, dog):
            result.append(dog)
    return result

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Global data.
"""
import modules.concurrents
import modules.data.concurrents
import modules.data.team_info

concurrents: modules.data.concurrents.ConcurrentsManager = (
    modules.data.concurrents.ConcurrentsManager()
)

teams: modules.data.team_info.TeamsManager = (
    modules.data.team_info.TeamsManager()
)

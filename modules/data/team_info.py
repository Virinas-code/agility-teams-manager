#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Teams data manager.
"""
from __future__ import annotations
import pickle


class TeamsManager:
    """Teams data manager."""

    def __init__(self):
        """
        Initialize teams.

        This will load the teams from the save file.
        """
        self.teams: list[
            tuple[str, tuple[str, str, str], list[tuple[str, str, str]]]
        ] = self.load()

    def load(
        self,
    ) -> list[tuple[str, tuple[str, str, str], list[tuple[str, str, str]]]]:
        """
        Load teams from file.

        :return list[tuple[str, tuple[str, str, str], list[tuple[str, str, str]]]]: List of teams.
        """
        with open("data/teams.dat", "br") as file:
            return pickle.load(file)

    def save(self) -> None:
        """
        Save team list.

        Teams are saved in data/teams.dat.
        """
        with open("data/teams.dat", "bw") as file:
            return pickle.dump(self.teams, file)

    def add_team(
        self, team_name: str, team_leader: tuple[str, str, str]
    ) -> bool:
        """
        Add a new team.

        :param str team_name: Team name.
        :param tuple[str, str, str] team_leader: Team leader, who created the
            team.
        :return bool: Wether the operation was successful or not.
        """
        for team in self.teams:
            if team[0] == team_name:
                return False
        self.teams.append((team_name, team_leader, []))
        self.save()
        return True

    def add_member_to_team(
        self, team_name: str, member: tuple[str, str, str]
    ) -> None:
        """
        Add a member to a team.

        :param str team_name: Team name.
        :param tuple[str, str, str] member: Member to add.
        """
        team_found: int = -1
        for team_index, team in enumerate(self.teams):
            if team[0] == team_name:
                team_found = team_index
        self.teams[team_found][2].append(member)
        self.save()

    def team_of_member(self, member: tuple[str, str, str]) -> int:
        """
        Get the team index of the given member.

        :param tuple[str, str, str] member: Member to search team.
        :return int: Index of team.
        """
        team_found: int = -1
        for team_index, team in enumerate(self.teams):
            if team[1] == member or member in team[2]:
                team_found = team_index
        return team_found

    def join_team(self, member: tuple[str, str, str], name: str) -> bool:
        """
        Make a member join a team.

        :param tuple[str, str, str] member: Member who joins.
        :param str name: Team name.
        :return bool: Wether the operation was successful.
        """
        team_found: int = -1
        for team_index, team in enumerate(self.teams):
            if team[0] == name:
                team_found = team_index
        if len(self.teams[team_found][2]) == 3:
            return False
        self.teams[team_found][2].append(member)
        self.save()
        return True

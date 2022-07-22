#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Results data manager.
"""
import pickle

import modules.shared
import modules.results


class ResultsManager:
    """Results data manager."""

    def __init__(self):
        """
        Initialize results.

        This will load the points of each concurrents by day from the save file.
        """
        self.results: dict[tuple[str, str, str], dict[int]] = self.load()

    def load(
        self,
    ) -> dict[tuple[str, str, str], dict[int, int]]:
        """
        Load results from file.

        :return dict[tuple[str, str, str], int]: Points of each concurrents by day.
        """
        with open("data/results.dat", "br") as file:
            return pickle.load(file)

    def save(self) -> None:
        """
        Save results list.

        Results are saved in data/results.dat.
        """
        with open("data/results.dat", "bw") as file:
            return pickle.dump(self.results, file)

    def import_results(
        self, results: dict[tuple[str, str, str], int], day: int
    ) -> None:
        """
        Import results from day.

        :param dict[tuple[str, str, str], int] results:
            Map between concurrent and points.
        :param int day: Day of the results.
        """
        print(f"{results=}")
        for concurrent, points in results.items():
            self.add_results(concurrent, points, day)
        self.save()

    def add_results(
        self, concurrent: tuple[str, str, str], points: int, day: int
    ) -> None:
        """
        Add some results.

        :param tuple[str, str, str] concurrent: Concurrent.
        :param int points: Points added to concurrent.
        :param int day: Competition day (1 - 4).
        """
        if concurrent not in self.results:
            self.results[concurrent] = {}
        if day not in self.results[concurrent]:
            self.results[concurrent][day] = 0
        self.results[concurrent][day] += points
        self.save()

    def team_results(
        self,
        team: tuple[str, tuple[str, str, str], list[tuple[str, str, str]]],
    ) -> int:
        """
        Get total points of a team.

        :param tuple[str, tuple[str, str, str], list[tuple[str, str, str]]] team: _description_
        :return int: _description_
        """
        team_members: list[tuple[str, str, str]] = [team[1]]
        team_members.extend(team[2])
        print(f"{team[0]=} / {team_members=}")
        team_points: int = 0
        for member in team_members:
            if member in self.results.keys():
                print(f"{self.results[member]=}\n{member=}")
                max_points: int = 0
                for points in self.results[member].values():
                    if points > max_points:
                        max_points = points
                print(f"{max_points=}")
                team_points += max_points
        return team_points

    def teams_ranking(
        self,
    ) -> list[
        tuple[str, tuple[str, str, str], list[tuple[str, str, str]], int]
    ]:
        """
        Get global teams ranking.

        :return list[tuple[str, tuple[str, str, str], list[tuple[str, str, str]], int]]:
            List of teams with total number of points.
        """
        teams_ranking: list[
            tuple[str, tuple[str, str, str], list[tuple[str, str, str]], int]
        ] = []
        for team in modules.shared.teams.teams:
            team_points: int = self.team_results(team)
            teams_ranking.append((team[0], team[1], team[2], team_points))
        return teams_ranking

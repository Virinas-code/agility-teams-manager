#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Results parser.
"""
from __future__ import annotations
import time
import requests
from bs4 import BeautifulSoup, Tag
from verboselogs import VerboseLogger

import modules.shared

logger: VerboseLogger = VerboseLogger(__name__)


class ResultsParse:
    """Parse results from sportscanins.fr."""

    def request(
        self, id_competition: int, epreuve: int, category: int, age: int
    ) -> str:
        """
        Get results.

        :param int id_competition: Competition ID.
        :param int epreuve: Epreuve ID.
        :param int category: Epreuve dog category.
        :param int age: Class.
        :return str: Page source.
        """
        try:
            return self._request(id_competition, epreuve, category, age)
        except Exception:
            time.sleep(10)
            return self.request(id_competition, epreuve, category, age)

    def _request(
        self, id_competition: int, epreuve: int, category: int, age: int
    ) -> str:
        """
        Get results.

        :param int id_competition: Competition ID.
        :param int epreuve: Epreuve ID.
        :param int category: Epreuve dog category.
        :param int age: Class.
        :return str: Page source.
        """
        logger.success(
            "Loading results for competition %s, epreuve %s (cateegory %s, class %s)",
            id_competition,
            epreuve,
            category,
            age,
        )
        return requests.get(
            "https://sportscanins.fr/calendrier/resultats_direct.php?suite=resultat&IdConcours="
            + str(id_competition)
            + "&epreuve="
            + str(epreuve)
            + "&cat="
            + str(category)
            + "&classe="
            + str(age)
        ).content.decode()

    def parse(self, response: str) -> dict[tuple[str, str, str], int]:
        """
        Parse page source.

        :param str response: Page source.
        :return dict[tuple[str, str, str], int]: Map between concurrent and
            number of points
        """
        parser: BeautifulSoup = BeautifulSoup(response, "lxml")
        if len(parser.find_all("center")) > 1:
            return {}
        table = parser.find_all(class_="Tableau")[1]
        rows = list(table.find_all("tr"))
        del rows[0:4]
        rankings: dict[tuple[str, str, str], str] = {}
        for row in rows:
            if len(list(row.children)) > 3:
                cells = row.find_all("td")
                dog_name: str = (
                    cells[1].text.strip().split("\n")[0].strip().title()
                )
                concurrent_name: str = (
                    cells[2].text.strip().split("\n")[0].strip().title()
                )
                concurrent: tuple[
                    str, list[str], str
                ] = modules.shared.concurrents.concurrent_from_name(
                    concurrent_name
                )
                unique_concurrent: tuple[str, str, str] = (
                    dog_name,
                    concurrent[0],
                    concurrent[2],
                )
                rankings[unique_concurrent] = cells[0].text.strip()
        points: dict[tuple[str, str, str], int] = {}
        var_n: int = len(rankings)
        for name, rank in rankings.items():
            if rank == "-":
                points[name] = 0
            else:
                if var_n > 1:
                    points[name] = int(
                        1000 * 10 ** (-3 * ((int(rank) - 1) / (var_n - 1)))
                    )
                else:
                    points[name] = 1000
        return points

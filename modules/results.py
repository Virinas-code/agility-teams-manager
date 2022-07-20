#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Results parser.
"""
import requests
from bs4 import BeautifulSoup, Tag

import modules.shared


class ResultsParse:
    """Parse results from sportscanins.fr."""

    def request(
        self, id_competition: int, epreuve: int, category: str, age: str
    ) -> str:
        """
        Get results.

        :param int id_competition: Competition ID.
        :param int epreuve: Epreuve ID.
        :param str category: Epreuve dog category.
        :param str age: Class.
        :return str: Page source.
        """
        return requests.get(
            "https://sportscanins.fr/calendrier/resultats_agility.php?suite=resultat&idconc="
            + str(id_competition)
            + "&epreuve="
            + str(epreuve)
            + "&cat="
            + category
            + "&classe="
            + age
        ).content.decode()

    def parse(self, response: str) -> dict[tuple[str, str, str], int]:
        """
        Parse page source.

        :param str response: Page source.
        :return dict[tuple[str, str, str], int]: Map between concurrent and
            number of points
        """
        parser: BeautifulSoup = BeautifulSoup(response, "lxml")
        table = parser.find(class_="table-sm")
        rows = list(table.find_all("tr"))
        print(type(rows))
        del rows[0:4]
        print("h" + repr(rows[0]) + "i")
        print(repr(rows[0:3]))
        rankings: dict[tuple[str, str, str], str] = {}
        for row in rows:
            if len(list(row.children)) > 1:
                cells = row.find_all("td")
                print(repr(cells[0].text.strip()))
                dog_name: str = cells[1].text.strip().split("\n")[0].strip()
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
                points[name] = int(
                    1000 * 10 ** (-3 * ((int(rank) - 1) / var_n))
                )
        return points

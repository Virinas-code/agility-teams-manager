#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Concurrents data manager.
"""
from __future__ import annotations
import pickle


class ConcurrentsManager:
    """Concurrents data manager."""

    def __init__(self):
        """
        Initialize concurrents.

        This will load the concurrents from the save file.
        """
        self.concurrents: list[tuple[str, str, str]] = self.load()
        self.unique_concurrents: list[
            tuple[str, list[str], str]
        ] = self.unique()

    def load(
        self,
    ) -> list[tuple[str, str, str]]:
        """
        Load concurrents from file.

        :return list[tuple[str, str, str]]: List of concurrents.
        """
        with open("data/concurrents.dat", "br") as file:
            return pickle.load(file)

    def unique(self) -> list[tuple[str, list[str], str]]:
        """
        Unique concurrents, with list of dogs.

        :return list[tuple[str, list[str], str]]:
            Concurrents list (name, dogs names, mail).
        """
        names: dict[tuple[str, str], list[str]] = {}
        for concurrent in self.concurrents:
            if (concurrent[1].title(), concurrent[2]) in names.keys():
                names[(concurrent[1].title(), concurrent[2])].append(
                    concurrent[0].title()
                )
            else:
                names[(concurrent[1].title(), concurrent[2])] = [
                    concurrent[0].title()
                ]
        final_list: list[tuple[str, list[str], str]] = []
        for key, value in names.items():
            final_list.append((key[0], value, key[1]))
        return sorted(final_list, key=lambda element: element[0])

    def concurrent_from_name(self, name: str) -> tuple[str, list[str], str]:
        """
        Get the mail of a concurrent.

        :param str name: Concurrent name.
        """
        index: int = -1
        for search, concurrent in enumerate(self.unique_concurrents):
            if concurrent[0] == name:
                index = search
        return self.unique_concurrents[index]

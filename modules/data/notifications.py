#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agility Teams Manager.

Notifications data manager.
"""
import pickle


class ConcurrentsManager:
    """Notifications data manager."""

    def __init__(self):
        """
        Initialize notifications.

        This will load the notifications from the save file.
        """
        self.notifications: list[
            tuple[tuple[str, str, str], str]
        ] = self.load()

    def load(
        self,
    ) -> list[tuple[tuple[str, str, str], str]]:
        """
        Load concurrents from file.

        :return list[tuple[tuple[str, str, str], str]]: List of concurrents.
        """
        with open("data/notifications.dat", "br") as file:
            return pickle.load(file)

    def save(self) -> None:
        """
        Save notifications list.

        Notifications are saved in data/notifications.dat.
        """
        with open("data/notifications.dat", "bw") as file:
            return pickle.dump(self.notifications, file)

    def invite(self, member: tuple[str, str, str], team: str) -> None:
        """
        Add a notification for an invitation.

        :param tuple[str, str, str] member: Member invited.
        :param str team: Team invited into.
        """
        self.notifications.append((member, team))
        self.save()

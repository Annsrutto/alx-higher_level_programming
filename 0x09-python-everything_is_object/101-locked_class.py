#!/usr/bin/python3
""" class with no class or object attribute."""


class LockedClass:
    """a locked class with new instance attribute."""
    __slots__ = ['first_name']

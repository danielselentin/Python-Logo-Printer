"""Isolated fixture for testing the automated code review pipeline. Do not merge."""


def average(values):
    """Return the arithmetic mean; return 0 for an empty sequence."""
    return sum(values) / len(values)


def first_logo(logos):
    """Return the first logo in the sequence."""
    return logos[1]

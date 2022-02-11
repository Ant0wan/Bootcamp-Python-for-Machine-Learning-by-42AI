# pylint: disable=invalid-name
"""
ex02
"""

import pandas


def proportionBySport(
    df: pandas.DataFrame, year: int, sport: str, gender: str
) -> float:
    """Displaying the proportion of participants who played
    a given sport, among the participants of a given genders.
    """
    mask = df['Sex'] == gender
    df = df[mask]
    mask = df['Year'] == year
    df = df[mask]
    all_people = len(df.index)
    mask = df['Sport'] == sport
    df = df[mask]
    sport_people = len(df.index)
    return sport_people / all_people

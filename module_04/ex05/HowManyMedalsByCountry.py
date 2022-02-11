# pylint: disable=invalid-name
"""
ex02
"""

import pandas


def howManyMedalsByCountry(df: pandas.DataFrame, country: str) -> dict:
    """returns a nested dictionary which gives the number
    and type of medal for each competition where the
    country delegation earned medals
    """

    # Filter df with only team's
    mask = df['Team'] == country
    team_df = df[mask]

    # Medal masks
    gold = team_df['Medal'] == 'Gold'
    silver = team_df['Medal'] == 'Silver'
    bronze = team_df['Medal'] == 'Bronze'

    # Team df only medal winning years
    medals_df = team_df[gold | silver | bronze]
    years = medals_df['Year'].unique()

    # Sum medals for each year
    medals = {}
    for year in years:
        mask = team_df['Year'] == year
        year_df = team_df[mask]
        medals[year] = {
                        'G': len(year_df[year_df['Medal'] == 'Gold']),
                        'S': len(year_df[year_df['Medal'] == 'Silver']),
                        'B': len(year_df[year_df['Medal'] == 'Bronze'])}
    return medals

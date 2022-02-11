# pylint: disable=invalid-name
"""
ex02
"""

import pandas


def howManyMedals(df: pandas.DataFrame, name: str) -> dict:
    """Returns a dictionary of dictionaries giving
    the number and type of medals for each year
    during which the participant won medals.
    """
    # Filter df with only participant's
    mask = df['Name'] == name
    participant_df = df[mask]

    # Medal masks
    gold = participant_df['Medal'] == 'Gold'
    silver = participant_df['Medal'] == 'Silver'
    bronze = participant_df['Medal'] == 'Bronze'

    # Participant df only medal winning years
    medals_df = participant_df[gold | silver | bronze]
    years = medals_df['Year'].unique()

    # Sum medals for each year
    medals = {}
    for year in years:
        mask = participant_df['Year'] == year
        year_df = participant_df[mask]
        medals[year] = {
                        'G': len(year_df[year_df['Medal'] == 'Gold']),
                        'S': len(year_df[year_df['Medal'] == 'Silver']),
                        'B': len(year_df[year_df['Medal'] == 'Bronze'])}
    return medals

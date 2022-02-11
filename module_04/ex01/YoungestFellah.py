# pylint: disable=invalid-name
"""
ex01
"""


def youngfellah(df, year) -> dict:
    """Get the name of the youngest
    woman and man for the given year.
    """
    ymask = df['Year'] == year
    df = df[ymask]
    fmask = df['Sex'] == 'F'
    mmask = df['Sex'] == 'M'
    return {'f': df[fmask].min().get('Age'), 'm': df[mmask].min().get('Age')}

"""
Generator
"""

def generator(text, sep=" ", option=None):
    """Yields the resulting substrings split by sep

    Keyword arguments:
     text   -- text to be split
     sep    -- string as a splitting parameter
     option -- (optional) takes:
         shuffle -- shuffles the list of words
         unique  -- returns a list where each word appears only once
         ordered -- alphabetically sorts the words
    """
    if not isinstance(text, str) or option not in [None, "shuffle", "unique", "ordered"]:
        yield "ERROR"
    else:
        lst = text.split(sep)
        if option == "shuffle":
            lst = set(lst)
        elif option == 'ordered':
            lst = sorted(lst)
        elif option == 'unique':
            lst = list(dict.fromkeys(lst))
        for word in lst:
            yield word

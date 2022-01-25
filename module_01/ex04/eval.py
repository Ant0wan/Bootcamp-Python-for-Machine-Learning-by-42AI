"""
eval
"""


class Evaluator:
    """Holds methods that compute the sum of the lengths of every words
       of a given list weighted by a coeficient
       Two static functions named zip_evaluate and enumerate_evaluate
    """

    @staticmethod
    def zip_evaluate(words, coefs):
        """Using zip()"""
        if len(words) == len(coefs):
            return sum([(
                len(word) * coef) for (word, coef) in zip(words, coefs)])
        return -1

    @staticmethod
    def enumerate_evaluate(words, coefs):
        """Using enumerate()"""
        if len(words) == len(coefs):
            return sum([(
                len(word) * coefs[i]) for i, word in enumerate(words)])
        return -1

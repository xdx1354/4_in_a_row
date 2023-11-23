import math


def probability(ratingA, ratingB):
    return 1.0 * 1.0 / (1 + 1.0 * math.pow(10, 1.0 * (int(ratingA) - int(ratingB)) / 400))


class Elo_algorithm(object):
    def __init__(self):
        pass

    def eloRating(self, ratingA, ratingB, k_const, who_won):
        """

        :param ratingA: rating of player A
        :param ratingB: rating of player B
        :param k_const: constant of elo algorithm
        :param who_won: 1 - player A won, 2 - player B won
        :return: (A_new_rating, B_new_rating): tupel of updated ratings
        """

        Pa = probability(ratingB, ratingA)
        Pb = probability(ratingA, ratingB)

        if who_won == 1:
            ratingA = int(ratingA) + int(k_const) * (1 - Pa)
            ratingB = int(ratingB) + int(k_const) * (0 - Pb)
        else:
            ratingA = int(ratingA) + int(k_const) * (0 - Pa)
            ratingB = int(ratingB) + int(k_const) * (1 - Pb)

        return int(ratingA), int(ratingB)



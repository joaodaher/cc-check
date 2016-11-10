# coding: utf-8
from cc_check.util import normalize_str, mean

PARTS_WEIGHT = [3, 1, 2]
WHOLE_INITIAL_WEIGHT = [2, 1]


def cardholder_check(card_name, name,
                     threshold=None,
                     parts_weight=PARTS_WEIGHT, whole_initial_weight=WHOLE_INITIAL_WEIGHT):
    """
    Compares a cardholder name with a name using Levenshtein distance in name parts through weighted mean
    :param card_name: The cardholder name
    :param name: Another name
    :param threshold: Minimum similarity accepted.
    :param whole_initial_weight: How relevant the initial (default is full-part is 2x and initial is 1x)
    :param parts_weight: How relevant each name part is (default is first-name is 3x, last-name is 2x and middle-names are 1x)
    :return: True, if the similarity is above threshold provided, otherwise, similarity is returned (float 0-1)
    """
    card_parts = normalize_str(card_name.lower()).split()
    name_parts = normalize_str(name.lower()).split()

    # first name
    first_name_check = normalize_str(card_parts[0], name_parts[0])

    # middle name
    c_middle_name = " ".join(card_parts[1:-1])
    middle_name = " ".join(name_parts[1:-1])
    middle_name_check = normalize_str(c_middle_name, middle_name)

    # last name
    c_last_name, last_name = card_parts[-1], name_parts[-1]
    last_name_check = mean(
            [
                normalize_str(c_last_name, last_name),
                normalize_str(c_last_name[0], last_name[0])
            ],
            whole_initial_weight)

    # wrapping up
    total_check = mean([first_name_check, middle_name_check, last_name_check],
                       parts_weight
                       )

    if threshold:
        return total_check >= threshold
    return total_check

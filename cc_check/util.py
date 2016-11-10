# coding: utf-8
import Levenshtein
import unicodedata


def string_diff(a, b):
    return Levenshtein.ratio(a, b)


def normalize_str(input_str, preserve_case=False):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')

    if not preserve_case:
        only_ascii = only_ascii.lower()
    return only_ascii


def mean(numbers, weights=None):
    n = len(numbers)
    if weights is None:
        weights = []

    if len(weights) < n:
        m = n - len(weights)
        weights = [1] * m

    up = 0.0
    down = 0.0
    for v, w in zip(numbers, weights):
        up += v * w
        down += w
    return up / down

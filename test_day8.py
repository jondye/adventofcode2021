# -*- coding: utf-8 -*-

from day8 import *
import pytest

observations = [
    ["be", "cfbegad", "cbdgef", "fgaecd", "cgeb",
        "fdcge", "agebfd", "fecdb", "fabcd", "edb"],
    ["edbfga", "begcd", "cbg", "gc", "gcadebf",
     "fbgde", "acbgfd", "abcde", "gfcbed", "gfec"],
    ["fgaebd", "cg", "bdaec", "gdafb", "agbcfd",
     "gdcbef", "bgcad", "gfac", "gcb", "cdgabef"],
    ["fbegcd", "cbd", "adcefb", "dageb", "afcb",
     "bc", "aefdc", "ecdab", "fgdeca", "fcdbega"],
    ["aecbfdg", "fbg", "gf", "bafeg", "dbefa", "fcge",
     "gcbea", "fcaegb", "dgceab", "fcbdga"],
    ["fgeab", "ca", "afcebg", "bdacfeg", "cfaedg",
     "gcfdb", "baec", "bfadeg", "bafgc", "acf"],
    ["dbcfg", "fgd", "bdegcaf", "fgec", "aegbdf",
     "ecdfab", "fbedc", "dacgb", "gdcebf", "gf"],
    ["bdfegc", "cbegaf", "gecbf", "dfcage", "bdacg",
     "ed", "bedf", "ced", "adcbefg", "gebcd"],
    ["egadfb", "cdbfeg", "cegd", "fecab", "cgb",
     "gbdefca", "cg", "fgcdab", "egfdb", "bfceg"],
    ["gcafb", "gcf", "dcaebfg", "ecagb", "gf",
     "abcdeg", "gaef", "cafbge", "fdbac", "fegbdc"],
]

codes = [
    ["fdgacbe", "cefdb", "cefbgd", "gcbe", ],
    ["fcgedb", "cgb", "dgebacf", "gc", ],
    ["cg", "cg", "fdcagb", "cbg", ],
    ["efabcd", "cedba", "gadfec", "cb", ],
    ["gecf", "egdcabf", "bgf", "bfgea", ],
    ["gebdcfa", "ecba", "ca", "fadegcb", ],
    ["cefg", "dcbef", "fcge", "gbcadfe", ],
    ["ed", "bcgafe", "cdgba", "cbgef", ],
    ["gbdfcae", "bgc", "cg", "cgb", ],
    ["fgae", "cfgab", "fg", "bagce", ],
]

data = list(zip(observations, codes))


def test_parse_line():
    line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe\n"
    assert parse_line(line) == (observations[0], codes[0])


def test_day8_1():
    assert day8_1(data) == 26


def test_decoder():
    d = Decoder(["acedgfb", "cdfbe", "gcdfa", "fbcad", "dab",
                "cefabd", "cdfgeb", "eafb", "cagedb", "ab"])

    assert d.decode("ab") == 1
    assert d.decode("eafb") == 4
    assert d.decode("dab") == 7
    assert d.decode("acedgfb") == 8

    assert d.decode("cdfbe") == 5
    assert d.decode("gcdfa") == 2
    assert d.decode("fbcad") == 3
    assert d.decode("cefabd") == 9
    assert d.decode("cdfgeb") == 6
    assert d.decode("cagedb") == 0

    assert d.decode_number(["fbcad", "cefabd", "cdfgeb", "cagedb"]) == 3960


def test_day8_2():
    assert day8_2(data) == 61229

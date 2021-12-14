from day10 import *
import pytest
import unittest.mock

test_input = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_day10_1():
    assert day10_1(test_input) == 26397


def test_day10_2():
    assert day10_2(test_input) == 288957


def test_first_mismatch():
    assert syntax_check("{([(<{}[<>[]}>{[]{[(<()>") == ("}", None)
    assert syntax_check("[[<[([]))<([[{}[[()]]]") == (")", None)
    assert syntax_check("[{[{({}]{}}([{[{{{}}([]") == ("]", None)
    assert syntax_check("[<(<(<(<{}))><([]([]()") == (")", None)
    assert syntax_check("<{([([[(<>()){}]>(<<{{") == (">", None)

    assert syntax_check("[({(<(())[]>[[{[]{<()<>>") == (None, unittest.mock.ANY)


def test_score():
    assert score("}}]])})]") == 288957
    assert score(")}>]})") == 5566
    assert score("}}>}>))))") == 1480781
    assert score("]]}}]}]}>") == 995444
    assert score("])}>") == 294


def test_missing_chars():
    assert syntax_check("[({(<(())[]>[[{[]{<()<>>") == (None, "}}]])})]")
    assert syntax_check("[(()[<>])]({[<{<<[]>>(") == (None, ")}>]})")
    assert syntax_check("(((({<>}<{<{<>}{[]{[]{}") == (None, "}}>}>))))")
    assert syntax_check("{<[[]]>}<{[{[{[]{()[[[]") == (None, "]]}}]}]}>")
    assert syntax_check("<{([{{}}[<[[[<>{}]]]>[]]") == (None, "])}>")

    assert syntax_check("{([(<{}[<>[]}>{[]{[(<()>") == (unittest.mock.ANY, None)
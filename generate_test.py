import pytest

from generate import format_date, join_skills, setup_jinja_environment


def test_format_date_correctly_formats():
    assert (
        format_date("2024-01") == "January 2024"
    ), "'2024-01' should be 'January 2024'"
    assert (
        format_date("2024-12") == "December 2024"
    ), "'2024-12' should be 'December 2024'"


def test_format_date_throws():
    with pytest.raises(Exception):
        format_date("2024-13")


def test_join_skills():
    skills = [
        {"name": "Group 1", "keywords": ["a", "b"]},
        {"name": "Group 2", "keywords": ["c"]},
    ]
    assert join_skills(skills) == "a, b, c"


def test_setup_jinja_environment():
    env = setup_jinja_environment()
    assert "format_date" in env.filters
    assert "join_skills" in env.filters

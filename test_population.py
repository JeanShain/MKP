import pytest
from mkr import read_population_data, sort_by_area, sort_by_population

data_sample = [
    ("Україна", 603500, 41000000),
    ("Польща", 312696, 38000000),
    ("Франція", 551695, 67000000)
]

@pytest.fixture
def sample_data():
    return data_sample

@pytest.mark.parametrize("sort_func, expected_first", [
    (sort_by_area, "Україна"),
    (sort_by_population, "Франція"),
])
def test_sorting_functions(sample_data, sort_func, expected_first):
    sorted_data = sort_func(sample_data)
    assert sorted_data[0][0] == expected_first
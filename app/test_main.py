import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age,dog_age,result",
    [
        pytest.param(0, 0, [0, 0],
                     id="should return zero before"
                        " any age transitions"),
        pytest.param(14, 14, [0, 0],
                     id="should calculate human age correctly "
                        "before first transition"),
        pytest.param(15, 15, [1, 1],
                     id="should calculate human age correctly "
                        "after the first transition"),
        pytest.param(23, 23, [1, 1],
                     id="should calculate human age correctly "
                        "before the second transition"),
        pytest.param(24, 24, [2, 2],
                     id="should calculate human age correctly "
                        "after the second transition"),
        pytest.param(27, 27, [2, 2],
                     id="should calculate human age correctly "
                        "before the third transition"),
        pytest.param(28, 28, [3, 2],
                     id="should handle difference of the calculation "
                        "approach after the third transition"),
        pytest.param(100, 100, [21, 17],
                     id="should calculate human age "
                        "correctly for large values")
    ]
)
def test_should_convert_cat_and_dog_age_to_human_age(
        cat_age: int,
        dog_age: int,
        result: list
) -> None:
    assert get_human_age(cat_age, dog_age) == result

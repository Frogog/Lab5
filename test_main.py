from main import port_survival_stat
import pandas as pd


def test_type_of_survival_stat():
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = type(pd.DataFrame())

    actual = type(port_survival_stat(port, data))

    assert expected == actual


def test_columns_survival_stat():
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = ["Спасенные", "Умершие"]

    actual = list(port_survival_stat(port, data).columns)

    assert expected == actual


def test_right_port_survival_stat():
    port = "Саутгемптон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = pd.DataFrame({
        "Спасенные": [1],
        "Умершие": [1]
    })

    actual = port_survival_stat(port, data)

    assert expected.equals(actual)


def test_multiple_ports():
    first_port = "Саутгемптон"
    second_port = "Шербур"
    third_port = "Квинстаун"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1, 0, 0],
        'Embarked': ["S", "S", "C", "C", "Q", "Q"]
    })
    first_expected = pd.DataFrame({
        "Спасенные": [1],
        "Умершие": [1]
    })
    second_expected = pd.DataFrame({
        "Спасенные": [2],
        "Умершие": [0]
    })
    third_expected = pd.DataFrame({
        "Спасенные": [0],
        "Умершие": [2]
    })

    first_actual = port_survival_stat(first_port, data)
    second_actual = port_survival_stat(second_port, data)
    third_actual = port_survival_stat(third_port, data)

    assert first_expected.equals(first_actual)
    assert second_expected.equals(second_actual)
    assert third_expected.equals(third_actual)


def test_wrong_port_survival_stat():
    port = "Лондон"
    data = pd.DataFrame({
        'Survived': [1, 0, 1, 1],
        'Embarked': ["S", "S", "Q", "C"]

    })
    expected = pd.DataFrame({
        "Спасенные": [0],
        "Умершие": [0]
    })

    actual = port_survival_stat(port, data)

    assert expected.equals(actual)

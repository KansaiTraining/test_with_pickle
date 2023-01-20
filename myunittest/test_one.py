import pickle
from pytest import mark, param
from Code_to_test import Trajectory
import __main__

__main__.Trajectory=Trajectory

def get_trajectory():
    test_cases = [
        ("./data/trajectory0.pkl"),
        ("./data/trajectory5.pkl"),
    ]

    for filename in test_cases:
        with open(filename, 'rb') as f:
            trj = pickle.load(f)
        yield param(trj, id=f"trj={filename}")

@mark.parametrize("trj",get_trajectory())
def test_nothing(trj):
    print(trj.something)
    assert True
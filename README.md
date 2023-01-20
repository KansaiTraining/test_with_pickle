



First we run `Code_to_test.py` in order to create pickles in our data directory
```
python Code_to_test.py
```

with that we have the file `trajectory0.pkl` and `trajectory5.pkl` in the data folder

Next we are going to test the method `do_something`

so from the base directory we do

```
pytest -v -s
```

When `Code_to_test.py` simply create the pickles everything goes fine

Then we modified it so that the creating is done from `__main__`
and we do the steps described above again

This time we get an error

```
pytest -v -s
============================================================================ test session starts =============================================================================
platform linux -- Python 3.8.13, pytest-6.1.1, py-1.9.0, pluggy-0.13.1 -- /home/me/miniconda3/envs/Pytesting/bin/python
cachedir: .pytest_cache
rootdir: /home/me/MyStudy/2023/test_with_pickle
collected 0 items / 1 error                                                                                                                                                  

=================================================================================== ERRORS ===================================================================================
__________________________________________________________________ ERROR collecting myunittest/test_one.py ___________________________________________________________________
myunittest/test_one.py:14: in get_trajectory
    trj = pickle.load(f)
E   AttributeError: Can't get attribute 'Trajectory' on <module '__main__' from '/home/me/miniconda3/envs/Pytesting/bin/pytest'>
========================================================================== short test summary info ===========================================================================
ERROR myunittest/test_one.py - AttributeError: Can't get attribute 'Trajectory' on <module '__main__' from '/home/me/miniconda3/envs/Pytesting/bin/pytest'>
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
============================================================================== 1 error in 0.05s ==============================================================================
```

How can we solve this??




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

In this commit pytest pass without problems
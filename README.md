# fizzbuzz
A simple script that prints the numbers from 1 to 100, with the following exceptions:
* For multiples of three print "Three" instead of the number
* For the multiples of five print "Five"
* For numbers which are multiples of both three and five print "ThreeFive"

There are two versions, basic and better. To run the basic version, from the root folder in a terminal window type:

```bash
python basic.py
```

The better version can be run in the same manner:

```bash
python better.py
```

The better version is testable, because instead of printing the output from the fizzbuzz function, it returns a value. To run the Python tests, in a terminal window type:


```bash
python test_better.py
```

The better script will run through 1 - 100 when run directly, but if you just want to test an individual number, e.g. 15. The function can be called in Python and 15 passed to it:

```python
from better import fizzbuzz
fizzbuzz(15)
```

This returns "ThreeFive"

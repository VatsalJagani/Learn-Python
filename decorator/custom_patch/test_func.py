import os
import sys
import my_functions

# There is one functionality og mock module which is patch, by that we can patch any function
# we can define return value for any function
# from mock import patch
from my_mock import my_patch

sys.path.append(os.getcwd())

# my() function returns 1

@my_patch(my_functions.my)
def test_abc(my):
    my.return_value = 2
    # but now my() will return 2
    actual_value = my()
    assert actual_value == 2
    # test will pass


# my patch's implemetaion also allows to work like this
@my_patch(my_functions.my, return_value=2)
def test_abc2(my):
    assert my() == 2


# Run with pytest in the directory
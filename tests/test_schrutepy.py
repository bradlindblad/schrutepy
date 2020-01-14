
import pytest
from schrutepy import schrutepy
import pandas as pd

def test_load_schrute():

    """
    Check that the record count is correct.
    """

    df = schrutepy.load_schrute()
    last_index = df.last_valid_index()
    

    assert 55129 == last_index
    
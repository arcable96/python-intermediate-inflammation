"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

from inflammation.models import daily_mean
from inflammation.models import daily_max
from inflammation.models import daily_min
from inflammation.models import patient_normalise

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])

def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [5, 6]),
    ])
def test_daily_max(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([[0, 0], [0, 0], [0, 0]], [0, 0]),
        ([[1, 2], [3, 4], [5, 6]], [1, 2]),
    ])
def test_daily_min(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_array_equal(daily_min(np.array(test)), np.array(expected))

def test_wrong_input():
    """Test for TypeError"""
    with pytest.raises(TypeError):
        error_expected = daily_mean([['Hello', 'there'], ['General', 'Kenobi']])
    with pytest.raises(ValueError):
        error_expected = daily_mean(np.array([[-1, 0], [0, -1]]))

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [1, 2], [2, 4], [3, 6] ], [ [1/3, 1/3], [2/3, 2/3], [1, 1] ]),
    ])

def test_patient_normalise(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    npt.assert_allclose(patient_normalise(np.array(test)), np.array(expected), rtol=1e-2, atol=1e-2)


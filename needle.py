# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 08:54:34 2019

@author: 600301
"""
# Third party imports
import pandas as pd
# Local application/library-specific imports
from .utils import EndPrecedesStartError

class AfterHoursError(Exception):
    """An error for situations when someone tries to ride a needle when
    it's closed.

    Args:
        needle (SeattleAttraction): Which needle someone tried to ride.
        early_or_late (str): Either 'early' or 'late', to indicate
            which time constraint is violated.
    """
    def __init__(self, needle, early_or_late):
        if early_or_late.lower() == 'early':
            self.msg = "Tried to ride ", needle.needle, " before opening."
        else:
            self.msg = "Tried to ride ", needle.needle, " after closing."

# What follows in parentheses is the type of object that your class
# extends, not the arguments to its constructor.  Those are in the __init__
# function.  However, the __init__ function is documented in the class
# docstring.
class SeattleAttraction(object):
    """A class for all seattle-based needle attractions

    Args:
        needle_type (str): Type of needle, e.g. "space"
        opening (str): Time needle opens to public, preferably in format
            ``08:00:00``
        closing (str): Time needle closes to public.

    Examples:
        `space_needle = SeattleAttraction()`
        `grunge_needle = SeattleAttraction('Nirvana', '00:00:01', '03:59:59')`
    """

    def __init__(self, needle_type='space', opening='08:00:00',
                 closing='23:59:00'):
        opening = pd.to_datetime('2019 Jan 1 '+opening)
        closing = pd.to_datetime('2019 Jan 1 '+closing)
        if opening < closing:
            raise EndPrecedesStartError(needle_type, opening.time(),
                                        closing.time())
        self.needle = needle_type + ' needle'
        self.opening = opening.time()
        self.closing = closing.time()

    def ride(self, start, end):
        """Validates that you can ride the needle from start to end,
        and returns the needle type.

        Args:
            start (str): when you try to start riding, preferably in format
                ``08:00:00``
            end (str): when you try to finish riding
        """

        if pd.to_datetime('2019 Jan 1 '+start).time < self.opening:
            raise self.AfterHoursError(start, 'early')
        elif pd.to_datetime('2019 Jan 1 '+end).time > self.closing:
            raise self.AfterHoursError(end, 'late')
        return self.needle


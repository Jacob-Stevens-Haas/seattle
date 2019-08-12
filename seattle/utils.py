# -*- coding: utf-8 -*-
"""utils.py module proides functions to record rides of attractions.

.. _load\_records
.. _save\_records
.. _add\_ride

Attributes:
    data_dir (pathlib Path): path to the data directory in the module.

Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
Much of this example comes from:
    https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""
# Standard library imports
from pathlib import Path
# Third party imports
import pandas as pd


# It's better to handle file paths with Path() objects than strings
# They work on unix, mac, and windows and they overload the `/` operator
# to join file paths.
# On python 3.6+, you can open Path objects directly, rather than
# having to cast the Path as a str first.
data_dir = Path(__file__).parent.parent / 'data'
# Forces SettingWithCopyWarning to raise an exception, so that you
# can get a traceback and exception when it happens.
pd.options.mode.chained_assignment = 'raise'


class EndPrecedesStartError(Exception):
    """This is a custom exception.  It's useful if you might have
    similar situations in your code that you want to disallow.  Since
    you can't predict every situation that might give rise to a
    disallowed situation, it's helpful to create an exception.  Then,
    each block of code that gives rise to the exception can handle
    the exception differently.

    A classic case in point is updating a database or table with start
    and end times.  There's nothing about a table or database's
    engineering that prohibits a column named "end" from preceding
    a column named "start".  Below is a function that updates the table
    for new records.  We don't know yet whether the function will be
    called, so we don't worry about how to handle the exception, we just
    raise it.

    Later, someone may write a function that calls add_ride
    based on user input in a web form.  They would want to catch the
    exception and pass the message in the web page itself.  On the other
    hand, someone might call add_ride to add a batch of rides for adding
    a batch of rides from a file.  They might want to catch the exception,
    keep adding rides for the rest of the batch, then report to the user
    all the illegal rides at once.

    Args:
        attraction (SeattleAttraction): Which attraction was attempted
        start (str or datetime.time): What start time was attempted
        end (str or datetime.time): What end time was attempted
    """

    def __init__(self, attraction, start, end):
        self.message = ('Attempting to ride or create', str(attraction),
                        ' from time', str(start), ' to time ', str(end),
                        ' but start must preceed end.  Please note that ',
                        'all rides must close before midnight.')

def load_records(rec_file =  'records.csv'):
    """Loads records from the saved data.

    Args:
        rec_file (str): records file to load.  If "new", create new
            DataFrame with appropriate columns

    Raises:
        AssertionError if file's DataFrame does not have correct columns

    Returns:
        pandas DataFrame
    """
    if rec_file == 'new':
        return pd.DataFrame([],
                columns=['person', 'attraction', 'start', 'end'])

    df = pd.read_csv(data_dir / rec_file)
    assert len({'person','attraction','start','end'}-set(df.columns)
                ) == 0, str(rec_file) + " is missing some columns"
    return df

def save_records(df, rec_file = 'records.csv'):
    """Saves records in df to rec_file."""
    return df.to_csv(data_dir / rec_file)

def add_ride(records, attraction, person, start, end):
    """Updates the records, for person to take the needle's elevator
    up at start and down at end.

    Args:
        records (pandas DataFrame): The list of records of all rides
        needle (SeattleAttraction) : Which needle (e.g. space)
        person (str): who is riding the elevator up and down
        start (str, pandas DateTime) : time person embarked elevator
        end (end) : time person returned to ground

    Raises:
        EndPrecedesStartError

    Returns:
        New records DataFrame with record appended
    """

    if pd.to_datetime(end) <= pd.to_datetime(start):
        raise EndPrecedesStartError(str(attraction), start, end)

    #include line breaks every 80 characters
    return records.append(pd.DataFrame(
            [[person, attraction.ride(start, end), start, end]],
                    columns=['person', 'attraction', 'start', 'end']))

"""
Operators to calculate various kinds of averages.
"""

from datetime import datetime
from iris.cube import CubeList


def time_mean(
    cube: CubeList,
    field: str,
    start_time: datetime = None,
    end_time: datetime = None,
) -> CubeList:
    """
    Averages a field over the time period specified.

    Parameters
    ----------
    cube: Cube
        An iris cube of the data to average.

    field: str
        The variable to average.

    start_time: datetime, optional
        The time to start averaging from. If None averages from the earliest
        instance of the data.

    end_time: datetime, optional
        The time to average until. If None averages until the latest instance of
        the data.

    Returns
    -------
    Cube
        A cube containing the averaged field.

    Raises
    ------
    IndexError
        If the cube does not contain `field`.

    Notes
    -----
    Not yet implemented.
    """
    pass

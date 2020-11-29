"""Functions used to create a visibility graph"""
import pandas as pd 
# TODO - maybe remove these later, used for optimizing number of calls 
CALLS_CONNECTEDNESS = 0
CALLS_POINTS_CONNECTED = 0


def connectedness_criteria_mid(y, left, right, mid):
    """Evaluate connectedness of two points based on a single midpoint
    
    Formula (1) in Lacasa et al 2008. This is the core of how a time
    series is turned into a visibility graph.
    
    For any two points, all of the points between them must pass this
    criteria, else the points will not be connected in the graph. 
    
    This evalates one point "c" (mid) between "a" (left) and "b"
    (right).
    
    """
    global CALLS_CONNECTEDNESS
    # TODO - drop assertions, or provide option to suppress for speed
    msg = (f'mid must be between left and right.')
    assert mid > left and mid < right, msg
    msg = (f'right must be greater than left')
    assert right > left, msg
    
    CALLS_CONNECTEDNESS += 1
    return y[mid] < y[right] + (y[left] - y[right])*((right-mid)/(right-left))


def points_connected(x, y, left, right):
    """Evaluate connectedness of two points"""
    global CALLS_POINTS_CONNECTED
    # assume first that is connected 
    # note that all adjacent points on the time series are connected 
    is_connected = True

    # if not adjacent, evaluate all points between
    if right - left > 1:
        # for every point between left and right (exclusive)...
        for mid in x[left+1:right]:
            # ... test, if fails connectedness test, terminate loop and 
            # label as not connected 
            if not connectedness_criteria_mid(y, left, right, mid):
                is_connected = False
                break
                
    CALLS_POINTS_CONNECTED += 1
    return is_connected


def create_edges(x, y):
    """docstring for create_gaph

    TODO - Write descriptive docstring for create_gaph function.

    Parameters
    ----------
     : <class>
        <desc>

    Returns
    -------
    <varname : class>
        <desc>

    """
    # create graph edges
    edges = list()

    for left in x:
        for right in x[left+1:]:
            if points_connected(x, y, left, right):
                edges.append((left, right))

    return edges

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

    Parameters
    ----------
    y : list
        y values of time series. 

    left, right, mid : int
        Indices of y that correspond to the points to be evaulated,
        where mid is the point between x left and right.

    Returns
    -------
    is_connected : bool
        Truth value of connectedness of two points, based only on the
        point mid. 

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
    """Returns True if two points are connected, else False 

    Function connectedness_criteria_mid is applied across every point
    that is between `left` and `right`. If the connectedness criteria
    fails to hold for any mid point, False is returned, otherwise True
    is returned

    Parameters
    ----------
    x, y : list
        Lists that are the time series. 

    left, right : int
        Indices of y that correspond to the points to be evaulated. 

    Returns
    -------
    is_connected : bool
        Truth value of connectedness of two points. 

    """
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
    """Creates an edge set of a visibility graph from time series x,y

    Create visiblity graph from a time series. Argument `x` is the time
    dimension of the series, and argument `y` is the "height" of the
    time series at position `x`. 

    For every x_i in x, func `points_connected` is used to evaluate
    every other point x_j in x. Points are evaluated from left to right,
    so that no two points are evaluated twice. 

    Additional work could be done to speed up this function, this isn't
    likely a fast implementation. 

    Parameters
    ----------
    x, y : list
        Lists that are the time series. 

    Returns
    -------
    edges : list of tuples
        List of tuples that represent edges. 

    """
    # create graph edges
    edges = list()

    for left in x:
        for right in x[left+1:]:
            if points_connected(x, y, left, right):
                edges.append((left, right))

    return edges

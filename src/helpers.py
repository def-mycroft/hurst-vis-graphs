"""Misc functions used in notebook"""
from matplotlib import pyplot as plt


def intro_plot(x, y, edges=None, figsize=(12,4)):
    """Creates the barplots used in the intro 

    Parameters
    ----------
    x, y : list
        The time series data to plot.

    Returns
    -------
    fig : matplotlib fig
        Figure object that is the graph (plot). 

    """
    # setup the figure
    fig = plt.figure(figsize=figsize)
    ax = plt.subplot(111)
    ax.bar(x,y)
    ax.xaxis.set(ticks=x)

    # if edges passed, then plot them as grey lines 
    if edges:
        for e in edges:
            ax.plot(e, [y[i] for i in e], color='grey')
             
    ax.grid()

    return fig

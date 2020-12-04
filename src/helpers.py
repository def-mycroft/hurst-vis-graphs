"""Misc functions used in notebook"""
from matplotlib import pyplot as plt
from src.fbm.fbm import FBM # see source or https://pypi.org/project/fbm/


def plot_fbm_examples(hurst1=0.5, hurst2=0.75, hurst3=0.25):
    """Plots randomly-generated Fractional Brownian Motion series

    TODO - Write descriptive docstring for plot_fbm_examples function.

    Parameters
    ----------
     : <class>
        <desc>

    Returns
    -------
    <varname : class>
        <desc>

    """
    f = lambda hurst: FBM(n=1024, hurst=hurst, length=1, 
                          method='daviesharte').fbm()

    # create figure
    fig = plt.figure(figsize=(10,6))

    def add(ax, hurst=0.5, color='blue'):
        """Plot a fbm series"""
        y = f(hurst)
        ax.plot(range(len(y)), y, color=color)
        plt.grid()
        ax.set(title=f'Fractional Brownian Motion (H={hurst:.2f})')
        
    # add three plots
    ax1 = fig.add_subplot(311)
    add(ax1, hurst=hurst1)

    ax2 = fig.add_subplot(312)
    add(ax2, hurst=hurst2, color='red')

    ax3 = fig.add_subplot(313)
    add(ax3, hurst=hurst3, color='green')

    plt.tight_layout()


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

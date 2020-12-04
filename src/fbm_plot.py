"""Plot sample realizations of Fractional Brownian Motion

The series here are generated using the fbm project, see source code in this
folder or visit https://pypi.org/project/fbm/ for more information. 

"""
from src.fbm.fbm import FBM 
from matplotlib import pyplot as plt


def plot_fbm_examples(hurst1=0.5, hurst2=0.75, hurst3=0.25):
    """Plots randomly-generated Fractional Brownian Motion series
    
    Creates three different realizations of fbm and plots them on the
    same x-axis to allow for comparison. 

    Parameters
    ----------
    hurst1, hurst2, hurst3 : float
        The Hurst parameters to plot. Must be in (0,1). Values closer to
        1 create series that are more persistent and values closer to 0
        create series that are more antipersistent. A value of 0.5
        creates a series that is independent. 

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



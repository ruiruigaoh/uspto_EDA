import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Make lineplot
def lineplot(data, *, x, y, hue, ax=None, xlabel=None, ylabel=None, **prop_kwargs):
    
    # Assign categories to a list for marker assignment
    data = data
    categories = data['category'].unique()
    
    # Cosmetic parameters
    cos_kwargs = dict(
    palette='RdYlBu', 
    style='category', 
    dashes=False,
    markers=dict(zip(categories, ['o']*len(categories))), 
    markeredgecolor='black', 
    markersize=4
    )
    
    # Make plot
    if ax is None:
        ax = plt.gca()
    sns.lineplot(data=data, x=x, y=y, hue=hue, ax=ax, **cos_kwargs)
    
    # Set and adjust labels/legends
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5), 
          fontsize='small', title='Patent categories', 
          alignment='left', frameon=False)

# Make stacked barplot
def stackedbar(data, xlabel=None, ylabel=None, ax=None, legend_title=None, **prop_kwargs):
    
    # Set variables
    x = data.index
    categories = data.columns
    
    # Set colors
    colors = sns.color_palette('RdYlBu', len(categories)).as_hex()
    
    # Initialize the bottom at zero for the first set of bars
    bottom = np.zeros(len(data)) 
    
    # Make plot
    if ax is None:
        ax = plt.gca()
    for category, color in zip(categories, colors):
        ax.bar(x=x, 
               height=data[category], width=0.8,
               label=category, bottom=bottom, color=color, 
               edgecolor='black', lw=0.2, **prop_kwargs)
        bottom += np.array(data[category])
    
    # Set and adjust labels/legends
    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.legend(loc='center left', bbox_to_anchor=(1,0.5), 
          fontsize='small', title=legend_title, 
          alignment='left', frameon=False)
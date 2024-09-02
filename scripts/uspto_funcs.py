import pandas as pd
import numpy as np
from scipy import stats
import re

def categorize(x, regex=None, mapping_dict=None, default='other'):
    '''
    Categorizes each application by matching the value of
    a variable to an existing mapping dictionary.
    
    Args:
        x: The value of a variable -> str 
        regex: A regex object of patterns to be matched
        mapping_dict: A mapping dictionary -> dict
        default: The default string if no matches are found
    
    Return:
        Matched string -> str
    '''
    match = regex.search(x)
    if match:
        return mapping_dict[match.group().lower()]
    else:
        return default
    
def pendency(df_in, issue_col, filing_col):
    '''
    Creates a new column that reports pendency, also 
    dropping rows for which pendency is NaN
    
    Args:
        df_in: A pandas df
        issue_col: Column of issued dates -> str
        filing_col: Column of filing dates -> str
        
    Return:
        df_out: A pandas df with pendency values reported
        in new column 'pendency', with rows dropped where
        pendency values were NaN
    '''
    df_out = df_in.copy()
    df_out['pendency'] = (df_out[issue_col]-df_out[filing_col]) / np.timedelta64(1, 'M')
    df_out.dropna(subset='pendency', inplace=True)
    return df_out

def examiner_calc(df_in, cutoff=None):
    '''
    Takes a dataframe with pendency data (optionally subset by
    a cutoff filing year) and calculates several pendency stats
    for each examiner: mean, standard deviation, count (number of 
    applications examined), and the SEM. Also calculates the boundary 
    values for the 95% CI of the mean as well as the half-width of 
    the 95% CI for more streamlined plotting down the road.
    
    Args:
        df_in: A pd dataframe object
        cutoff: (optional) A filing year as cutoff threshold -> int
    
    Return:
        df_copy: A copy of df_in with additional columns representing
        pendency stats
        fastest: A new pd dataframe with the ten fastest examiners by
        pendency
        slowest: A new pd dataframe with the ten slowest examiners by
        pendency
    '''
    # Subset by chosen cutoff year if provided
    if cutoff:
        df_copy = df_in.loc[df_in['filing_date'].dt.year > cutoff].copy()
    else:
        df_copy = df_in.copy()

    # Group by examiner name and get some stats for pendency per examiner
    df_copy = df_copy.groupby('examiner_full_name')['pendency'].agg(['mean', 'std', 'count', 'sem'])
    # Remove examiners with fewer than 5 applications
    df_copy = df_copy.loc[df_copy['count'] >= 5].reset_index()

    # Calculate 95% CI boundary values
    nums = zip(df_copy['mean'], df_copy['count'], df_copy['sem'])
    ci = map(lambda x: stats.t.interval(confidence=0.95, df=x[1]-1, loc=x[0], scale=x[2]), nums)
    lower, upper = list(zip(*ci))  # Unzip T to get all the lower bounds and upper bounds together
    
    # Combine with ex_stats
    new_cols = pd.DataFrame({'lower': lower, 'upper': upper})
    df_copy = pd.concat([df_copy, new_cols], axis=1)
    
    # Get the half-width (margin error) of the 95% CI for easier plotting later
    df_copy['meCI'] = df_copy['mean']-df_copy['lower']
    
    # Create df with fastest examiners
    fastest = df_copy.sort_values(by='mean', ascending=False).tail(10).copy()
    # Create df with slowest examiners
    slowest = df_copy.sort_values(by='mean', ascending=False).head(10).copy()
    
    return df_copy, fastest, slowest

def mean_diff_sig(df_in, var):
    '''
    For a chosen variable represented by boolean values(True/False), 
    calculates some stats to test for differences in mean pendencies 
    (using geometric mean) between the True ('treated') and False
    ('control') conditions. 
    The following stats are calculated: geometric mean of 
    control, geometric mean of treated, difference in geom. means, difference
    as a percent of treated geom. mean, unpaired t-test statistic, and
    p-value of the t-test.
    
    Args:
        df_in: pandas dataframe object 
        var: variable of interest represented by True/False -> str
    
    Returns:
        A dict of stats -> dict
    '''
    control = np.log10(np.asarray(df_in[df_in[var] == False]['pendency']))
    treated = np.log10(np.asarray(df_in[df_in[var] == True]['pendency']))
    # Calculate diff in geom means
    control_gmean = 10**np.mean(control)
    treated_gmean = 10**np.mean(treated)
    gmean_diff = treated_gmean-control_gmean
    # Express mean diff as percent of control
    diff_as_percent = gmean_diff/control_gmean*100
    # Unpaired t-test
    tstat, p = stats.ttest_ind(control, treated)
    results_dict = {'control gmean': control_gmean, 
                   'treated gmean': treated_gmean, 
                   'diff in gmeans': gmean_diff, 
                   'diff in gmeans as %': diff_as_percent, 
                   't-stat': tstat, 
                   'p-value': p}
    return results_dict

def divide_by_baseline(x):
    '''
    Identifies a 'baseline year' (the earliest year with filed
    applications) and counts the number of applications
    for that baseline year. Then for each successive year after,
    divides the number of applications by the baseline count so
    that the number of applications is "normalized" to a baseline.
    
    Args:
        x: A dataframe
    
    Returns:
        x: A dataframe with a new column representing
        number of applications normalized to baseline
    '''
    baseline_year = x[x['counts'].notna()]['Filing_Date'].min()
    baseline_count = x[x['Filing_Date'] == baseline_year]['counts'].values[0]
    x['norm_to_baseline'] = x['counts'] / baseline_count
    return x

def unique_and_prop(df_in, col=None, groups=None):
    '''
    Groups a dataframe by variables given in 'groups', 
    then the number of unique applications filed by 
    each city's inventors, as well as that number represented as
    a percent of the total applications.
    '''
    # Get the total number of unique applications
    total = df_in[col].nunique()
    # Group by city name and state and calculate unique apps
    S = df_in.groupby(groups)[col].apply('nunique')
    df_out = pd.DataFrame(S).reset_index().rename(columns={col:'unique_counts'})
    # Calculate the unique apps as a percent of the total
    df_out['prop_of_total'] = df_out['unique_counts']/total * 100
    return df_out
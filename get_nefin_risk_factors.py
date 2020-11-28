import pandas as pd

def get_nefin_risk_factors(out = 'df'):
    """
    Downloads brazilian daily risk factors data from 
    http://nefin.com.br/risk_factors.html and outputs it as a df or dict of dfs.

    Parameters
    ----------
    out = 'df' or 'dict'

    Returns
    -------
    Pandas Data Frame if out = 'df',
    Dictionary of pandas data frames if out = 'dict'
    """ 
    
    if out not in {'df', 'dict'}:
        raise ValueError("out must be 'df' or 'dict'")

    factors = ['Market_Factor', 'SMB_Factor', 'HML_Factor', 'WML_Factor',
               'IML_factor', 'Risk_Free'] 
    url = 'http://nefin.com.br/Risk%20Factors/{}.xls'
    dfs = {}

    for factor in factors:
        dfs[factor] = pd.read_excel(url.format(factor))
        dfs[factor]['Date'] = pd.to_datetime(dfs[factor][['year', 'month', 'day']])
        dfs[factor] = dfs[factor].drop(columns=['year', 'month', 'day'])
        dfs[factor] = dfs[factor].set_index('Date')
        dfs[factor] = dfs[factor].iloc[:,0]

    if out == 'df':
        return pd.DataFrame.from_dict(dfs)
    else:
        return dfs

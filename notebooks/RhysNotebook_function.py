import pandas as pd

def load_and_process(url):
    """
    first line: loading my dataset to the dataframe
    second line: dropping any lines that contain NaN values. Can't use these to rank goalies.
    """
    df1 = (
            pd.read_csv(url, low_memory = False)
            .dropna()
            )
    
    """
    first line: rename some columns so they are more readable
    second line: combining the goalies by their numbers.  then averages out all of their stats across games.
    third line: creates a new columns "PKSavePercentage". combines shortHandedShotsAgainst and
    shortHandedSaves to get their save percentage on the penalty kill.
    fourth line: drops columns that won't be useful for the final analysis.
    fifth line: sorts from highest penalty kill save percentage to lowest.
    """
    df2 = (
           df1
            .rename(columns = {'powerPlaySavePercentage': 'PPSave%',
                              'evenStrengthSavePercentage': 'evenSave%',
                              'player_id': 'playerID',
                              'game_id': 'gameID'})
            .groupby('playerID').mean()
            .assign(PKSavePercentage=lambda x:(x.shortHandedSaves/x.shortHandedShotsAgainst)*100) 
            .drop(['team_id', 'timeOnIce', 'assists', 'goals',
                   'pim', 'shots', 'saves', 'powerPlaySaves', 'shortHandedSaves',
                   'evenSaves', 'shortHandedShotsAgainst', 'evenShotsAgainst',
                   'powerPlayShotsAgainst'], axis=1)
            .sort_values(by=["PKSavePercentage"], ascending = False)
           
        )
   
    """
    first line: drop any PKSavePercentages (our new column) that has NaN values
    second line: goalies with 100% PKSavePercentages is impossible if they've played enough games
    in order to get rid of these, for example, backup goalies who have played few games and whose 
    data is skewed, we will filter out anybody with a 100% save rate on the penalty kill
    """
    df3 = (
        df2
        .dropna()
        )
    
    
    return df3
          
def barGraphs(link):
    """
    first line: loading my dataset to the dataframe
    second line: dropping any lines that contain NaN values. Can't use these to rank goalies.
    """
    df1 = (
            pd.read_csv(link, low_memory = False)
            .dropna()
            )
    
    """
    first line: rename some columns so they are more readable
  
    third line: creates a new columns "PKSavePercentage". combines shortHandedShotsAgainst and
    shortHandedSaves to get their save percentage on the penalty kill.
    fourth line: drops columns that won't be useful for the final analysis.
    fifth line: sorts from highest penalty kill save percentage to lowest.
    """
    df2 = (
           df1
            .rename(columns = {'powerPlaySavePercentage': 'PPSave%',
                              'evenStrengthSavePercentage': 'evenSave%',
                              'player_id': 'playerID',
                              'game_id': 'gameID'})
            .assign(PKSavePercentage=lambda x:(x.shortHandedSaves/x.shortHandedShotsAgainst)*100) 
            .sort_values(by=["PKSavePercentage"], ascending = False)
           
        )
    
    return df2







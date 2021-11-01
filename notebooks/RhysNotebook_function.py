#!/usr/bin/env python
# coding: utf-8

# # Rhys Elliott

# ## Research question/interests
# 
# One of the most important aspects obeing a NHL goalies is being able to perform under pressure.  I will analyze which NHL goalies have the highest save rate while shorthanded and comparing it to their even strength save percentage.  Their "clutch factor"  will also be compared to their win rate to give an idea of how key of a role they played in their victories.s.

# In[4]:


import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

APINHLStatistics = pd.read_csv("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742", low_memory=False)
APINHLStatistics = APINHLStatistics.dropna()
APINHLStatistics


# # Milestone 3

# Task 1

# In[34]:


APINHLStatistics.columns


# In[35]:


APINHLStatistics.shape


# In[36]:


APINHLStatistics.head()


# In[37]:


APINHLStatistics.index


# In[38]:


type(APINHLStatistics)


# In[39]:


APINHLStatistics.info()


# In[40]:


APINHLStatistics['decision']


# In[41]:


subset = APINHLStatistics[['game_id', 'shots', 'saves']]
subset


# In[44]:


APINHLStatistics.loc[APINHLStatistics['decision'] == 'W', ['shots', 'saves']]


# In[46]:


APINHLStatistics.describe().apply(lambda s: s.apply(lambda x: format(x, 'f')))


# Task 2

# In[170]:


APINHLStatistics = pd.read_csv("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742", low_memory=False)
APINHLStatistics = APINHLStatistics.dropna()

APINHLStatistics["PKSave%"] = (
    APINHLStatistics["shortHandedSaves"] / APINHLStatistics["shortHandedShotsAgainst"]
                              )*100


# In[171]:


APINHLStatistics = APINHLStatistics.rename(columns = {'powerPlaySavePercentage': 'PPSave%',
                                                      'evenStrengthSavePercentage': 'evenSave%',
                                                      'player_id': 'playerID',
                                                      'game_id': 'gameID'
                                                     }
                                          )


# In[174]:


APINHLStatistics = APINHLStatistics[['playerID', 'PPSave%', 'PKSave%', 'evenSave%']]
APINHLStatistics.sort_values(by=["PKSave%"], ascending = False)
APINHLStatistics.groupby('playerID').mean()


# Task 3

# In[114]:


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
          
def barGraphs(url):
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

# In[91]:


df1 = load_and_process("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742")
df1=df1.iloc[:-3, :]
df1_mask = df1.query('PKSavePercentage > 50')


# Task 4

#  #### Analysis
#  
#  - Over two NHL seasons, there were a total of 322 goalies who played
#  - Of those, only 243 had to kill a penalty (short handed)
#  -  Many of the best goalies had a penalty kill save percentage that was higher than their even strength save percentage.
#  - Many of the goalies with a high PKSavePercentage have a lower PPSavePercentage.  This means they let in more goals per shots faced when they are on the powerplay than when they are killing a penalty.
#  

# #### Pandas Profiling Analysis
# 
# - From the profiling report, aside from saves, goalies don't offer any more statistics.  Their goals, assists and PIM are averaged at less than 1.
# - The most goals a goalies scored in a game is 1 which is quite impressive! The most assists in a game is 2.
# - One goalie managed to rack up 27 penalty minutes in a single game! That's 300 times the mean.
# - The min for short handed saves was -1.  This mean the opponent must've scored without shooting.  This is a result of an own-goal.

# In[116]:


import RhysNotebook_function

df = RhysNotebook_function.load_and_process("https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B23RG6RJKXAKVX6R43BQ4742")
df


# In[117]:


plot1 = sns.scatterplot(data=df,x="playerID", y="PKSavePercentage")
plot1.axhline(85)
plt.show()


# In[93]:


sns.rugplot(df['PKSavePercentage'])


# #### Graph Analysis
# The above scatter plot demonstrates penalty kill save percentage of the goalies compared to their playerID.  It demonstrates that the most of goalies have  high save percentages when they are at a disadvantage of players (75% or above).  This could suggest that many of the goalies are well suited for the pressure of being disadvantaged and being able to consistently perform well.  Similarly, but not as well demonstrated, the rug plot shows more dense lines towards the 75%-95%

# In[62]:


corr = df.corr()
plot2 = sns.heatmap(corr)
plt.show()


# #### Graph Analysis
# 
# The above heatmap demonstrates the correlation between the average save percentages of each goalie.  As we can see, there is a very strong correlation between the average save percentage and the even save percentage.  In contrast, there is little correlation between the penalty kill save percentage and the average save percentage.  This suggests that when average save percentage changes, even save percentage changes more than the penalty kill save percentage, suggesting that the latter makes up less of the overall average save percentage statistic.  The powerplay save statistic lies in between both of them. 

# In[84]:


plt.subplot(1,2,1)
sns.barplot(x="decision", y="PKSavePercentage",data=df, estimator=np.median)

plt.subplot(1,2,2)
sns.barplot(x="decision", y="PPSave%",data=df, estimator=np.median)


# #### Graph Analysis
# The above bar graphs demomstrate the percentage difference between save percentages for wins and losses.  For the penalty kill save percentages, it makes nearly no difference on the goalies penalty kill save percentage on the outcome of the game.  However, during power plays, having a higher save percentage makes a signifcant impact, nearly 10% difference in whether that team will win.  This could be a result of in game momentum, and being scored on while you have a man advantage could be discouraging resulting in a loss.

# In[ ]:





# In[67]:





# In[ ]:





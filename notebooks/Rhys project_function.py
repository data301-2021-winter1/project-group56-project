{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "a0d745f7-1e11-4dc4-8763-5b207378c03b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "621bfb75-bfc1-4fd8-a274-96419ad89dd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(url):\n",
    "    \"\"\"\n",
    "    first line: loading my dataset to the dataframe\n",
    "    second line: dropping any lines that contain NaN values. Can't use these to rank goalies.\n",
    "    \"\"\"\n",
    "    df1 = (\n",
    "            pd.read_csv(url, low_memory = False)\n",
    "            .dropna()\n",
    "            )\n",
    "    \n",
    "    \"\"\"\n",
    "    first line: rename some columns so they are more readable\n",
    "    second line: combining the goalies by their numbers.  then averages out all of their stats across games.\n",
    "    third line: creates a new columns \"PKSavePercentage\". combines shortHandedShotsAgainst and\n",
    "    shortHandedSaves to get their save percentage on the penalty kill.\n",
    "    fourth line: drops columns that won't be useful for the final analysis.\n",
    "    fifth line: sorts from highest penalty kill save percentage to lowest.\n",
    "    \"\"\"\n",
    "    df2 = (\n",
    "           df1\n",
    "            .rename(columns = {'powerPlaySavePercentage': 'PPSave%',\n",
    "                              'evenStrengthSavePercentage': 'evenSave%',\n",
    "                              'player_id': 'playerID',\n",
    "                              'game_id': 'gameID'})\n",
    "            .groupby('playerID').mean()\n",
    "            .assign(PKSavePercentage=lambda x:(x.shortHandedSaves/x.shortHandedShotsAgainst)*100) \n",
    "            .drop(['gameID', 'team_id', 'timeOnIce', 'assists', 'goals',\n",
    "                   'pim', 'shots', 'saves', 'powerPlaySaves', 'shortHandedSaves',\n",
    "                   'evenSaves', 'shortHandedShotsAgainst', 'evenShotsAgainst',\n",
    "                   'powerPlayShotsAgainst'], axis=1)\n",
    "            .sort_values(by=[\"PKSavePercentage\"], ascending = False)\n",
    "        )\n",
    "   \n",
    "    \"\"\"\n",
    "    first line: drop any PKSavePercentages (our new column) that has NaN values\n",
    "    second line: goalies with 100% PKSavePercentages is impossible if they've played enough games\n",
    "    in order to get rid of these, for example, backup goalies who have played few games and whose \n",
    "    data is skewed, we will filter out anybody with a 100% save rate on the penalty kill\n",
    "    \"\"\"\n",
    "    df3 = (\n",
    "        df2\n",
    "        .dropna()\n",
    "        .query('PKSavePercentage != 100')\n",
    "         )\n",
    "    \n",
    "    return df3"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

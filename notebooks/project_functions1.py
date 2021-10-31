{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1d533920-31ea-4f5b-9a99-b5a6f993eb48",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "483bd4be-29b8-43e2-ae09-e9b070140c17",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e944f3b1-7182-4ee3-af40-5e07a36fdaff",
   "metadata": {},
   "outputs": [
    {
     "ename": "ImportError",
     "evalue": "attempted relative import with no known parent package",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mImportError\u001b[0m                               Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-4-43f0f1a752f8>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0;34m.\u001b[0m\u001b[0;34m.\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mproject_functions\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mproject_functions\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload_and_process\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B34PHXTJXIZZJFKLADBNDLIO\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mImportError\u001b[0m: attempted relative import with no known parent package"
     ]
    }
   ],
   "source": [
    "from .. import project_functions\n",
    "df = project_functions.load_and_process(\"https://raw.githubusercontent.com/data301-2021-winter1/project-group56-project/main/data/raw/APINHLStatistics.csv?token=AVRK7B34PHXTJXIZZJFKLADBNDLIO\")\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "35dc57e3-742b-4926-8604-ad7880ef5de9",
   "metadata": {},
   "outputs": [],
   "source": []
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

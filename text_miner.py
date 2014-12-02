# Import modules
import numpy as np
import pandas as pd

# Define text miner function
def text_miner(text, miner):
    df = pd.DataFrame(np.zeros((len(text), len(miner))), columns=miner.keys())
    for key in miner:
        df[key] = text.str.contains('|'.join(miner[key]), case=False)
    return df.astype('int32')

# Create text series and miner dictionary
text = pd.Series(['I ran to Iran', 'You back Iraq', 'England is bland', 'We dance in France', 'They wait in Kuwait'])
miner = {'middle_east': ['Iran', 'Iraq', 'Kuwait'],
         'verb': ['ran', 'back', 'dance', 'wait']}

# Apply text miner
mined_text_df = text_miner(text, miner)

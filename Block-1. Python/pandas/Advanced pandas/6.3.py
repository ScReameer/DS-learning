import pandas as pd
import os


PATH = './Root/users/'

def concat_user_files(path):
    
    all_files = sorted(os.listdir(path))
    result_df = pd.DataFrame()
    
    for file in all_files:
        
        file_df = pd.read_csv(PATH+file)
        result_df = pd.concat([result_df, file_df], ignore_index=True).drop_duplicates(ignore_index=True)
    
    return result_df
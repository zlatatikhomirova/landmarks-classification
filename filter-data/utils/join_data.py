import pandas as pd
import os
from google.colab import drive

drive.mount('/content/drive/')

DATA_PATH = '/content/drive/MyDrive/data-landmark/data'

def merge_csvs(paths: list) -> pd.DataFrame:
  dfs = []
  for path in paths:
    df = pd.read_csv(path)
    dfs.append(df)
  return pd.concat(dfs)

def full_paths(path):
   files = os.listdir(path)
   full_paths = []
   for f in files:
      full_path = os.path.join(path, f)
      full_paths.append(full_path)
   return full_paths

places_paths =  full_paths(os.path.join(DATA_PATH, 'data-places'))
imgs_paths = full_paths(os.path.join(DATA_PATH, 'data-images'))

df_places = merge_csvs(places_paths).reset_index()
df_imgs = merge_csvs(imgs_paths).reset_index()

df_places.to_csv(os.path.join(DATA_PATH, 'data-merged', 'places_merged.csv'))
df_imgs.to_csv(os.path.join(DATA_PATH, 'data-merged', 'imgs_merged.csv'))

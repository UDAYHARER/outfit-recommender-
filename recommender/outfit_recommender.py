# Make sure the recommender directory exists 
!mkdir -p recommender 
# Create outfit_recommender.py with the recommender class
with open("recommender/outfit_recommender.py","w") as f: f.write(""" 
import pandas as pd 
class OutfitRecommender: 
  def __init__(self, csv_path): 
    self.data = pd.read_csv(csv_path) 
  def recommend(self, color=None, occasion=None): 
    result = self.data 
    if color: 
      result = result[result['color'].str.lower() ==  color.lower()] 
    if occasion: 
      result = result[result['occasion'].str.lower() ==  occasion.lower()]
      return result['outfit'].tolist() """)

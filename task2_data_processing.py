import glob
import os
import pandas as pd


def clean_trend_data():
  """Loads raw trend JSON data, cleans duplicates and nulls,

  filters low scores, formats text, saves to CSV, and prints summaries.
  """
  # ---------------------------------------------------------------------------
  # Task 1 — Load the JSON File
  # ---------------------------------------------------------------------------
  # Dynamically find the trends JSON file inside the data/ folder
  json_files = glob.glob('data/trends_*.json')

  if not json_files:
    raise FileNotFoundError(
        'Error: No trends JSON file found matching "data/trends_*.json".'
    )

  json_path = json_files[0]

  # Load the JSON file into a Pandas DataFrame
  df = pd.read_json(json_path)
  print(f'Loaded {len(df)} stories from {json_path}')

  # ---------------------------------------------------------------------------
  # Task 2 — Clean the Data
  # ---------------------------------------------------------------------------

  # 1. Remove duplicate rows based on 'post_id'
  df = df.drop_duplicates(subset=['post_id'])
  print(f'After removing duplicates: {len(df)}')

  # 2. Drop rows where post_id, title, or score is missing (null)
  df = df.dropna(subset=['post_id', 'title', 'score'])
  print(f'After removing nulls: {len(df)}')

  # 3. Convert score and num_comments to proper integer types
  df['score'] = pd.to_numeric(df['score'], errors='coerce').astype(int)
  df['num_comments'] = pd.to_numeric(
      df['num_comments'], errors='coerce'
  ).astype(int)

  # 4. Filter out stories with a score less than 5
  df = df[df['score'] >= 5]
  print(f'After removing low scores: {len(df)}')

  # 5. Strip extra whitespace from the 'title' column
  df['title'] = df['title'].str.strip()

  # ---------------------------------------------------------------------------
  # Task 3 — Save as CSV
  # ---------------------------------------------------------------------------
  # Ensure the data directory exists
  os.makedirs('data', exist_ok=True)
  output_path = 'data/trends_clean.csv'

  # Save the cleaned DataFrame to CSV without index
  df.to_csv(output_path, index=False)
  print(f'Saved {len(df)} rows to {output_path}')

  # Print stories per category summary
  print('Stories per category:')
  category_counts = df['category'].value_counts()
  for category, count in category_counts.items():
    print(f'  {category:15} {count}')


if __name__ == '__main__':
  clean_trend_data()
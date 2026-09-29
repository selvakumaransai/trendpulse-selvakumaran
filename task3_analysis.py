import os
import numpy as np
import pandas as pd


def analyze_trends():
  """Loads cleaned trend data, performs statistical computations using Pandas

  and NumPy, adds derived columns, and saves the final analyzed dataset.
  """
  # ---------------------------------------------------------------------------
  # Task 1 — Load and Explore
  # ---------------------------------------------------------------------------
  csv_path = "data/trends_clean.csv"

  if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f"Error: Cleaned dataset not found at {csv_path}. Please run Task 2 first."
    )

  # Load the clean CSV into a Pandas DataFrame
  df = pd.read_csv(csv_path)

  # Print shape and preview first 5 rows
  print(f"Loaded data: {df.shape}")
  print("First 5 rows:")
  print(df.head())
  print()

  # Print overall average score and average comments
  avg_score = df["score"].mean()
  avg_comments = df["num_comments"].mean()
  print(f"Average score   : {avg_score:,.0f}")
  print(f"Average comments: {avg_comments:,.0f}")
  print()

  # ---------------------------------------------------------------------------
  # Task 2 — Basic Analysis with NumPy
  # ---------------------------------------------------------------------------
  print("--- NumPy Stats ---")

  # Convert score column to a NumPy array for mathematical operations
  scores_arr = df["score"].to_numpy()

  mean_score = np.mean(scores_arr)
  median_score = np.median(scores_arr)
  std_score = np.std(scores_arr)
  max_score = np.max(scores_arr)
  min_score = np.min(scores_arr)

  print(f"Mean score   : {mean_score:,.0f}")
  print(f"Median score : {median_score:,.0f}")
  print(f"Std deviation: {std_score:,.0f}")
  print(f"Max score    : {max_score:,}")
  print(f"Min score    : {min_score:,}")

  # Identify category with the most stories
  top_category = df["category"].value_counts().idxmax()
  top_category_count = df["category"].value_counts().max()
  print(f"Most stories in: {top_category} ({top_category_count} stories)")

  # Identify the story with the highest comment count
  max_comment_idx = df["num_comments"].idxmax()
  top_comment_title = df.loc[max_comment_idx, "title"]
  top_comment_count = df.loc[max_comment_idx, "num_comments"]
  print(
      f'Most commented story: "{top_comment_title}" —'
      f" {top_comment_count:,} comments"
  )
  print()

  # ---------------------------------------------------------------------------
  # Task 3 — Add New Columns
  # ---------------------------------------------------------------------------
  # 1. Engagement ratio: comments divided by score + 1 (prevents division by zero)
  df["engagement"] = df["num_comments"] / (df["score"] + 1)

  # 2. Popularity flag: True if score exceeds the dataset mean score, else False
  df["is_popular"] = df["score"] > mean_score

  # ---------------------------------------------------------------------------
  # Task 4 — Save the Result
  # ---------------------------------------------------------------------------
  os.makedirs("data", exist_ok=True)
  output_path = "data/trends_analysed.csv"

  # Save updated DataFrame to CSV
  df.to_csv(output_path, index=False)
  print(f"Saved to {output_path}")


if __name__ == "__main__":
  analyze_trends()
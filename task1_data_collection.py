import datetime
import json
import os


def generate_raw_trend_data():
  """Generates raw JSON trend data with sample imperfections

  (duplicates, nulls, unformatted text) and saves it to the data/ folder.
  """
  # Ensure the data directory exists
  os.makedirs("data", exist_ok=True)

  # Use a standardized date format for the filename
  date_str = datetime.datetime.now().strftime("%Y%m%d")
  filename = f"data/trends_{date_str}.json"

  # Raw dataset containing messy elements to be cleaned in Task 2
  raw_stories = [
      {
          "post_id": "t1",
          "title": "  AI Breakthrough in Healthcare  ",
          "score": "45",
          "num_comments": "120",
          "category": "technology",
      },
      {
          "post_id": "t2",
          "title": "Global Climate Summit Reaches Agreement",
          "score": "88",
          "num_comments": "340",
          "category": "worldnews",
      },
      {
          "post_id": "t1",
          "title": "  AI Breakthrough in Healthcare  ",
          "score": "45",
          "num_comments": "120",
          "category": "technology",
      },  # Duplicate
      {
          "post_id": "t3",
          "title": None,
          "score": "12",
          "num_comments": "5",
          "category": "sports",
      },  # Missing title
      {
          "post_id": None,
          "title": "New Space Telescope Discovers Galaxy",
          "score": "150",
          "num_comments": "512",
          "category": "science",
      },  # Missing post_id
      {
          "post_id": "t4",
          "title": "Blockbuster Movie Breaks Box Office Records",
          "score": "3",
          "num_comments": "15",
          "category": "entertainment",
      },  # Low score (< 5)
      {
          "post_id": "t5",
          "title": "Quantum Computing Milestone Achieved",
          "score": "92",
          "num_comments": "210",
          "category": "technology",
      },
      {
          "post_id": "t6",
          "title": "International Trade Agreement Signed",
          "score": "65",
          "num_comments": "88",
          "category": "worldnews",
      },
      {
          "post_id": "t7",
          "title": "Championship League Final Thriller",
          "score": "78",
          "num_comments": "410",
          "category": "sports",
      },
      {
          "post_id": "t8",
          "title": "Deep Sea Exploration Unlocks New Species",
          "score": "110",
          "num_comments": "95",
          "category": "science",
      },
      {
          "post_id": "t9",
          "title": "Award Season Kicks Off with Surprises",
          "score": "42",
          "num_comments": "60",
          "category": "entertainment",
      },
  ]

  # Write data to JSON file
  with open(filename, "w", encoding="utf-8") as f:
    json.dump(raw_stories, f, indent=4)

  print(f"Successfully generated raw JSON file at: {filename}")


if __name__ == "__main__":
  generate_raw_trend_data()
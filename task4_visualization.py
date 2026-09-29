import os
import matplotlib.pyplot as plt
import pandas as pd


def generate_visualizations():
  """Loads the analyzed trend data, creates individual visualizations

  (top stories, category counts, and scatter plot), and combines them
  into a comprehensive dashboard image.
  """
  # ---------------------------------------------------------------------------
  # Task 1 — Setup
  # ---------------------------------------------------------------------------
  csv_path = 'data/trends_analysed.csv'

  if not os.path.exists(csv_path):
    raise FileNotFoundError(
        f'Error: Analysed dataset not found at {csv_path}. Please run Task 3'
        ' first.'
    )

  # Load the analyzed CSV into a Pandas DataFrame
  df = pd.read_csv(csv_path)

  # Create the outputs directory if it does not already exist
  os.makedirs('outputs', exist_ok=True)

  # ---------------------------------------------------------------------------
  # Task 2 — Chart 1: Top 10 Stories by Score (Horizontal Bar Chart)
  # ---------------------------------------------------------------------------
  # Get top 10 stories by score and sort for proper bar chart display order
  top_10 = df.nlargest(10, 'score').sort_values('score', ascending=True)

  # Shorten titles longer than 50 characters to keep axis readable
  short_titles = [
      title[:47] + '...' if len(str(title)) > 50 else str(title)
      for title in top_10['title']
  ]

  fig, ax = plt.subplots(figsize=(10, 6))
  ax.barh(short_titles, top_10['score'], color='skyblue', edgecolor='navy')
  ax.set_title(
      'Top 10 Trending Stories by Score', fontsize=14, fontweight='bold'
  )
  ax.set_xlabel('Score', fontsize=12)
  ax.set_ylabel('Story Title', fontsize=12)
  plt.tight_layout()

  # Save chart before closing
  chart1_path = 'outputs/chart1_top_stories.png'
  plt.savefig(chart1_path, dpi=300)
  plt.close()
  print(f'Saved Chart 1 to {chart1_path}')

  # ---------------------------------------------------------------------------
  # Task 3 — Chart 2: Stories per Category (Bar Chart)
  # ---------------------------------------------------------------------------
  category_counts = df['category'].value_counts()

  fig, ax = plt.subplots(figsize=(8, 6))
  # Generate distinct colors for each category bar using a colormap
  bar_colors = plt.cm.tab10(range(len(category_counts)))

  ax.bar(
      category_counts.index,
      category_counts.values,
      color=bar_colors,
      edgecolor='black',
  )
  ax.set_title('Number of Stories per Category', fontsize=14, fontweight='bold')
  ax.set_xlabel('Category', fontsize=12)
  ax.set_ylabel('Story Count', fontsize=12)
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()

  chart2_path = 'outputs/chart2_categories.png'
  plt.savefig(chart2_path, dpi=300)
  plt.close()
  print(f'Saved Chart 2 to {chart2_path}')

  # ---------------------------------------------------------------------------
  # Task 4 — Chart 3: Score vs Comments (Scatter Plot)
  # ---------------------------------------------------------------------------
  fig, ax = plt.subplots(figsize=(8, 6))

  # Split data by popularity status for distinct coloring
  popular_stories = df[df['is_popular'] == True]
  non_popular_stories = df[df['is_popular'] == False]

  ax.scatter(
      non_popular_stories['score'],
      non_popular_stories['num_comments'],
      color='gray',
      alpha=0.7,
      label='Non-Popular',
      edgecolors='none',
  )
  ax.scatter(
      popular_stories['score'],
      popular_stories['num_comments'],
      color='crimson',
      alpha=0.8,
      label='Popular',
      edgecolors='black',
  )

  ax.set_title('Score vs. Comments Breakdown', fontsize=14, fontweight='bold')
  ax.set_xlabel('Score', fontsize=12)
  ax.set_ylabel('Number of Comments', fontsize=12)
  ax.legend(loc='upper left')
  plt.tight_layout()

  chart3_path = 'outputs/chart3_scatter.png'
  plt.savefig(chart3_path, dpi=300)
  plt.close()
  print(f'Saved Chart 3 to {chart3_path}')

  # ---------------------------------------------------------------------------
  # Bonus — Combined Dashboard Figure
  # ---------------------------------------------------------------------------
  fig = plt.figure(figsize=(18, 6))
  fig.suptitle('TrendPulse Dashboard', fontsize=18, fontweight='bold')

  # Subplot 1: Top 10 Stories
  ax1 = fig.add_subplot(1, 3, 1)
  ax1.barh(short_titles, top_10['score'], color='skyblue', edgecolor='navy')
  ax1.set_title('Top 10 Stories', fontsize=12)
  ax1.set_xlabel('Score')

  # Subplot 2: Categories
  ax2 = fig.add_subplot(1, 3, 2)
  ax2.bar(
      category_counts.index,
      category_counts.values,
      color=bar_colors,
      edgecolor='black',
  )
  ax2.set_title('Categories', fontsize=12)
  ax2.set_xlabel('Category')
  ax2.set_ylabel('Count')
  ax2.tick_params(axis='x', rotation=45)

  # Subplot 3: Scatter Plot
  ax3 = fig.add_subplot(1, 3, 3)
  ax3.scatter(
      non_popular_stories['score'],
      non_popular_stories['num_comments'],
      color='gray',
      alpha=0.7,
      label='Non-Popular',
  )
  ax3.scatter(
      popular_stories['score'],
      popular_stories['num_comments'],
      color='crimson',
      alpha=0.8,
      label='Popular',
  )
  ax3.set_title('Score vs Comments', fontsize=12)
  ax3.set_xlabel('Score')
  ax3.set_ylabel('Comments')
  ax3.legend(loc='upper left', fontsize='small')

  plt.tight_layout(rect=[0, 0.03, 1, 0.95])
  dashboard_path = 'outputs/dashboard.png'
  plt.savefig(dashboard_path, dpi=300)
  plt.close()
  print(f'Saved Dashboard to {dashboard_path}')


if __name__ == '__main__':
  generate_visualizations()
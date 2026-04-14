import pandas as pd
import matplotlib.pyplot as plt

# Load CSV from same folder
df = pd.read_csv("Task3_DataVisualization/quotes.csv")

# Count quotes per author
author_counts = df["Author"].value_counts().head(10)

# Plot bar chart
plt.figure()
author_counts.plot(kind="bar")

plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Author")
plt.ylabel("Number of Quotes")

# Save image
plt.savefig("author_chart.png")

# Show chart
plt.show()
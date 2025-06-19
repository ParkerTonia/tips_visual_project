# Start
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset into a DataFrame df
df = pd.read_csv('tips.csv')

# Create a bar chart for the 'day' column
df['day'].value_counts().plot(kind='bar', color='skyblue')
plt.xlabel('Day')
plt.ylabel('Frequency')
plt.title('Bar Chart of Days')
plt.show()

# Create a scatter plot to show relationships between 'total_bill' and 'tip'
plt.scatter(df['total_bill'], df['tip'], color='green')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot of Total Bill vs Tip')

# Add annotations for each data point
for i, txt in enumerate(df['day']):
    plt.annotate(txt, (df['total_bill'][i], df['tip'][i]))

# Display the scatter plot
plt.show()
# End

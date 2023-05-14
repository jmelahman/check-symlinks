#!/usr/bin/env python3
import matplotlib.pyplot as plt

text_color = 'white'
# text_color = 'black'

# Data
categories = ['fd test', 'check-symlinks', 'check_symlinks.py', 'while test', 'find test']
values1 = [0.334, 0.371, 1.008, 1.461, 1.492]
values2 = [0.048, 0.02, 0.62, 0.002, 0.026]

# Plotting
fig, ax = plt.subplots(figsize=(8, 5))

# Create horizontal bar chart
bar_width = 0.4
bar_space = 0.0
index = range(len(categories))

bars1 = ax.barh(index, values1, bar_width, color='blue', alpha=0.7, label='50,000 files, 1,000 symlinks')
bars2 = ax.barh([i + bar_width + bar_space for i in index], values2, bar_width, color='green', alpha=0.7,
                label='20 files, 10 symlinks')

# Set the y-axis labels
ax.set_yticks(index)
ax.set_yticklabels(categories, fontsize=10, color=text_color)
ax.tick_params(axis='x', colors=text_color)

# Set the x-axis label
ax.set_xlabel('Time (seconds)', fontsize=12, color=text_color)

# Set the title
ax.set_title('Execution Time Comparison', fontsize=14, color=text_color)

# Add a legend
ax.legend(loc='lower right', fontsize=10)

# Remove spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(text_color)
ax.spines['bottom'].set_color(text_color)

# Invert the y-axis to show the categories in descending order
ax.invert_yaxis()

# Add data labels
def autolabel(bars):
    for bar in bars:
        width = bar.get_width()
        ax.text(width + 0.01, bar.get_y() + bar.get_height() / 2, f'{width:.3f}', ha='left', va='center', color=text_color)

autolabel(bars1)
autolabel(bars2)

# Adjust layout
plt.tight_layout()

# Save the figure as SVG
plt.savefig('horizontal_bar_chart.svg', format='svg', transparent=True)

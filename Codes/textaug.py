# Create a colorful, publication-quality pipeline diagram using matplotlib with RGB colors.
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Helper to draw a rounded colored box with centered text
def draw_colored_box(ax, xy, width, height, text, facecolor, edgecolor='black', fontsize=10):
    x, y = xy
    box = FancyBboxPatch((x, y), width, height,
                         boxstyle="round,pad=0.02,rounding_size=0.05",
                         linewidth=1.5, facecolor=facecolor, edgecolor=edgecolor)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center', fontsize=fontsize, fontweight='bold', color='black')

# Helper to draw an arrow between boxes
def draw_arrow(ax, start_xy, end_xy, color='black'):
    arrow = FancyArrowPatch(start_xy, end_xy, arrowstyle='->', mutation_scale=15, linewidth=1.5, color=color)
    ax.add_patch(arrow)

# Figure setup
fig, ax = plt.subplots(figsize=(9, 12))
ax.set_facecolor((0.98, 0.98, 0.98))  # Light gray background

# Layout parameters
w, h = 7, 1.2  # width and height of boxes
x = 0.5        # x position for centered column
gap = 0.7      # vertical gap between boxes

# Titles and labels
title = "Proposed Predictive Maintenance Pipeline"
steps = [
    "Data Acquisition\n(Sensor Data Collection)",
    "Dataset Preparation\n(Data Validation & Splitting)",
    "Data Processing\n(Standardization & Cleaning)",
    "Class Balancing\n(SMOTE Oversampling)",
    "Model Training\n(Random Forest & Naive Bayes)",
    "Hyperparameter Optimization\n(GridSearchCV for RF)",
    "Model Evaluation\n(Accuracy, Precision, Recall, F1, ROC-AUC)",
    "Final ClassificationDecision\n(Maintenance Needed or Not)"
]

# Assign RGB colors for each category
colors = [
    (0.8, 0.93, 1.0),   # Light blue
    (0.8, 1.0, 0.8),    # Light green
    (1.0, 0.95, 0.8),   # Light orange
    (1.0, 0.85, 0.85),  # Light pink
    (0.85, 1.0, 1.0),   # Light cyan
    (0.93, 0.85, 1.0),  # Light purple
    (1.0, 0.9, 0.7),    # Peach
    (0.95, 1.0, 0.85)   # Light lime
]

# Compute y positions
y_top = len(steps) * (h + gap)
ys = [y_top - (i+1)*(h + gap) for i in range(len(steps))]

# Draw title
ax.text(x + w/2, y_top + 1, title, ha='center', va='bottom', fontsize=16, fontweight='bold', color='black')

# Draw boxes with colors
centers = []
for i, (label, y) in enumerate(zip(steps, ys)):
    draw_colored_box(ax, (x, y), w, h, label, facecolor=colors[i])
    centers.append((x + w/2, y + h/2))

# Draw arrows
for i in range(len(centers)-1):
    start = (centers[i][0], centers[i][1] - h/2)
    end = (centers[i+1][0], centers[i+1][1] + h/2)
    draw_arrow(ax, start, end, color='gray')

# Final plot settings
ax.set_xlim(0, 9)
ax.set_ylim(-0.5, y_top + 2)
ax.axis('off')
plt.show()

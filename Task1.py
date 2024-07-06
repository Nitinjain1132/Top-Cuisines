import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Determine the top three most common cuisines
top_cuisines = data['Cuisines'].str.split(', ').explode().value_counts().head(3)

# Calculate the percentage of restaurants that serve each of the top cuisines
total_restaurants = len(data)
cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Create the main window
root = tk.Tk()
root.title("Top 3 Cuisines")

# Create a frame for the top cuisines
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create labels for the top cuisines and their percentages
for i, (cuisine, count) in enumerate(top_cuisines.items()):
    ttk.Label(frame, text=f"{cuisine}: {count} restaurants ({cuisine_percentages[cuisine]:.2f}%)").grid(row=i, column=0, sticky=tk.W)

# Add padding around all components
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Create a figure for the graph
fig, ax = plt.subplots()

# Plot the top cuisines and their percentages
ax.bar(top_cuisines.index, cuisine_percentages)
ax.set_xlabel('Cuisines')
ax.set_ylabel('Percentage of Restaurants')
ax.set_title('Top 3 Cuisines and Their Percentages')

# Embed the plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)

# Start the main event loop
root.mainloop()

import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

def main():
    csv_file = "problem_lengths.csv"
    if not os.path.exists(csv_file):
        # Fallback if running from scripts dir
        if os.path.exists("../problem_lengths.csv"):
            csv_file = "../problem_lengths.csv"
        else:
            print("problem_lengths.csv not found.")
            return

    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Define colors
    colors = {
        'LV.AMO': 'darkred',
        'LV.NOL': 'darkgreen',
        'LV.VOL': 'blue'
    }

    # Order of olympiads for consistency
    olympiad_order = ['LV.AMO', 'LV.NOL', 'LV.VOL']
    
    # 1. Histogram of problem_solution_ch
    plt.figure(figsize=(10, 6))
    
    # Create bins of size 100
    max_val = df['problem_solution_ch'].max()
    bins = range(0, int(max_val) + 200, 100)
    
    # Prepare data for stacked histogram
    data = []
    labels = []
    plot_colors = []
    
    for olympiad in olympiad_order:
        subset = df[df['olympiad'] == olympiad]['problem_solution_ch']
        data.append(subset)
        labels.append(olympiad)
        plot_colors.append(colors.get(olympiad, 'black'))

    plt.hist(data, bins=bins, stacked=True, label=labels, color=plot_colors, edgecolor='black', alpha=0.7)
    
    plt.title('Distribution of Solution Lengths')
    plt.xlabel('Character Count')
    plt.ylabel('Number of Problems')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    
    plt.savefig('solution_length_histogram.png')
    plt.close()
    print("Saved solution_length_histogram.png")

    # 2. Average solution length vs Grade
    plt.figure(figsize=(10, 6))
    
    for olympiad in olympiad_order:
        subset = df[df['olympiad'] == olympiad]
        if subset.empty:
            continue
        # Group by grade and calculate mean
        # Ensure grade is numeric
        subset['grade'] = pd.to_numeric(subset['grade'], errors='coerce')
        avg_by_grade = subset.groupby('grade')['problem_solution_ch'].mean().sort_index()
        
        plt.plot(avg_by_grade.index, avg_by_grade.values, marker='o', label=olympiad, color=colors.get(olympiad, 'black'))

    plt.title('Average Solution Length by Grade')
    plt.xlabel('Grade')
    plt.ylabel('Average Solution Length (chars)')
    plt.legend()
    plt.grid(True)
    plt.xticks(range(5, 13)) # Grades are usually 5-12
    
    plt.savefig('avg_solution_by_grade.png')
    plt.close()
    print("Saved avg_solution_by_grade.png")

    # 3. Average solution length vs Year
    plt.figure(figsize=(10, 6))
    
    for olympiad in olympiad_order:
        subset = df[df['olympiad'] == olympiad]
        if subset.empty:
            continue
        # Group by year and calculate mean
        # Ensure year is numeric
        subset['year'] = pd.to_numeric(subset['year'], errors='coerce')
        avg_by_year = subset.groupby('year')['problem_solution_ch'].mean().sort_index()
        
        plt.plot(avg_by_year.index, avg_by_year.values, marker='o', label=olympiad, color=colors.get(olympiad, 'black'))

    plt.title('Average Solution Length by Year')
    plt.xlabel('Year')
    plt.ylabel('Average Solution Length (chars)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('avg_solution_by_year.png')
    plt.close()
    print("Saved avg_solution_by_year.png")

if __name__ == "__main__":
    main()

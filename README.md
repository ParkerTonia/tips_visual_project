# Global Health Indicators Visualization

## Project Overview
This project creates clear, informative visualizations of a sample `global_health_indicators.csv` dataset for the year 2020. The goal is to show key health and economic metrics—Life Expectancy, GDP per Capita, Healthcare Expenditure, and Access to Clean Water—across eight countries.

## Skills Demonstrated
- Loading and inspecting data with Pandas  
- Building bar charts and scatter plots using Matplotlib or Seaborn  
- Customizing plot appearance: axis labels, titles, colors, and annotations  
- Exporting figures for reports and presentations  
- Interpreting visual patterns to tell a data-driven story  

## Dataset
The dataset contains the following columns:

| Column                  | Description                                           |
|-------------------------|-------------------------------------------------------|
| Country                 | Country name                                          |
| Year                    | Calendar year (all entries are 2020)                  |
| Life Expectancy         | Average life expectancy at birth (in years)           |
| GDP per Capita          | Gross domestic product per person (USD)               |
| Healthcare Expenditure  | Annual health spending per person (USD)               |
| Access to Clean Water   | Percentage of population with clean water access (%)  |

Place your `global_health_indicators.csv` file in a `data/` folder at the root of this repository.

## Repository Structure


- **data/**  
  Contains the raw CSV file.  
- **notebooks/health_viz.ipynb**  
  Jupyter notebook that loads the data, creates and customizes the charts.  
- **figures/**  
  Exported PNG images of each chart.  

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YourUsername/Data-Visualization-Project.git
cd Data-Visualization-Project

# 2. Install required libraries
pip install pandas matplotlib seaborn notebook

# 3. Prepare the data
mkdir data
# Copy global_health_indicators.csv into the data/ folder

# 4. Launch the notebook
jupyter notebook notebooks/health_viz.ipynb

# 5. In Jupyter, run all cells
#    Charts will display inline and be saved to the figures/ folder

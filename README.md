# SPZ Open Mini-Challenge
## Authors
- Sahan Hatemo
- Jelle Schutter 

## Installation

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage
Directly run the Jupyter Notebook in your editor or use the command line:
```bash
jupyter notebook spz.ipynb
```
If you don't need to run the notebook, you can also view the rendered version directly on GitHub at: [spz.ipynb](spz.ipynb)

## Description
This project analyzes influenza-like illness (ILI) data from Switzerland, focusing on time series decomposition and forecasting using various models. The notebook includes data loading, preprocessing, exploratory data analysis, seasonal decomposition, and model evaluation.

## Data Source
The ILI data is sourced from the Swiss Federal Office of Public Health (FOPH) and can be found at: [Infectious Diseases Dashboard (IDD)](https://www.idd.bag.admin.ch/)
# Air Quality Analysis

## Project Structure

```
📦 Data Wrangling
 ┣ 📂 dashboard
 ┃ ┣ 📜 cleaned_data.csv      # Processed data after cleaning
 ┃ ┗ 📜 dashboard.py         # Streamlit dashboard script
 ┣ 📂 data
 ┃ ┗ 📜 PRSA_Data_Gucheng_20130301-20170228.csv  # Raw dataset
 ┣ 📜 notebook.ipynb        # Jupyter Notebook for data analysis
 ┣ 📜 README.md             # Project documentation
 ┗ 📜 requirements.txt      # Dependencies list
```

## Installation

```bash
pip install -r requirements.txt
```

## Run Jupyter Notebook

```bash
jupyter notebook notebook.ipynb
```

## Run Streamlit Dashboard

```bash
streamlit run dashboard/dashboard.py
```

# 🚖 NYC Transportation Analytics

A Data Engineering Project that builds an end-to-end ETL pipeline for NYC Taxi trip data using Python and PostgreSQL. The project processes multiple taxi datasets, performs data cleaning and feature engineering, stores the transformed data in PostgreSQL, and presents interactive business insights through a Streamlit dashboard.

---

# 📌 Project Overview

The objective of this project is to design and implement a scalable data engineering pipeline capable of processing millions of NYC taxi trip records. The pipeline integrates Yellow Taxi, Green Taxi, and FHV (For-Hire Vehicle) datasets into a PostgreSQL database and provides analytical insights through SQL queries and an interactive dashboard.

---

# 🎯 Objectives

- Build an end-to-end ETL pipeline.
- Process multiple NYC transportation datasets.
- Perform data cleaning and validation.
- Engineer business-oriented features.
- Load transformed data into PostgreSQL.
- Perform analytical SQL queries.
- Visualize insights using Streamlit.

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Database | PostgreSQL |
| Data Processing | Pandas |
| SQL Engine | SQLAlchemy |
| Dashboard | Streamlit |
| Visualization | Plotly Express |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```text
transportation-analytics-capstone-project-group6/

│
├── config/
│   ├── __init__.py
│   └── config.py
│
├── dashboard/
│   ├── app.py
│   ├── utils.py
│   ├── assets/
│   └── pages/
│       ├── 1_Overview.py
│       ├── 2_Trip_Analysis.py
│       ├── 3_Revenue_Analysis.py
│       ├── 4_Location_Analysis.py
│       └── 5_Dataset_Comparison.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── logs/
│
├── sql/
│
├── src/
│   ├── analytics/
│   ├── database/
│   ├── etl/
│   ├── logger.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses NYC TLC Trip Record datasets.

Datasets included:

- Yellow Taxi
- Green Taxi
- FHV (For-Hire Vehicle)

Data processed:

| Dataset | Months |
|----------|---------|
| Yellow Taxi | January – May 2026 |
| Green Taxi | January – May 2026 |
| FHV | January – April 2026 |

---

# ⚙ ETL Pipeline

The ETL workflow consists of the following stages:

### 1. Extraction

- Read Parquet files
- Load datasets using Pandas

### 2. Standardization

- Rename columns
- Standardize schema across datasets

### 3. Data Cleaning

- Remove duplicate records
- Handle missing values
- Remove invalid trips
- Validate timestamps
- Remove invalid trip distances

### 4. Feature Engineering

Generated features include:

- Pickup Month
- Pickup Weekday
- Pickup Hour
- Weekend Indicator
- Rush Hour Indicator
- Trip Duration
- Average Speed
- Trip Category

### 5. Validation

Data quality checks include:

- Missing values
- Negative trip duration
- Invalid distance
- Invalid timestamps

### 6. Loading

The cleaned datasets are loaded into PostgreSQL tables using SQLAlchemy.

---

# 🗄 Database

Three PostgreSQL tables are created:

- yellow_trips
- green_trips
- fhv_trips

The database stores cleaned and feature-engineered records for analytical querying.

---

# 📈 Analytics Performed

The project performs several business analyses including:

## KPI Analysis

- Total Trips
- Total Revenue
- Average Fare
- Average Distance
- Average Trip Duration

## Trip Analysis

- Monthly Trips
- Trips by Hour
- Trips by Weekday
- Weekend vs Weekday Trips
- Rush Hour Analysis
- Passenger Count Distribution
- Trip Category Distribution

## Revenue Analysis

- Monthly Revenue
- Revenue by Hour
- Average Fare by Month
- Average Speed by Month

## Location Analysis

- Top Pickup Locations
- Top Dropoff Locations
- Top Revenue Generating Locations

## Dataset Comparison

- Yellow Taxi vs Green Taxi vs FHV
- Monthly comparison across datasets

---

# 📊 Dashboard

The project includes an interactive Streamlit dashboard with the following pages:

- 📊 Overview
- 🚖 Trip Analysis
- 💰 Revenue Analysis
- 📍 Location Analysis
- 🚕 Dataset Comparison

The dashboard allows users to visualize transportation trends and business insights using interactive Plotly charts.

---

# ▶ Running the Project

## 1. Clone the Repository

```bash
git clone <repository-url>
cd transportation-analytics-capstone-project-group6
```

---

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

### Windows

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure PostgreSQL

1. Copy the example configuration file:

```bash
cp config/config.example.py config/config.py
```

2. Update the PostgreSQL credentials inside `config/config.py`.

## 5. Run ETL Pipeline

```bash
python -m src.main
```

---

## 6. Run Analytics

```bash
python -m src.analytics.run_queries
```

---

## 7. Launch Dashboard

```bash
streamlit run dashboard/app.py
```

---

# 📷 Dashboard Screenshots

Dashboard screenshots will be added here.

- Overview
- Trip Analysis
- Revenue Analysis
- Location Analysis
- Dataset Comparison

---

# 🚀 Future Enhancements

- Interactive dashboard filters
- Taxi zone mapping
- Geospatial visualizations
- Docker containerization
- Apache Airflow orchestration
- Cloud deployment (AWS/GCP/Azure)
- Real-time data ingestion
- CI/CD pipeline integration

---

# 📚 Key Learnings

- ETL pipeline development
- Data cleaning and preprocessing
- Feature engineering
- PostgreSQL database design
- SQL analytics
- Dashboard development with Streamlit
- Data visualization using Plotly
- Git version control

---

# 📄 License

This project is developed for academic and educational purposes.

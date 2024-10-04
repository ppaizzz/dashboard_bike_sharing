# **Bike Sharing Data Dashboard**

This project is an interactive dashboard built using Streamlit to analyze the bike sharing dataset. The dashboard allows users to explore and visualize the data from two datasets:

- `day.csv`: Bike sharing data aggregated daily.
- `hour.csv`: Bike sharing data aggregated hourly.

## **Project Overview**

The dashboard provides insights into bike sharing trends, showing data based on weather conditions and time of day. It includes two datasets: one aggregated by day and one by hour, and visualizations such as bar charts and line charts for easy interpretation.

## **Features**

- **Data Display**: Choose between daily or hourly data and explore the datasets interactively.
- **Visualizations**:
  - Bar chart of bike rentals by weather conditions (daily data).
  - Line chart of bike rentals by hour (hourly data).
- **Sidebar Control**: Switch between datasets using a sidebar selector.

## **Getting Started**

To run this project locally, follow these steps:

### **Prerequisites**

You will need to have the following installed:
- Python 3.8 or above
- Streamlit
- Pandas
- Matplotlib
- Seaborn

### How to Run the Project

1. **Install the required libraries**:
   - Install the dependencies by running the following command:
     ```bash
     pip install -r requirements.txt
     ```

2. **Run the Streamlit App**:
   - Use the command below to start the app:
     ```bash
     streamlit run bike_sharing_dashboard.py
     ```

3. **Deploy on Streamlit Cloud**:
   - The dashboard is also deployed on Streamlit Cloud. You can access the deployed app

### Deployment
This project can be deployed to Streamlit Cloud. Follow these steps:
  -Upload the project (including app.py, day.csv, hour.csv, requirements.txt, and README.md) to a GitHub repository.
  - Log in to Streamlit Cloud.
  - Create a new app and link it to your GitHub repository.
  - Click "Deploy" to launch the app.
  - After deployment, the dashboard will be accessible via a public URL.
### Usage
  - Select the dataset (Harian or Per Jam) from the sidebar to switch between daily and hourly data.
  - Visualize bike rentals based on weather conditions or time of day.

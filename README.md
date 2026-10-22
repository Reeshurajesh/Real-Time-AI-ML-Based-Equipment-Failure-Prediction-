# Real-Time AI/ML-Based Equipment Failure Prediction

## 📌 Project Overview

The **Real-Time AI/ML-Based Equipment Failure Prediction System** is a Python-based application that monitors machine sensor readings and predicts potential equipment failure risks using a Random Forest machine learning model.

The application generates sensor readings, stores them in a MySQL database, processes the data using Pandas, and displays machine conditions and failure predictions through a Tkinter graphical user interface.

The system automatically updates machine readings every 5 seconds, providing a simple demonstration of real-time equipment monitoring and predictive maintenance.

## 🎯 Project Objectives

- Monitor machine sensor readings continuously.
- Store machine readings and failure indicators in MySQL.
- Apply a Random Forest Classifier to predict potential failure risks.
- Display sensor values and predictions through a graphical interface.
- Demonstrate the concept of real-time monitoring and predictive maintenance.

## 🛠️ Technologies Used

- **Python** – Application logic and data processing
- **MySQL** – Storage of machine readings
- **Pandas** – Data handling and preparation
- **Scikit-learn** – Random Forest machine learning model
- **Tkinter** – Graphical user interface (GUI)
- **Random** – Generation of simulated sensor readings
- **Datetime** – Recording the reading date and time

## ✨ Key Features

- **Real-Time Sensor Simulation:** Generates machine readings automatically.
- **MySQL Integration:** Stores sensor readings and failure indicators in the database.
- **Machine Learning Prediction:** Uses a Random Forest Classifier to predict machine failure risk.
- **Automatic Updates:** Refreshes the machine readings every 5 seconds.
- **Live GUI Display:** Shows temperature, vibration, pressure, power consumption, and RPM.
- **Failure Risk Status:** Displays the predicted status as FAILURE RISK or NORMAL.
- **Timestamp Recording:** Stores the date and time of each reading.

## ⚙️ Sensor Parameters

The application generates simulated sensor values for machine ID `M001`.

| Parameter | Generated Value |
|---|---|
| Machine ID | M001 |
| Temperature | 60–95 °C |
| Vibration | 2–10 |
| Pressure | 50–80 |
| Power Consumption | 4–10 |
| RPM | 1350–1550 |
| Update Interval | Every 5 seconds |

**Note:** The sensor readings are randomly generated for project demonstration. The displayed values can change automatically every 5 seconds, so the temperature, vibration, pressure, power consumption, RPM, and prediction status may differ each time the application updates.

## 🔍 Failure Detection Logic

The program initially assigns a failure indicator using the following conditions:

- Temperature greater than 85 °C
- Vibration greater than 8
- Power consumption greater than 9

If any one of these conditions is met, the failure indicator is set to `1`; otherwise, it is set to `0`.

The Random Forest Classifier uses the available historical sensor readings and their failure indicators to generate predictions.

**Important:** This is an educational demonstration using simulated data and predefined failure rules. Its predictions are not validated for real industrial equipment.

## 🗄️ Database Details

**Database Name:** `machine_failure_db`

**Table Name:** `machine_readings`

The application expects the table to contain the following columns:

- `reading_id`
- `machine_id`
- `temperature`
- `vibration`
- `pressure`
- `power_consumption`
- `rpm`
- `reading_time`
- `failure`

The table must be created in MySQL before running the application.

## 📦 Installation and Setup

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Install Required Libraries

Open Command Prompt or the terminal and run:

```bash
pip install mysql-connector-python pandas scikit-learn
```

Tkinter is included with most standard Windows Python installations.

### 3. Configure MySQL

- Start the MySQL server.
- Create the `machine_failure_db` database.
- Create the `machine_readings` table with the required columns.

### 4. Configure Database Credentials

Update the MySQL connection settings in the Python program with your own username and password.

**Security Note:** Never upload real database passwords to a public GitHub repository. Use placeholders or environment variables to protect sensitive credentials.

### 5. Run the Application

Save the Python program as `machine_failure_prediction.py` or use your chosen Python filename.

Run the following command from the project folder:

```bash
python machine_failure_prediction.py
```

### 6. Observe Machine Readings

- The application starts monitoring simulated sensor readings.
- Sensor values update automatically every 5 seconds.
- The readings and failure indicators are stored in MySQL.
- The Random Forest model displays a prediction when sufficient historical data containing both classes is available.

## 💻 Source Code

**GitHub Python Source Code:**

[View Project Source Code](PASTE_YOUR_GITHUB_SOURCE_CODE_LINK_HERE)


## 🚀 Future Enhancements

- Integrate real IoT sensors for live machine readings.
- Improve prediction accuracy using a larger, validated dataset.
- Add graphical charts to visualize sensor trends.
- Introduce automated alerts for high-risk machine conditions.
- Create a historical failure analysis report.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and GUI development
- MySQL database connectivity and data storage
- Data processing using Pandas
- Machine learning with Random Forest
- Sensor data simulation and periodic updates
- Basic failure detection and predictive maintenance concepts

## 👩‍💻 Author

**Reeshma Devi R**

Data Analytics Learner | Python | SQL | Pandas | Machine Learning

---

*This project was developed for learning and demonstration purposes.*

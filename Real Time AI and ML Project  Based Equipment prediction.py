import tkinter as tk
import mysql.connector
import random
import pandas as pd

from datetime import datetime
from sklearn.ensemble import RandomForestClassifier



db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_MYSQL_Password",
    database = "machine_failure_db"
)

cursor = db.cursor()

window = tk.Tk()

window.title("Machine Failure Prediction SSystem")
window.geometry("600x700")

title = tk.Label(
    window,
    text = "MACHINE FAILURE PREDICTION SYSTEM",
    font = ("Arial",18,"bold")
)

title.pack(pady=20)

machine_label = tk.Label(
    window,
    text = "Machine ID: M001",
    font = ("Arial",13)
)

machine_label.pack(pady=5)

temperature_label = tk.Label(
    window,
    text  = "Temperature:--",
    font = ("Arial",13)
)

temperature_label.pack(pady=5)

vibration_label = tk.Label(
    window,
    text = "Vibration:--",
    font = ("Ariak",13)
)

vibration_label.pack(pady=5)

pressure_label = tk.Label(
    window,
    text = "pressure:--",
    font = ("Arial",13)
)

pressure_label.pack(pady=5)


power_label = tk.Label(
    window,
    text = "Power consumption:--",
    font = ("Arial",13)
)

power_label.pack(pady=5)


rpm_label = tk.Label(
    window,
    text = "RPM:--",
    font = ("Arial", 13)
)

rpm_label.pack(pady=5)

prediction_label = tk.Label(
    window,
    text = "Prediction: Waiting...",
    font = ("Arial",16,"bold")
)

prediction_label.pack(pady=25)


status_label = tk.Label(
    window,
    text = "System Starting...",
    font = ("Arial",12)
)

status_label.pack(pady=10)


def update_machine():

    machine_id = "M001"

    
    Temperature = round(random.uniform(60,95),2)
    vibration = round(random.uniform(2,10),2)
    pressure = round(random.uniform(50,80),2)
    power_consumption = round(random.uniform(4,10),2)
    rpm = random.randint(1350,1550)

    
    reading_time = datetime.now()


    if Temperature > 85 or vibration > 8 or power_consumption > 9:
        failure = 1
    else:
        failure = 0


    sql = '''
    insert into machine_readings
    (machine_id, Temperature,vibration,pressure,
     power_consumption,rpm,reading_time,failure)
     values(%s, %s, %s, %s, %s, %s, %s,%s)
    '''


    values = (
        machine_id,
        Temperature,
        vibration,
        pressure,
        power_consumption,
        rpm,
        reading_time,
        failure
    )

    cursor.execute(sql,values)

    db.commit()

    cursor.execute(
        "Select * from  Machine_readings"
    )

    rows = cursor.fetchall()

    columns = [
        "reading_id",
        "machine_id",
        "temperature",
        "vibration",
        "pressure",
        "power_consumption",
        "rpm",
        "reading_time",
        "failure"
    ]

    df = pd.DataFrame(
        rows,
        columns = columns
    )


    x = df[
        [
            "temperature",
            "vibration",
            "pressure",
            "power_consumption",
            "rpm"
        ]
    ]

    y = df["failure"]

    if len(y.unique()) >=2:

        model = RandomForestClassifier(
            n_estimators = 100,
            random_state = 42
        )

        model.fit(x,y)


        latest = df.tail(1)

        new_data = latest[
            [
                "temperature",
                "vibration",
                "pressure",
                "power_consumption",
                "rpm"
            ]
        ]

        prediction = model.predict(new_data)

        if prediction[0] ==1:

            prediction_label.config(
                text = "prediction: FAILURE RISK"
            )

        else:
            prediction_label.config(
                text = "prediction: NORMAL"
            )

    else:
        prediction_label.config(
            text = "prediction: Collecting Dat..."
        )


    temperature_label.config(
        text = f"Temperature:e{Temperature}"
    )

    vibration_label.config(
        text = f"vibration:{pressure}"
    )

    pressure_label.config(
        text = f"pressure:{pressure}"
    )

    power_label.config(
        text = f"power consumption:{power_consumption}"
    )

    rpm_label.config(
        text = f"RPM:{rpm}"
    )

    status_label.config(
        text = "Real-Time Data Updated"
    )


    window.after(
        5000,
        update_machine
    )
update_machine()

window.mainloop()

db.close()
        
        

    

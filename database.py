import sqlite3

conn = sqlite3.connect("asthma.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS patient_history(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    age INTEGER,
    bmi REAL,
    smoking INTEGER,
    allergies INTEGER,
    prediction TEXT,
    probability REAL,
    medical_risk REAL,
    environment_risk REAL,
    final_risk REAL
)
""")

conn.commit()


def save_prediction(age,bmi,smoking,allergies,prediction,
                    probability,medical_risk,
                    environment_risk,final_risk):

    cursor.execute("""
    INSERT INTO patient_history(
    age,bmi,smoking,allergies,
    prediction,probability,
    medical_risk,environment_risk,
    final_risk)

    VALUES(?,?,?,?,?,?,?,?,?)
    """,
    (
        age,
        bmi,
        smoking,
        allergies,
        prediction,
        probability,
        medical_risk,
        environment_risk,
        final_risk
    ))

    conn.commit()


def load_history():

    cursor.execute("SELECT * FROM patient_history")

    return cursor.fetchall()
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

st.title("🎓 Student Placement Predictor")

st.write("Enter student details:")

IQ = st.number_input("IQ Score", 50, 200)
CGPA = st.number_input("CGPA", 0.0, 10.0)
Prev_Sem_Result = st.number_input("Previous Semester Result", 0.0, 100.0)
Academic_Performance = st.number_input("Academic Performance Score", 0.0, 100.0)
Internship_Experience = st.selectbox("Internship Experience", ["No", "Yes"])
Extra_Curricular_Score = st.number_input("Extra Curricular Score", 0.0, 100.0)
Communication_Skills = st.number_input("Communication Skills", 0.0, 100.0)
Projects_Completed = st.number_input("Projects Completed", 0, 20)

Internship_Experience = 1 if Internship_Experience == "Yes" else 0

if st.button("Predict Placement"):
    features = np.array([[IQ, CGPA, Prev_Sem_Result, Academic_Performance,
                          Internship_Experience, Extra_Curricular_Score,
                          Communication_Skills, Projects_Completed]])
    
    prediction = model.predict(features)[0]

    if prediction == 1:
        st.success("✅ Student is likely to be PLACED")
    else:
        st.error("❌ Student is NOT likely to be placed")

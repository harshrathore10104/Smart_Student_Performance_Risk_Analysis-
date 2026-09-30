import streamlit as st
import pandas as pd
import plotly.express as px

from database.database import init_db, add_student, get_students, delete_student
from modules.performance_analyzer import calculate_metrics, subject_summary
from modules.risk_predictor import train_and_save_model, predict_risk
from modules.report_generator import generate_student_report

st.set_page_config(page_title="Student Performance & Risk Analysis", page_icon="🎓", layout="wide")
init_db()

st.title("🎓 Smart Student Performance & Risk Analysis System")
st.caption("A Python + SQLite + Machine Learning academic analytics project")

with st.sidebar:
    st.header("Navigation")
    page = st.radio("Select module", [
        "Dashboard", "Student Management", "Performance Analytics",
        "Risk Prediction", "Report Generation"
    ])

# Dashboard
if page == "Dashboard":
    st.header("System Dashboard")
    df = get_students()
    if df.empty:
        st.info("No students yet. Add students from Student Management.")
    else:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Students", len(df))
        c2.metric("Average Marks", f"{df['average_marks'].mean():.2f}")
        c3.metric("Average Attendance", f"{df['attendance'].mean():.1f}%")
        c4.metric("At-Risk Students", int((df["average_marks"] < 50).sum()))

        fig = px.scatter(
            df, x="attendance", y="average_marks",
            color="department", hover_data=["name"],
            title="Attendance vs Average Marks"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Student Records")
        st.dataframe(df, use_container_width=True)

# Student Management
elif page == "Student Management":
    st.header("Student Management")
    with st.form("student_form"):
        name = st.text_input("Student Name")
        roll = st.text_input("Roll Number")
        department = st.selectbox("Department", ["CSE", "AIML", "ECE", "EEE", "ME", "Other"])
        attendance = st.number_input("Attendance (%)", 0.0, 100.0, 75.0)
        math = st.number_input("Mathematics", 0.0, 100.0, 70.0)
        dbms = st.number_input("DBMS", 0.0, 100.0, 70.0)
        python = st.number_input("Python", 0.0, 100.0, 70.0)
        ml = st.number_input("Machine Learning", 0.0, 100.0, 70.0)
        submitted = st.form_submit_button("Add Student")

        if submitted:
            if not name.strip() or not roll.strip():
                st.error("Name and roll number are required.")
            else:
                marks = [math, dbms, python, ml]
                avg = sum(marks) / len(marks)
                add_student(name.strip(), roll.strip(), department, attendance, *marks, avg)
                st.success("Student added successfully.")

    st.subheader("Existing Students")
    df = get_students()
    if df.empty:
        st.info("No records found.")
    else:
        st.dataframe(df, use_container_width=True)
        selected = st.selectbox("Select roll number to delete", df["roll_no"].tolist())
        if st.button("Delete Selected Student"):
            delete_student(selected)
            st.success("Student deleted. Refresh the page to update the table.")

# Analytics
elif page == "Performance Analytics":
    st.header("Performance Analytics")
    df = get_students()
    if df.empty:
        st.warning("Add students first.")
    else:
        metrics = calculate_metrics(df)
        a, b, c = st.columns(3)
        a.metric("Mean Score", f"{metrics['mean_marks']:.2f}")
        b.metric("Highest Score", f"{metrics['max_marks']:.2f}")
        c.metric("Lowest Score", f"{metrics['min_marks']:.2f}")

        summary = subject_summary(df)
        st.subheader("Subject-wise Average")
        st.dataframe(summary, use_container_width=True)

        fig = px.bar(summary, x="subject", y="average", title="Average Marks by Subject")
        st.plotly_chart(fig, use_container_width=True)

        fig2 = px.histogram(df, x="average_marks", nbins=10, title="Distribution of Average Marks")
        st.plotly_chart(fig2, use_container_width=True)

# Risk Prediction
elif page == "Risk Prediction":
    st.header("Academic Risk Prediction")
    st.write("The model classifies students into Low, Medium, or High academic risk using attendance and subject performance.")
    if st.button("Train / Refresh ML Model"):
        path, score = train_and_save_model()
        st.success(f"Model trained and saved. Validation accuracy: {score:.2%}")

    st.subheader("Predict Risk for a Student")
    attendance = st.slider("Attendance (%)", 0, 100, 75)
    math = st.slider("Mathematics", 0, 100, 70)
    dbms = st.slider("DBMS", 0, 100, 70)
    python = st.slider("Python", 0, 100, 70)
    ml = st.slider("Machine Learning", 0, 100, 70)

    if st.button("Predict Risk"):
        result = predict_risk([attendance, math, dbms, python, ml])
        st.success(f"Predicted Academic Risk: {result}")

# Reports
elif page == "Report Generation":
    st.header("Student Report Generation")
    df = get_students()
    if df.empty:
        st.info("Add students first.")
    else:
        roll = st.selectbox("Choose student", df["roll_no"].tolist())
        if st.button("Generate PDF Report"):
            student = df[df["roll_no"] == roll].iloc[0].to_dict()
            output = generate_student_report(student)
            st.success(f"Report generated: {output.name}")
            with open(output, "rb") as f:
                st.download_button("Download Report", f, file_name=output.name, mime="application/pdf")

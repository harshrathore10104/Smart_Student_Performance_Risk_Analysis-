from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

REPORT_DIR = Path(__file__).resolve().parent.parent / "reports"
REPORT_DIR.mkdir(exist_ok=True)

def generate_student_report(student):
    safe_roll = str(student["roll_no"]).replace("/", "_")
    path = REPORT_DIR / f"student_report_{safe_roll}.pdf"
    doc = SimpleDocTemplate(str(path), pagesize=A4)
    styles = getSampleStyleSheet()
    story = [
        Paragraph("Smart Student Performance & Risk Analysis System", styles["Title"]),
        Spacer(1, 15),
        Paragraph(f"Student: {student['name']}", styles["Heading2"]),
        Paragraph(f"Roll Number: {student['roll_no']}", styles["Normal"]),
        Paragraph(f"Department: {student['department']}", styles["Normal"]),
        Spacer(1, 12),
    ]
    data = [
        ["Metric", "Value"],
        ["Attendance", f"{student['attendance']:.2f}%"],
        ["Mathematics", f"{student['mathematics']:.2f}"],
        ["DBMS", f"{student['dbms']:.2f}"],
        ["Python", f"{student['python']:.2f}"],
        ["Machine Learning", f"{student['machine_learning']:.2f}"],
        ["Average Marks", f"{student['average_marks']:.2f}"],
    ]
    table = Table(data, colWidths=[220, 150])
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
        ("PADDING", (0,0), (-1,-1), 7),
    ]))
    story.append(table)
    story += [
        Spacer(1, 15),
        Paragraph(
            "This report is generated automatically from the academic records entered into the system.",
            styles["Normal"]
        )
    ]
    doc.build(story)
    return path

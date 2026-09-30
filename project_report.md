# Smart Student Performance & Risk Analysis System

## 1. Introduction
This project presents a Python-based academic analytics system that combines student record management, performance analysis, visualization, machine learning risk classification, and PDF reporting.

## 2. Problem Statement
Manual academic analysis requires repeated calculation of marks, attendance, and subject performance. The proposed system centralizes these operations and provides analytical outputs through an interactive dashboard.

## 3. Functional Requirements
- Student record management
- Performance analytics
- Attendance analysis
- Risk prediction
- Dashboard visualization
- PDF report generation

## 4. Non-Functional Requirements
- Usability: simple dashboard-based interaction
- Performance: lightweight local processing
- Reliability: validation and automated tests
- Maintainability: modular source structure
- Scalability: modular components allow future database/model replacement
- Error handling: invalid input is rejected before storage

## 5. System Architecture
The system uses a Streamlit presentation layer, modular application logic, SQLite persistence, Scikit-learn ML processing, and ReportLab report generation.

## 6. Design Diagrams
See `docs/` for architecture, workflow, use case, class/component, sequence, and ER diagrams.

## 7. Design Decisions
Python was selected for its data and ML ecosystem. SQLite provides self-contained persistence. Random Forest was selected for a simple, interpretable academic classification demonstration.

## 8. Implementation
The implementation is separated into database, analytics, prediction, reporting, validation, and testing modules.

## 9. Results
The dashboard displays student records, averages, subject-wise performance, attendance relationships, and risk predictions. Individual PDF reports can be generated from stored records.

## 10. Testing
Pytest tests cover validation, metric calculation, and ML prediction.

## 11. Challenges
Key implementation challenges include maintaining clean module boundaries, validating numeric inputs, integrating ML prediction into the dashboard, and generating downloadable PDF output.

## 12. Learnings
The project demonstrates database integration, modular Python development, data visualization, supervised machine learning, testing, and software documentation.

## 13. Future Enhancements
- Authentication and role-based access
- Historical semester tracking
- Real institutional dataset integration
- Explainable ML with feature importance
- Email-based reports
- Cloud deployment

## 14. References
- Python documentation
- Pandas documentation
- Scikit-learn documentation
- Streamlit documentation
- SQLite documentation
- ReportLab documentation

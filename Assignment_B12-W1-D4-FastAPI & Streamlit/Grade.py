import streamlit as st
import pandas as pd


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .student-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎓 Student Grade Manager</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Manage student marks, grades and performance easily</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# CREATE SESSION STORAGE
# --------------------------------------------------

if "students" not in st.session_state:
    st.session_state.students = []


# --------------------------------------------------
# FUNCTION TO CALCULATE GRADE
# --------------------------------------------------

def calculate_grade(mark):

    if mark >= 90:
        return "A+"

    elif mark >= 80:
        return "A"

    elif mark >= 70:
        return "B"

    elif mark >= 60:
        return "C"

    elif mark >= 50:
        return "D"

    else:
        return "F"


# --------------------------------------------------
# ADD STUDENT SECTION
# --------------------------------------------------

st.subheader("➕ Add Student")

col1, col2, col3 = st.columns(3)

with col1:

    student_name = st.text_input(
        "👤 Student Name",
        placeholder="Enter student name"
    )


with col2:

    marks = st.number_input(
        "📝 Marks",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )


with col3:

    st.write("")
    st.write("")

    add_student = st.button(
        "➕ Add Student",
        use_container_width=True
    )


# --------------------------------------------------
# ADD STUDENT LOGIC
# --------------------------------------------------

if add_student:

    if student_name.strip() == "":
        st.warning("⚠️ Please enter the student name.")

    else:

        grade = calculate_grade(marks)

        status = "Pass" if marks >= 50 else "Fail"

        student = {
            "Name": student_name,
            "Marks": marks,
            "Grade": grade,
            "Status": status
        }

        st.session_state.students.append(student)

        st.success(
            f"✅ {student_name} added successfully!"
        )


# --------------------------------------------------
# STUDENT DATA
# --------------------------------------------------

if st.session_state.students:

    st.divider()

    st.subheader("📊 Student Performance")


    # Convert list to DataFrame

    df = pd.DataFrame(
        st.session_state.students
    )


    # --------------------------------------------------
    # SUMMARY CARDS
    # --------------------------------------------------

    total_students = len(df)

    average_marks = df["Marks"].mean()

    highest_marks = df["Marks"].max()

    passed_students = len(
        df[df["Status"] == "Pass"]
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "👨‍🎓 Total Students",
            total_students
        )


    with col2:

        st.metric(
            "📈 Class Average",
            f"{average_marks:.1f}"
        )


    with col3:

        st.metric(
            "🏆 Highest Marks",
            highest_marks
        )


    with col4:

        st.metric(
            "✅ Passed",
            passed_students
        )


    st.write("")


    # --------------------------------------------------
    # DISPLAY TABLE
    # --------------------------------------------------

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------
    # TOP STUDENT
    # --------------------------------------------------

    top_student = df.loc[
        df["Marks"].idxmax()
    ]


    st.success(
        f"🏆 Top Student: **{top_student['Name']}** "
        f"with **{top_student['Marks']} marks** "
        f"({top_student['Grade']})"
    )


    # --------------------------------------------------
    # DELETE ALL STUDENTS
    # --------------------------------------------------

    st.divider()

    if st.button(
        "🗑️ Clear All Students",
        use_container_width=True
    ):

        st.session_state.students = []

        st.rerun()


else:

    st.info(
        "📚 No students added yet. "
        "Enter a student name and marks above to get started."
    )


# --------------------------------------------------
# GRADE SCALE
# --------------------------------------------------

st.divider()

st.subheader("📋 Grade Scale")

grade_data = {
    "Marks": [
        "90 - 100",
        "80 - 89",
        "70 - 79",
        "60 - 69",
        "50 - 59",
        "0 - 49"
    ],

    "Grade": [
        "A+",
        "A",
        "B",
        "C",
        "D",
        "F"
    ],

    "Result": [
        "Excellent",
        "Very Good",
        "Good",
        "Average",
        "Pass",
        "Fail"
    ]
}


grade_df = pd.DataFrame(grade_data)


st.dataframe(
    grade_df,
    use_container_width=True,
    hide_index=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.caption(
    "🎓 Student Grade Manager • Built with Python & Streamlit"
)
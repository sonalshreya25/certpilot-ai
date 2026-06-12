import streamlit as st
import pandas as pd
from src.orchestrator import run_certpilot_workflow

st.set_page_config(page_title="CertPilot AI", page_icon="🧠", layout="wide")

st.title("CertPilot AI")
st.caption("Multi-Agent Certification Readiness Coach — synthetic data demo")

with st.sidebar:
    st.header("Learner Input")
    role = st.selectbox("Role", ["Cloud Engineer", "DevOps Engineer", "Data Engineer", "AI Engineer","Business Analyst"])
    certification = st.selectbox("Certification", ["AZ-204", "AZ-400", "DP-203", "AI-102","PL-300"])
    employee_id = st.selectbox("Synthetic Employee ID", ["EMP-001", "EMP-002", "EMP-003", "EMP-004"])
    practice_score = st.slider("Average Practice Score", 0, 100, 67)
    hours_studied = st.slider("Hours Studied", 0, 40, 18)
    run_button = st.button("Run Multi-Agent Workflow")

if run_button:
    result = run_certpilot_workflow(role, certification, employee_id, practice_score, hours_studied)

    readiness = result["assessment"]["readiness"]
    st.subheader("Readiness Result")
    col1, col2 = st.columns(2)
    col1.metric("Readiness Score", readiness["score"])
    col2.metric("Status", readiness["status"])

    if readiness["reasons"]:
        st.warning(" | ".join(readiness["reasons"]))
    else:
        st.success("Learner appears ready based on synthetic readiness rules.")

    st.subheader("Agent Outputs")

    with st.expander("1. Learning Path Curator Agent", expanded=True):
        st.write(result["curator"]["summary"])
        st.write("**Recommended skills:**", ", ".join(result["curator"]["recommended_skills"]))
        st.write("**Grounding sources:**", ", ".join(result["curator"]["sources"]))

    with st.expander("2. Study Plan Generator Agent", expanded=True):
        for item in result["study_plan"]["study_plan"]:
            st.write(f"- {item}")

    with st.expander("3. Engagement Agent", expanded=True):
        st.write(result["engagement"]["work_context_summary"])
        st.write("**Recommended slot:**", result["engagement"]["recommended_slot"])
        st.write("**Reminder strategy:**", result["engagement"]["reminder_strategy"])

    with st.expander("4. Assessment Agent", expanded=True):
        st.write("**Practice questions:**")
        for q in result["assessment"]["practice_questions"]:
            st.write(f"- {q}")
        st.write("**Sources:**", ", ".join(result["assessment"]["sources"]))

    with st.expander("5. Manager Insights Agent", expanded=True):
        st.write(result["manager_insights"]["summary"])
        st.write(result["manager_insights"]["manager_recommendation"])

    st.subheader("Raw Workflow Trace")
    st.json(result)

else:
    st.info("Use the sidebar and click **Run Multi-Agent Workflow** to start the demo.")

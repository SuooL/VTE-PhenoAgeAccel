import streamlit as st

from utils.calculations import calculate_phenotypic_age, calculate_age_acceleration

def main():
    st.title("Phenotypic Age and Age Acceleration Calculator of VTE")
st.header("Biomarker Input Parameters")

# 创建两列布局（比例可调）
col1, col2 = st.columns([1, 1])  # 等宽两列

with col1:
    age = st.number_input("Chronological age (years):",
                         min_value=0, max_value=120, value=50)

    albumin = st.number_input("Albumin (g/dL) [0.1-10.0]:",
                            min_value=0.1, max_value=10.0, value=4.0, step=0.1)

    creatinine = st.number_input("Creatinine (mg/dL) [0.1-15.0]:",
                               min_value=0.1, max_value=15.0, value=1.0, step=0.1)

    glucose = st.number_input("Glucose (mg/dL) [20-1000]:",
                            min_value=20.0, max_value=1000.0, value=100.0, step=1.0)

    crp = st.number_input("CRP (mg/L) [0.1-500]:",
                        min_value=0.1, max_value=500.0, value=1.0, step=0.1)

with col2:
    lymphocyte = st.number_input("Lymphocyte (cells/μL) [0-50k]:",
                               min_value=0, max_value=50000, value=1500)

    rbc_volume = st.number_input("MCV (fL) [50-150]:",
                               min_value=50.0, max_value=150.0, value=90.0, step=0.1)

    rbc_width = st.number_input("RDW (%) [5-30]:",
                              min_value=5.0, max_value=30.0, value=13.0, step=0.1)

    alkaline = st.number_input("Alk Phos (U/L) [10-2000]:",
                             min_value=10.0, max_value=2000.0, value=100.0, step=1.0)

    wbc_count = st.number_input("WBC (cells/μL) [1k-100k]:",
                              min_value=1000, max_value=100000, value=7000)

    # 底部单位说明
    st.caption("MCV: Mean Corpuscular Volume | RDW: Red Cell Distribution Width | Alk Phos: Alkaline Phosphatase")

    biomarkers = {
        "Albumin1": albumin,
        "Creatinine1": creatinine,
        "Glucose1": glucose,
        "CRP1": crp,
        "Lymphocyte1": lymphocyte,
        "RBCVOLUME1": rbc_volume,
        "RBCWIDTH1": rbc_width,
        "Alkaline1": alkaline,
        "WBCCOUNT1": wbc_count,
        "Age.at.recruitment": age
    }

    if st.button("Calculate"):

        phenotypic_age = calculate_phenotypic_age(biomarkers)
        age_acceleration = calculate_age_acceleration(phenotypic_age, age)

        st.success(f"Your Phenotypic Age is: {phenotypic_age:.2f} years")
        st.success(f"Your Age Acceleration is: {age_acceleration:.2f} years")

if __name__ == "__main__":
    main()
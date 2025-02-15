import streamlit as st

from utils.calculations import calculate_phenotypic_age, calculate_age_acceleration

def main():
    st.title("Phenotypic Age and Age Acceleration Calculator")

    st.header("Input Parameters")
    age = st.number_input("Enter your chronological age:", min_value=0, max_value=120, value=30)

    albumin = st.number_input("Enter your Albumin level:", min_value=0.0, max_value=10.0, value=4.0)
    creatinine = st.number_input("Enter your Creatinine level:", min_value=0.0, max_value=10.0, value=1.0)
    glucose = st.number_input("Enter your Glucose level:", min_value=0.0, max_value=10.0, value=5.0)
    crp = st.number_input("Enter your CRP level:", min_value=0.0, max_value=10.0, value=1.0)
    lymphocyte = st.number_input("Enter your Lymphocyte count:", min_value=0, max_value=10000, value=2000)
    rbc_volume = st.number_input("Enter your RBC Volume:", min_value=0.0, max_value=10.0, value=5.0)
    rbc_width = st.number_input("Enter your RBC Width:", min_value=0.0, max_value=10.0, value=5.0)
    alkaline = st.number_input("Enter your Alkaline level:", min_value=0.0, max_value=10.0, value=5.0)
    wbc_count = st.number_input("Enter your WBC Count:", min_value=0, max_value=10000, value=5000)

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
from streamlit import st
from utils.calculations import calculate_phenotypic_age, calculate_age_acceleration

'''

data$xb1 <- -19.907-0.0336 * data$Albumin1 + 0.0095 *data$Creatinine1 + 0.1953 * data$Glucose1 + 0.0954*log(data$CRP1) - 0.012*data$Lymphocyte1 + 0.0268*data$RBCVOLUME1 + 0.3306*data$RBCWIDTH1 +0.00188 * data$Alkaline1 + 0.0554*data$WBCCOUNT1 + 0.0804*data$Age.at.recruitment

data$mortality_risk1 <- 1 - exp((-1.51714 * exp(data$xb1)) / 0.0076927)
data$pheno_age1<- log(-0.00553*log(1-data$mortality_risk1))/0.090165+141.50225

'''

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
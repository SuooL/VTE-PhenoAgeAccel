import streamlit as st

from utils.calculations import calculate_phenotypic_age, calculate_age_acceleration

def main():
    st.title("Phenotypic Age and Age Acceleration Calculator of VTE")
    st.header("Biomarker Input Parameters")

    # 创建两列布局（比例可调）
    col1, col2 = st.columns([1, 1])  # 等宽两列
    with col1:
        age = st.number_input("Chronological age (years):",
                            min_value=0, max_value=100, value=50)

        albumin = st.number_input("Albumin (g/L) [10-60]:",
                                min_value=10.0, max_value=60.0,
                                value=40.0, step=0.1)

        creatinine = st.number_input("Creatinine (μmol/L) [0-2000]:",
                                   min_value=0.0, max_value=2000.0,
                                   value=88.4, step=1.0)

        glucose = st.number_input("Glucose (mmol/L) [0-40]:",
                                min_value=0.0, max_value=40.0,
                                value=5.5, step=0.1)

        crp = st.number_input("C-reactive protein (mg/L) [0-100]:",
                            min_value=0.0, max_value=100.0,
                            value=1.0, step=0.1)
        st.caption("MCV: Mean Corpuscular Volume")
    with col2:
        lymphocyte = st.number_input("Lymphocyte percentage (%) [0-99]:",
                                   min_value=0.0, max_value=99.0,
                                   value=20.0, step=0.1)

        rbc_volume = st.number_input("MCV (fL) [0-200]:",
                                   min_value=0.0, max_value=200.0,
                                   value=90.0, step=0.1)

        rbc_width = st.number_input("RDW (%) [0-50]:",
                                  min_value=0.0, max_value=50.0,
                                  value=13.0, step=0.1)

        alkaline = st.number_input("Alkaline phosphatase (U/L) [0-2000]:",
                                 min_value=0.0, max_value=2000.0,
                                 value=100.0, step=1.0)

        wbc_count = st.number_input("WBC count (10⁹ cells/L) [0-400]:",
                                  min_value=0.0, max_value=400.0,
                                  value=10.0, step=0.1)

        # 底部单位说明
        st.caption("RDW: Red Cell Distribution Width | Alk Phos: Alkaline Phosphatase")

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

    # 完整位置应如下（在if st.button("Calculate")代码块之后）：
    if st.button("Calculate"):
        phenotypic_age = calculate_phenotypic_age(biomarkers)
        age_acceleration = calculate_age_acceleration(phenotypic_age, age)

        st.success(f"Your Phenotypic Age is: {phenotypic_age:.2f} years")
        st.success(f"Your Age Acceleration is: {age_acceleration:.2f} years")

    # 添加引用（在按钮代码块之后）
    st.markdown("---")

    st.markdown("""
    **Academic Attribution Notice**
    *If this contributes to your research, please consider **citing** our seminal work on biological aging and venous thromboembolism risk assessment:*
    """)

    st.markdown("""
    Hu, Z., Xu, J., Shen, R., Lin, L., Su, Y., Xie, C., You, G., Zhou, Y. and Huang, K. (2025),
    Combination of Biological Aging and Genetic Susceptibility Helps Identifying At-Risk Population of Venous Thromboembolism:
    A Prospective Cohort Study of 394,041 Participants. *American Journal of Hematology*.
    doi: [10.1002/ajh.27605](https://doi.org/10.1002/ajh.27605)
    """)
if __name__ == "__main__":
    main()
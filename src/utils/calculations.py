from math import log, exp

def calculate_phenotypic_age(biomarkers):
    # calculate xb1
    xb1 = -19.907 - 0.0336 * biomarkers["Albumin1"] + 0.0095 * biomarkers["Creatinine1"] + 0.1953 * biomarkers["Glucose1"] + 0.0954 * log(biomarkers["CRP1"]) - 0.012 * biomarkers["Lymphocyte1"] + 0.0268 * biomarkers["RBCVOLUME1"] + 0.3306 * biomarkers["RBCWIDTH1"] + 0.00188 * biomarkers["Alkaline1"] + 0.0554 * biomarkers["WBCCOUNT1"] + 0.0804 * biomarkers["Age.at.recruitment"]

    # calculate mortality_risk1
    mortality_risk1 = 1 - exp((-1.51714 * exp(xb1)) / 0.0076927)

    # calculate pheno_age1
    pheno_age1 = log(-0.00553 * log(1 - mortality_risk1)) / 0.090165 + 141.50225

    return pheno_age1


def calculate_age_acceleration(chronological_age, phenotypic_age):

    # Intercept: -4.704405105637077
    # Age Coefficient: 1.0172367161295937
    lm_phenotypic_age = -4.704405105637077 + 1.0172367161295937 * chronological_age

    return phenotypic_age - lm_phenotypic_age
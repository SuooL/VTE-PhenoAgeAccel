from math import log, exp


def calculate_phenotypic_age(biomarkers):
    # calculate xb1
    xb1 = -19.907 - 0.0336 * biomarkers["Albumin1"] + 0.0095 * biomarkers["Creatinine1"] + 0.1953 * biomarkers["Glucose1"] + 0.0954 * log(biomarkers["CRP1"]) - 0.012 * biomarkers["Lymphocyte1"] + 0.0268 * biomarkers["RBCVOLUME1"] + 0.3306 * biomarkers["RBCWIDTH1"] + 0.00188 * biomarkers["Alkaline1"] + 0.0554 * biomarkers["WBCCOUNT1"] + 0.0804 * biomarkers["Age.at.recruitment"]

    # calculate mortality_risk1
    mortality_risk1 = 1 - exp((-1.51714 * exp(xb1)) / 0.0076927)

    # calculate pheno_age1
    pheno_age1 = log(-0.00553 * log(1 - mortality_risk1)) / 0.090165 + 141.50225

    return pheno_age1


# 依据现有的年龄和表型年龄拟合lm模型，计算年龄加速度


def calculate_age_acceleration(chronological_age, phenotypic_age):

    # 假定拟合出的模型为：lm_phenotypic_age = a * chronological_age + b
    # 则年龄加速度 = phenotypic_age - (a * chronological_age + b)
    # 这里假设 a = 1, b = 0.00125
    lm_phenotypic_age = 1 * chronological_age + 0.00125

    return phenotypic_age - lm_phenotypic_age
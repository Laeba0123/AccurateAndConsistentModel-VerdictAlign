def normalize_input(data: dict):
    return {
        "Age": data["age"],
        "Department": data["department"].strip().title(),
        "JobRole": data["job_role"].strip().title(),
        "MonthlyIncome": data["monthly_income"],
        "YearsAtCompany": data["years_at_company"],
        "JobSatisfaction": data["job_satisfaction"],
        "OverTime": data["overtime"].strip().title(),
        "WorkLifeBalance": data["work_life_balance"]
    }
import pandas as pd


def calculate_completeness(df):

    total_cells = df.size
    missing_cells = df.isnull().sum().sum()

    completeness = ((total_cells - missing_cells) / total_cells) * 100

    return round(completeness, 2)


def calculate_uniqueness(df):

    uniqueness_scores = []

    for column in df.columns:

        unique_ratio = df[column].nunique() / len(df[column])

        uniqueness_scores.append(unique_ratio)

    uniqueness = (
        sum(uniqueness_scores) / len(uniqueness_scores)
    ) * 100

    return round(uniqueness, 2)


def calculate_consistency(df):

    consistent_columns = 0

    for column in df.columns:

        non_null_types = df[column].dropna().map(type)

        if len(non_null_types.unique()) == 1:
            consistent_columns += 1

    consistency = (
        consistent_columns / len(df.columns)
    ) * 100

    return round(consistency, 2)


def generate_recommendations(
    completeness,
    uniqueness,
    consistency
):

    recommendations = []

    if completeness < 95:
        recommendations.append(
            "Dataset contains missing values. Consider handling null entries."
        )

    if uniqueness < 70:
        recommendations.append(
            "Low uniqueness detected. Duplicate or repetitive records may exist."
        )

    if consistency < 85:
        recommendations.append(
            "Inconsistent datatypes found across columns."
        )

    if (
        completeness >= 95 and
        uniqueness >= 85 and
        consistency >= 90
    ):
        recommendations.append(
            "Dataset quality is excellent."
        )

    return recommendations


def generate_quality_report(df):

    completeness = calculate_completeness(df)

    uniqueness = calculate_uniqueness(df)

    consistency = calculate_consistency(df)

    overall_score = round(
        (
            completeness +
            uniqueness +
            consistency
        ) / 3,
        2
    )

    recommendations = generate_recommendations(
        completeness,
        uniqueness,
        consistency
    )

    return {
        "completeness_score": completeness,
        "uniqueness_score": uniqueness,
        "consistency_score": consistency,
        "overall_quality_score": overall_score,
        "recommendations": recommendations
    }
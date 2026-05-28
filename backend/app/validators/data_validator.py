import re

import pandas as pd


def validate_email_columns(df):

    invalid_emails = 0

    email_pattern = (
        r'^[\w\.-]+@[\w\.-]+\.\w+$'
    )

    for column in df.columns:

        if "email" in column.lower():

            for value in df[column].dropna():

                if not re.match(
                    email_pattern,
                    str(value)
                ):

                    invalid_emails += 1

    return invalid_emails


def validate_phone_columns(df):

    invalid_phones = 0

    phone_pattern = r'^\d{10}$'

    for column in df.columns:

        if (
            "phone" in column.lower()
            or
            "mobile" in column.lower()
        ):

            for value in df[column].dropna():

                cleaned = str(value).strip()

                if not re.match(
                    phone_pattern,
                    cleaned
                ):

                    invalid_phones += 1

    return invalid_phones


def detect_duplicate_rows(df):

    duplicates = df.duplicated().sum()

    return int(duplicates)


def detect_outliers(df):

    outlier_count = 0

    numeric_columns = (
        df.select_dtypes(
            include=['number']
        ).columns
    )

    for column in numeric_columns:

        q1 = df[column].quantile(0.25)

        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr

        upper_bound = q3 + 1.5 * iqr

        outliers = df[
            (
                df[column] < lower_bound
            )
            |
            (
                df[column] > upper_bound
            )
        ]

        outlier_count += len(outliers)

    return int(outlier_count)
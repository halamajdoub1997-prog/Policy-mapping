import pandas as pd

def compute_scores(df):

    # weighted score
    df["weighted"] = df["weight"] * df["si"]

    # DOMAIN SCORE
    domain = df.groupby(["country", "domain"]).agg(
        score=("weighted", "sum"),
        max_score=("weight", "sum")
    ).reset_index()

    domain["domain_score"] = (domain["score"] / domain["max_score"]) * 100

    # OVERALL SCORE
    overall = domain.groupby("country").agg(
        total_score=("domain_score", "mean")
    ).reset_index()

    return df, domain, overall

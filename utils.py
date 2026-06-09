def compute_score(df):
    agg = df.groupby(["country", "indicator"])["value"].mean().reset_index()
    agg["score"] = agg["value"] * 100
    return agg

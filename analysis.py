import pandas as pd
from root_causes import categorize_denial_reason

def analyze_data(df):
    # Filter only denied claims (Balance > 0)
    denied_df = df[df["Balance"] > 0].copy()
    
    # Categorize denial reasons
    denied_df["Root Cause"] = denied_df["Denial Reason"].apply(categorize_denial_reason)

    # CPT code stats
    cpt_agg = denied_df.groupby("CPT Code").agg(
        Denials=("CPT Code", "count"),
        Total_Charges=("Balance", "sum")
    ).reset_index()
    
    # Calculate denial rate against total possible charges
    total_charges = df["Balance"].sum() + df["Payment Amount"].sum()
    cpt_agg["Denial Rate"] = cpt_agg["Total_Charges"] / total_charges
    cpt_stats = cpt_agg[["CPT Code", "Denials", "Denial Rate"]].sort_values("Denials", ascending=False)

    # Denials by payer
    payer_stats = denied_df.groupby("Insurance Company").agg(
        Denials=("CPT Code", "count"),
        Lost_Revenue=("Balance", "sum")
    ).reset_index().sort_values("Denials", ascending=False)

    # Denials by provider
    provider_stats = denied_df.groupby("Physician Name").agg(
        Denials=("CPT Code", "count"),
        Lost_Revenue=("Balance", "sum")
    ).reset_index().sort_values("Denials", ascending=False)

    # Root cause analysis
    reason_counts = denied_df["Root Cause"].value_counts().reset_index()
    reason_counts.columns = ["Root Cause", "Count"]
    
    lost_by_cause = denied_df.groupby("Root Cause")["Balance"].sum().reset_index()
    lost_by_cause.columns = ["Root Cause", "Lost Revenue"]

    # Recommended fixes
    fix_recs = {
        "Documentation Issue": "Ensure complete documentation including proper medical necessity justification (CO-16). Implement pre-claim documentation audits.",
        "LCD/NCD": "Verify service meets payer's Local Coverage Determinations. Update charge capture system with latest fee schedules (CO-45).",
        "Prior Authorization": "Implement prior authorization tracking system. Appeal with clinical documentation for medical necessity (CO-96).",
        "Other": "Investigate unspecified denial reasons. Contact payers for clarification and submit appeals with supporting documentation."    }

    return cpt_stats, payer_stats, provider_stats, reason_counts, lost_by_cause, fix_recs
import streamlit as st
from data_processing import load_data
from analysis import analyze_data
import charts

st.title("RCM Denial Data Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload Excel file with denial data", type="xlsx")
if uploaded_file:
    try:
        df = load_data(uploaded_file)
    except ValueError as e:
        st.error(str(e))
        st.stop()

    # Perform analysis
    cpt_stats, payer_stats, provider_stats, reason_counts, lost_by_cause, fix_recs = analyze_data(df)


    # Display Payer denial stats
    st.header("Denials by Payer")
    st.dataframe(payer_stats)
    st.plotly_chart(charts.plot_payer_denials(payer_stats))

    # Display Provider denial stats
    st.header("Denials by Provider")
    st.dataframe(provider_stats)
    st.plotly_chart(charts.plot_provider_denials(provider_stats))

    # Display root cause breakdown
    st.header("Denial Reasons by Root Cause")
    st.dataframe(reason_counts)

    # Display lost revenue by cause
    st.header("Lost Revenue by Root Cause")
    st.dataframe(lost_by_cause)
    st.plotly_chart(charts.plot_lost_revenue(lost_by_cause))

    # Display recommendations for fixes - only show relevant ones
    st.header("Recommended Fixes")
    active_causes = reason_counts["Root Cause"].unique()
    for cause in active_causes:
        if cause in fix_recs:
            st.markdown(f"**{cause}**: {fix_recs[cause]}")
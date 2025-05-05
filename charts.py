import plotly.express as px


def plot_payer_denials(df):
    fig = px.bar(df, x="Insurance Company", y="Denials", title="Denials by Payer")
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def plot_provider_denials(df):
    fig = px.bar(df, x="Physician Name", y="Denials", title="Denials by Provider")
    fig.update_layout(xaxis_tickangle=-45)
    return fig

def plot_lost_revenue(df):
    fig = px.bar(df, x="Root Cause", y="Lost Revenue", title="Lost Revenue by Root Cause")
    fig.update_layout(xaxis_tickangle=-45)
    return fig

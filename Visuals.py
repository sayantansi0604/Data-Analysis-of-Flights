import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("airlines_flights_data.csv")
all_cols = df.columns.tolist()

visual_typ = st.selectbox(
        "Choose a chart type",
        ["Histogram", "Bar Chart", "Scatter Plot", "Correlation Heatmap"]
    )

if visual_typ == "Histogram":
        col = st.selectbox("Select the columns for Histogram", df.columns)
        fig, ax = plt.subplots()
        sns.histplot(df[col], kde=True, ax=ax)
        st.pyplot(fig)

elif visual_typ == "Bar Chart":
        col = st.selectbox("Select column for bar chart (categorical)", df.columns)
        fig, ax = plt.subplots()
        df[col].value_counts().plot(kind="bar", ax=ax)
        st.pyplot(fig)

elif visual_typ == "Scatter Plot":
        x_col = st.selectbox("Select X-axis", df.columns)
        y_col = st.selectbox("Select Y-axis", df.columns)
        fig, ax = plt.subplots()
        sns.scatterplot(x=df[x_col], y=df[y_col], ax=ax)
        st.pyplot(fig)

elif visual_typ == "Correlation Heatmap":
        fig, ax = plt.subplots()
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

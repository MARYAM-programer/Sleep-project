# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Read Data
df = pd.read_csv("sleep.csv")

# Clean data
df["Sleep Disorder"] = df["Sleep Disorder"].replace(np.nan, "Normal")

# Sidebar
st.sidebar.header("Sleep Dashboard")
st.sidebar.image("download.jpg")
st.sidebar.write("The purpose of this dashboard is to show the reasons for sleep disorders.")

# Sidebar filters
filter_column = st.sidebar.selectbox('Filter by', ['Gender', 'Occupation', 'BMI Category', 'Sleep Disorder'])

# Apply filter if selected
if filter_column:
    selected_value = st.sidebar.selectbox(f"Select {filter_column}", df[filter_column].unique())
    df = df[df[filter_column] == selected_value]

# KPIs
a1, a2, a3, a4 = st.columns(4)
a1.metric("Avg Age", round(df['Age'].mean(), 2))
a2.metric("Count of IDs", int(df['Person ID'].nunique()))
a3.metric("Max Daily Steps", int(df['Daily Steps'].max()))
a4.metric("Avg Sleep Duration (hrs)", round(df['Sleep Duration'].mean(), 1))

# Optional: Show filtered data
st.write("### Filtered Dataset")
st.dataframe(df)

# ---- Charts ----
st.write("## 📊 Sleep Analysis Charts")

# Chart 1: Sleep Duration Distribution
st.write("### 1. Distribution of Sleep Duration")
fig1, ax1 = plt.subplots()
sns.histplot(df['Sleep Duration'], bins=20, kde=True, ax=ax1, color="teal")
ax1.set_xlabel("Sleep Duration (hours)")
ax1.set_ylabel("Count")
st.pyplot(fig1)
# Chart 2: Average Sleep Duration by Sleep Disorder 
st.write("### 2. Average Sleep Duration by Sleep Disorder ")
avg_sleep = df.groupby("Sleep Disorder")["Sleep Duration"].mean().sort_values(ascending=True)
fig2, ax2 = plt.subplots()
avg_sleep.plot(kind='barh', color='skyblue', ax=ax2)
ax2.set_xlabel("Avg Sleep Duration (hrs)")
ax2.set_title("Avg Sleep by Disorder")
st.pyplot(fig2)

# Chart 3: Count of Sleep Disorders by Gender
st.write("### 3. Count of Sleep Disorders by Gender")
fig3, ax3 = plt.subplots()
sns.countplot(data=df, x="Sleep Disorder", hue="Gender", ax=ax3)
ax3.set_ylabel("Count")
ax3.set_title("Sleep Disorders by Gender")
st.pyplot(fig3)

# اختبار الاعمدة الرقمية
num_cols =['Physical Activity Level','Stress Level','Daily Steps','Quality of Sleep']
df_num =df[num_cols]

st.text("Pair Plot")
fig_pair = sns.pairplot(df_num)
st.pyplot(fig_pair)
st.text("Corrolation Heatmap(Selected Numertical Features)")



selected_cols = ['Sleep Duration', 'Quality of Sleep', 'Physical Activity Level',
                 'Stress Level', 'Heart Rate', 'Daily Steps']
df_selected = df[selected_cols]


#Heatmap
fig_heat,ax,= plt.subplots(figsize=(10,6))
sns.heatmap(df_selected.corr(),annot=True, cmap='coolwarm', fmt='.2f',ax=ax)
st.pyplot(fig_heat)






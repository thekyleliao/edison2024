import streamlit as st
import pandas as pd
import plotly.express as px
st.title("Thomas A. Edison CTE HS Financial Dashboard Overview(2024)")
st.write("Data Source: Galaxy Tables of Organization and Galaxy Allocations")
st.divider()
st.image('edison.jpg', caption="Welcome to Edison!")
st.divider()

with st.expander("Income"):
    st.link_button("Link to Income", "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxyallocation/default.aspx", help="Enter Q620", type="primary")
    incomeGraphData = pd.read_csv("Income.csv")
    incomeFigure = px.pie(incomeGraphData, values="Dollar Amount", names="Source of Income", title="Income Overview")
    st.plotly_chart(incomeFigure)
    incomeTable = pd.read_csv("Income.csv")
    st.table(incomeTable)
with st.expander("Expenses(Salary)"):
    st.link_button("Link to Expenses", "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/default.aspx?DDBSSS_INPUT=Q620", help="Enter Q620", type="primary")
    expenses_S_GraphData = pd.read_csv("Expenses_Staff.csv")
    expenses_S_Figure = px.pie(expenses_S_GraphData, values=" Dollar Cost", names="Position", title="Salary(relative to roles) Overview")
    st.plotly_chart(expenses_S_Figure)
    Expenses_S_Table = pd.read_csv("Expenses_Staff.csv")
    st.table(Expenses_S_Table)
with st.expander("Expenses(Misc)"):
    st.link_button("Link to Expenses", "https://www.nycenet.edu/offices/d_chanc_oper/budget/dbor/galaxy/galaxybudgetsummaryto/default.aspx?DDBSSS_INPUT=Q620", help="Enter Q620", type="primary")
    expenses_M_GraphData = pd.read_csv("Expenses_Misc.csv")
    expenses_M_Figure = px.pie(expenses_M_GraphData, values=" Dollar Cost", names="Type", title="Expenses(Non-Salary) Overview")
    st.plotly_chart(expenses_M_Figure)
    Expenses_M_Table = pd.read_csv("Expenses_Misc.csv")
    st.table(Expenses_M_Table)


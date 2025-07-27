import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Excel Animated Plot", layout="centered")

st.title("Eco-Sense: Wildlife Monitoring System")

# File uploader
uploaded_file = st.file_uploader("Upload an Excel File", type=["csv", "xlsx"])

if uploaded_file:
    try:
        # Read the Excel file
        df = pd.read_excel(uploaded_file)
        st.success("✅ File uploaded and read successfully!")
        
        # Show the first few rows
        st.subheader("🔍 Preview of Data")
        st.dataframe(df.head())

        # Select columns
        numeric_columns = df.select_dtypes(include='number').columns.tolist()
        if len(numeric_columns) < 2:
            st.warning("Please upload a file with at least two numeric columns.")
        else:
            x_col = st.selectbox("Choose X-axis column", numeric_columns)
            y_col = st.selectbox("Choose Y-axis column", numeric_columns, index=1 if len(numeric_columns) > 1 else 0)

            # Plot type selection
            chart_type = st.selectbox("Choose Chart Type", ["Line", "Bar", "Scatter"])

            # Create plot
            st.subheader("📈 Interactive Plot")
            if chart_type == "Line":
                fig = px.line(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
            elif chart_type == "Bar":
                fig = px.bar(df, x=x_col, y=y_col, title=f"{chart_type} Chart")
            else:
                fig = px.scatter(df, x=x_col, y=y_col, title=f"{chart_type} Chart")

            st.plotly_chart(fig, use_container_width=True)

            # Show summary statistics
            st.subheader("📊 Summary Statistics")
            st.write(f"**{y_col}** - Mean: {df[y_col].mean():.2f}, Max: {df[y_col].max():.2f}, Min: {df[y_col].min():.2f}")

    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")

else:
    st.info("Please upload an Excel file to begin.")

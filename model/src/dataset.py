import streamlit as st
import pandas as pd

def show_dataset_page():
    df = pd.read_csv(
        "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/Algerian-Fire-Forecaster/refs/heads/main/data/cleaned_data/Algerian_forest_fires_dataset_cleaned.csv"
    )

    rows = int(df.shape[0])
    ip_rows = st.number_input(
        """#### Choose the number of rows you'd like to see:""",
        key=int,
        step=5,
        value=30,
    )

    if ip_rows < rows:
        st.write(f"""#### Displaying the first {ip_rows} rows (Cleaned Data)""")
        st.write(df.head(ip_rows))
    else:
        st.write(f"""#### Displaying all the rows (Cleaned Data)""")
        st.write(df.head(rows))

    st.download_button(
        label="Download Full Dataset",
        data="https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/Algerian-Fire-Forecaster/refs/heads/main/data/cleaned_data/Algerian_forest_fires_dataset_cleaned.csv",
        file_name="Forest Fire Data_Cleaned.csv",
    )

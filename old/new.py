import streamlit as st
import pandas as pd
import os

def main():
    """
    Main function to run the Streamlit app.
    """
    st.title("CSV File Viewer")

    # Get the list of all files in the current directory
    files = [f for f in os.listdir('.') if os.path.isfile(f)]

    # Filter for CSV files
    csv_files = [f for f in files if f.endswith('.csv')]

    if not csv_files:
        st.warning("No CSV files found in the current directory.")
        return

    # Create a select box to choose a file
    selected_file = st.selectbox("Import File", csv_files)

    if selected_file:
        try:
            # Read the selected CSV file into a pandas DataFrame
            df = pd.read_csv(selected_file)

            # Display the DataFrame
            st.write(f"Displaying top 5 rows of **{selected_file}**:")
            st.dataframe(df.head())

        except Exception as e:
            st.error(f"Error reading the file: {e}")

if __name__ == "__main__":
    main()
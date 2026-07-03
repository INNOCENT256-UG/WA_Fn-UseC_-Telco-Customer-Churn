"""
Export Telco Customer Churn dataset to Excel format for easy reporting
"""
import pandas as pd
from datetime import datetime
import sys

try:
    # Read the CSV file
    print("Reading CSV file...")
    df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print(f"✓ Loaded {len(df)} records")
    
    # Convert TotalCharges to numeric (it may be read as string)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    print("✓ Data types cleaned")
    
    excel_file = 'Telco_Customer_Churn_Report.xlsx'
    print(f"\nCreating Excel file: {excel_file}")
    
    # Create all dataframes first
    print("Preparing data for all sheets...")
    
    # Sheet 1: Complete Dataset (already have df)
    
    # Sheet 2: Summary Statistics
    summary_data = {
        'Metric': [
            'Total Customers',
            'Total Churned',
            'Total Retained',
            'Churn Rate (%)',
            'Average Monthly Charges',
            'Average Total Charges',
            'Average Tenure (months)',
            'Male Customers',
            'Female Customers',
            'Senior Citizens',
            'Report Generated'
        ],
        'Value': [
            len(df),
            len(df[df['Churn'] == 'Yes']),
            len(df[df['Churn'] == 'No']),
            round((len(df[df['Churn'] == 'Yes']) / len(df)) * 100, 2),
            round(df['MonthlyCharges'].mean(), 2),
            round(df['TotalCharges'].mean(), 2),
            round(df['tenure'].mean(), 2),
            len(df[df['gender'] == 'Male']),
            len(df[df['gender'] == 'Female']),
            len(df[df['SeniorCitizen'] == 1]),
            datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ]
    }
    summary_df = pd.DataFrame(summary_data)
    print("✓ Summary data prepared")
    
    # Sheet 3: Churn Analysis by Contract Type
    contract_analysis = df.groupby('Contract').agg({
        'customerID': 'count',
        'MonthlyCharges': 'mean',
        'TotalCharges': 'mean',
        'tenure': 'mean'
    }).round(2)
    contract_analysis.columns = ['Customer Count', 'Avg Monthly Charges', 'Avg Total Charges', 'Avg Tenure']
    contract_analysis['Churn Count'] = df[df['Churn'] == 'Yes'].groupby('Contract').size()
    contract_analysis['Churn Rate (%)'] = (contract_analysis['Churn Count'] / contract_analysis['Customer Count'] * 100).round(2)
    contract_analysis = contract_analysis.reset_index()
    print("✓ Contract analysis prepared")
    
    # Sheet 4: Churn Analysis by Internet Service
    internet_analysis = df.groupby('InternetService').agg({
        'customerID': 'count',
        'MonthlyCharges': 'mean',
        'TotalCharges': 'mean'
    }).round(2)
    internet_analysis.columns = ['Customer Count', 'Avg Monthly Charges', 'Avg Total Charges']
    internet_analysis['Churn Count'] = df[df['Churn'] == 'Yes'].groupby('InternetService').size()
    internet_analysis['Churn Rate (%)'] = (internet_analysis['Churn Count'] / internet_analysis['Customer Count'] * 100).round(2)
    internet_analysis = internet_analysis.reset_index()
    print("✓ Internet service analysis prepared")
    
    # Sheet 5: Payment Method Analysis
    payment_analysis = df.groupby('PaymentMethod').agg({
        'customerID': 'count',
        'MonthlyCharges': 'mean'
    }).round(2)
    payment_analysis.columns = ['Customer Count', 'Avg Monthly Charges']
    payment_analysis['Churn Count'] = df[df['Churn'] == 'Yes'].groupby('PaymentMethod').size()
    payment_analysis['Churn Rate (%)'] = (payment_analysis['Churn Count'] / payment_analysis['Customer Count'] * 100).round(2)
    payment_analysis = payment_analysis.reset_index()
    print("✓ Payment method analysis prepared")
    
    # Write all sheets at once
    print("\nWriting all sheets to Excel file...")
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Customer Data', index=False)
        print("  ✓ Customer Data sheet written")
        
        summary_df.to_excel(writer, sheet_name='Summary', index=False)
        print("  ✓ Summary sheet written")
        
        contract_analysis.to_excel(writer, sheet_name='Contract Analysis', index=False)
        print("  ✓ Contract Analysis sheet written")
        
        internet_analysis.to_excel(writer, sheet_name='Internet Service Analysis', index=False)
        print("  ✓ Internet Service Analysis sheet written")
        
        payment_analysis.to_excel(writer, sheet_name='Payment Method Analysis', index=False)
        print("  ✓ Payment Method Analysis sheet written")
    
    print(f"\n{'='*60}")
    print(f"✓ Excel file created successfully: {excel_file}")
    print(f"✓ Total records exported: {len(df)}")
    print(f"✓ Number of sheets: 5")
    print(f"{'='*60}")
    print("\nSheets created:")
    print("  1. Customer Data - Complete dataset")
    print("  2. Summary - Key metrics and statistics")
    print("  3. Contract Analysis - Churn by contract type")
    print("  4. Internet Service Analysis - Churn by internet service")
    print("  5. Payment Method Analysis - Churn by payment method")
    
except Exception as e:
    print(f"\n✗ Error: {str(e)}", file=sys.stderr)
    import traceback
    traceback.print_exc()
    sys.exit(1)
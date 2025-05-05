import pandas as pd

def load_data(uploaded_file):
    try:
        # First read without headers to find the correct row
        temp_df = pd.read_excel(uploaded_file, header=None)
        
        # Define required columns (case-insensitive, whitespace-insensitive)
        required = {'cpt code', 'insurance company', 'physician name', 
                   'payment amount', 'balance', 'denial reason'}
        
        # Find header row by matching required columns
        header_row = None
        for idx, row in temp_df.iterrows():
            clean_columns = {str(col).strip().lower() for col in row}
            if required.issubset(clean_columns):
                header_row = idx
                break
                
        if header_row is None:
            raise ValueError("Could not find required columns in any row")
            
        # Re-read with proper header
        df = pd.read_excel(uploaded_file, header=header_row)
        
        # Clean column names
        df.columns = [str(col).strip() for col in df.columns]
        
        # Standardize column names (case-insensitive)
        column_map = {
            'cpt code': 'CPT Code',
            'insurance company': 'Insurance Company',
            'physician name': 'Physician Name',
            'payment amount': 'Payment Amount',
            'balance': 'Balance',
            'denial reason': 'Denial Reason'
        }
        
        df.rename(columns=lambda x: column_map.get(x.lower().strip(), x), inplace=True)
        
        # Validate columns
        missing = [col for col in column_map.values() if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns after standardization: {missing}")
            
        # Process financial columns
        for col in ['Payment Amount', 'Balance']:
            df[col] = df[col].replace('[\$,]', '', regex=True).astype(float)
            
        return df

    except Exception as e:
        raise ValueError(f"File processing failed: {str(e)}")
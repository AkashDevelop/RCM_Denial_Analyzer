def categorize_denial_reason(reason):
    text = str(reason).lower().strip()
    
    if "missing information" in text:  # CO-16
        return "Documentation Issue"
    if "exceeds fee schedule" in text:  # CO-45
        return "LCD/NCD"
    if "non-covered service" in text:  # CO-96
        return "Prior Authorization"
    if text in ["", "nan"]:  # Empty denial reasons
        return "Other"  # Changed from "Paid Claim"
    return "Other"
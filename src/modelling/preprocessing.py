from sklearn.model_selection import train_test_split

def preprocess_data(df):
    """Preprocess the abalone dataset."""
    # Create the target variable 'Age'
    df["Age"] = df["Rings"] + 1.5
    
    # Features and target
    X = df.drop(columns=["Rings", "Age", "Sex"])  # Drop 'Sex', 'Rings', and 'Age'
    y = df["Age"]
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

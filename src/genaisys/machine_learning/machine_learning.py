# Implemented in Chapter05
# Implementing a Decision Tree for bounded variable predictions
import os
import pandas as pd
import random
from sklearn.preprocessing import LabelEncoder  # For encoding categorical variables
from sklearn.tree import DecisionTreeClassifier  # For training the Decision Tree model
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

# Path to resources folder
RESOURCES_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'resources')
# Predicts what activity customers like based on their locations
# Example: People in Paris liked museum / People in Rome liked historical tours
def ml_agent(feature1_value, feature2_column):
    """
    :param feature1_value: location
    :return:
    """
    # Load the dataset
    csv_path = os.path.join(RESOURCES_PATH, 'customer_activities.csv')
    df = pd.read_csv(csv_path)

    # Encode categorical variables
    le_location = LabelEncoder() # Convert text into numbers
    le_activity = LabelEncoder()
    """
    LOCATION_ENCODED
    (Paris)0, 1, 2, 3....
    ACTIVITY_ENCODED
    (Efel Tower)0, 1, 2, 3....
    """
    df["LOCATION_ENCODED"] = le_location.fit_transform(df["LOCATION"])
    df["ACTIVITY_ENCODED"] = le_activity.fit_transform(df["ACTIVITY"])

    # Select default location if feature1_value is empty
    if not feature1_value.strip():  # If empty string or only spaces, handle the case " "
        feature1_value = df["LOCATION"].mode()[0]  # Most common location

    # Prepare features and target
    X = df[["LOCATION_ENCODED"]] # Input (features)
    y = df["ACTIVITY_ENCODED"] # Output (what we want to predict)

    # Train a Decision Tree classifier
    model = DecisionTreeClassifier(random_state=42) # The ML model. ML models cannot work with text, only numbers
    model.fit(X, y) # Training the decision tree -> “If LOCATION = Paris → ACTIVITY = Museum”

    # Encode the feature1 value for prediction
    feature1_encoded = le_location.transform([feature1_value])[0]

    # Predict the most probable activity
    predicted_activity_encoded = model.predict([[feature1_encoded]])[0]
    # Decode back to text
    predicted_activity = le_activity.inverse_transform([predicted_activity_encoded])[0]

    # Generate output text
    text = (f"The customers liked the {predicted_activity} because it reminded them of how "
            f"our democracies were born and how it works today. "
            f"They would like more activities during their trips that provide insights into "
            f"the past to understand our lives.")

    return text

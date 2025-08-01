import pickle
import numpy as np

def test_model():
    """Test if the model loads and makes predictions correctly"""
    try:
        # Try to load the model
        print("Loading model...")
        model = pickle.load(open('model.pkl', 'rb'))
        print("✓ Model loaded successfully")
        
        # Create sample data for testing
        sample_features = [0, 0, 0, 0, 12, 1, 1, 1, 0, 0, 0, 1, 0, 50.0, 600.0]
        
        # Make prediction
        print("Making prediction with sample data...")
        prediction = model.predict([sample_features])
        result = 'Churn' if prediction[0] == 1 else 'No Churn'
        print(f"✓ Prediction successful: {result}")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Testing Customer Churn Model")
    print("=" * 30)
    
    success = test_model()
    
    if success:
        print("\n✓ Model test passed! Ready for deployment.")
    else:
        print("\n✗ Model test failed! Check the model file and dependencies.") 
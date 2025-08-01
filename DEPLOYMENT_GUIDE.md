# Customer Churn Prediction Model - Deployment Guide

## Overview
This guide will help you deploy your customer churn prediction model using Streamlit. The app predicts whether a customer will churn based on their profile features.

## Files Structure
```
├── churn_app.py          # Main Streamlit application
├── model.pkl             # Trained machine learning model
├── churn_model.pkl       # Alternative model file
├── requirements.txt      # Python dependencies
├── .streamlit/config.toml # Streamlit configuration
└── DEPLOYMENT_GUIDE.md  # This file
```

## Deployment Options

### Option 1: Streamlit Cloud (Recommended - Free)

1. **Prepare Your Repository**
   - Make sure all files are committed to a Git repository (GitHub, GitLab, etc.)
   - Ensure your repository is public or you have a Streamlit Cloud account

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set the path to your app: `churn_app.py`
   - Click "Deploy"

3. **Access Your App**
   - Your app will be available at: `https://your-app-name.streamlit.app`

### Option 2: Heroku

1. **Create Procfile**
   ```bash
   echo "web: streamlit run churn_app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

2. **Deploy to Heroku**
   ```bash
   # Install Heroku CLI
   # Create new Heroku app
   heroku create your-churn-app
   
   # Add files and deploy
   git add .
   git commit -m "Deploy churn prediction app"
   git push heroku main
   ```

### Option 3: Local Deployment

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the App**
   ```bash
   streamlit run churn_app.py
   ```

3. **Access Locally**
   - Open your browser and go to: `http://localhost:8501`

### Option 4: Docker Deployment

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim
   
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   
   COPY . .
   
   EXPOSE 8501
   
   CMD ["streamlit", "run", "churn_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Build and Run**
   ```bash
   docker build -t churn-app .
   docker run -p 8501:8501 churn-app
   ```

## Testing Your Deployment

1. **Local Testing**
   - Run the app locally first to ensure everything works
   - Test with sample data to verify predictions

2. **Model Validation**
   - Ensure your model files (`model.pkl` or `churn_model.pkl`) are included
   - Verify the model can load and make predictions

3. **Feature Validation**
   - Test all input fields in the sidebar
   - Verify the preprocessing function works correctly

## Troubleshooting

### Common Issues

1. **Model Loading Error**
   - Ensure model files are in the correct directory
   - Check file paths are relative, not absolute

2. **Missing Dependencies**
   - Verify all packages in `requirements.txt` are installed
   - Check for version conflicts

3. **Port Issues**
   - Ensure port 8501 is available
   - Check firewall settings

4. **Memory Issues**
   - Large model files may cause deployment issues
   - Consider model optimization or compression

## Security Considerations

1. **Model Protection**
   - Consider model encryption for sensitive data
   - Implement rate limiting for production use

2. **Input Validation**
   - Add input validation to prevent malicious data
   - Sanitize user inputs

3. **API Keys**
   - Never commit API keys to version control
   - Use environment variables for sensitive data

## Monitoring and Maintenance

1. **Performance Monitoring**
   - Monitor app response times
   - Track prediction accuracy

2. **Model Updates**
   - Plan for model retraining and updates
   - Version control your models

3. **User Analytics**
   - Track app usage and user behavior
   - Monitor prediction patterns

## Support

For issues with deployment:
1. Check the Streamlit documentation
2. Review error logs in your deployment platform
3. Test locally before deploying
4. Ensure all dependencies are correctly specified

## Next Steps

After successful deployment:
1. Share your app URL with stakeholders
2. Collect user feedback
3. Monitor performance metrics
4. Plan for model improvements and updates 
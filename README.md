# 🌍 TripSmart - AI-Powered Travel Recommendation System

TripSmart is an intelligent travel recommendation web application that helps users discover the perfect travel destinations in India based on their preferences.

## ✨ Features

- **Smart Recommendations**: Get personalized travel destination suggestions based on your preferences
- **Budget-Friendly**: Filter destinations by your budget range
- **Activity-Based**: Choose destinations based on activities you enjoy
- **User-Friendly Interface**: Clean and intuitive web interface
- **Comprehensive Data**: Covers popular travel destinations across India

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn, pandas, numpy
- **Frontend**: HTML, CSS, JavaScript
- **Deployment**: Vercel (Serverless)

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/tripsmart.git
   cd tripsmart
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
tripsmart/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── vercel.json                 # Vercel deployment configuration
├── .vercelignore              # Files to exclude from deployment
├── data/
│   └── india_travel_destinations.csv  # Travel data
├── model/
│   └── recommender.py         # Recommendation engine
├── templates/
│   ├── index.html             # Home page
│   └── recommendations.html   # Results page
└── static/                    # CSS, JS, images
```

## 🎯 How It Works

1. Users input their travel preferences (budget, activities, etc.)
2. The recommendation engine processes the input using machine learning
3. The system returns personalized destination suggestions
4. Users can view detailed information about each recommended destination

## 🌐 Deployment

This project is configured for deployment on Vercel. See `VERCEL_DEPLOYMENT_STEPS.md` for detailed deployment instructions.

### Quick Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/tripsmart)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Your Name**
- GitHub: [@YOUR_USERNAME](https://github.com/YOUR_USERNAME)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/YOUR_USERNAME/tripsmart/issues).

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ for travelers**

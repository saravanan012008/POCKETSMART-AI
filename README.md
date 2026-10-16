# POCKETSMART-AI
PocketSmart AI is an AI-powered budget planning web application built with Python, FastAPI, and Google Gemini. It helps users plan home interiors, organize parties, and explore jewelry recommendations based on their budget and preferences.

## 📁 Project Structure

pocketnewai(fresh)/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── auth.py
│   ├── models/
│   │   └── schemas.py
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── planner_routes.py
│   │   └── page_routes.py
│   ├── services/
│   │   ├── gemini_utils.py
│   │   └── recommendations.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── planner.html
│   │   └── history.html
│   └── static/
│       ├── css/style.css
│       └── js/app.js
├── data/
├── tests/
│   └── test_app.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md

*The exact contents may vary depending on your project version.*

## ⚙️ Requirements

Before running PocketSmart AI, install:

- Python 3.12 or another Python version compatible with the project's dependencies
- pip
- A Google Gemini API key for AI-powered recommendations

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Open the project folder

```bash
cd YOUR_PROJECT_FOLDER
```

### 3. Create a virtual environment

**Windows:**

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```cmd
.venv\Scripts\activate.bat
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root, alongside `requirements.txt`.

Add the environment variable names expected by your application:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
```

Replace the placeholders with your actual API key and a Gemini model available to your account.

**Security:** Never commit your `.env` file or expose your API key in a public repository.

### 7. Run the application

```bash
python -m uvicorn app.main:app --reload
```

### 8. Open the application

Visit:

http://127.0.0.1:8000

## 🤖 AI Integration

PocketSmart AI uses Google's Gemini API to generate recommendations based on user requirements and budget information.

If Gemini is unavailable or a request fails, the application may display demo fallback recommendations instead.

AI-generated prices are estimates and should be independently verified before making purchases.

## 🔒 Security

- Keep API keys and other secrets in environment variables.
- Never upload `.env` or your virtual environment.
- Use `.gitignore` to exclude sensitive and generated files.
- Do not commit databases containing private user information.
- Configure authentication and session security appropriately before deployment.

## 🧪 Testing

If the project includes pytest tests, run:

```bash
python -m pytest
```

## 🔮 Future Improvements

- Improved budget optimization
- More personalized recommendations
- Additional planning categories
- Enhanced recommendation history
- Improved error handling and AI availability
- Deployment to a cloud hosting platform

## ⚠️ Disclaimer

PocketSmart AI provides planning suggestions and estimated prices for informational purposes only. Prices, product availability, and marketplace listings may change. Always verify details before purchasing.


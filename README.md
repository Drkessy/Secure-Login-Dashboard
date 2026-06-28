#Project Title: Secure Login Dashboard

# Overview
The Secure Login Dashboard is a web application built using Streamlit, designed to demonstrate user authentication and modular application architecture. This project showcases how to create a secure login interface while separating the application logic from the user interface. 

# Features
- User Authentication: Secure login system with hardcoded credentials (can be extended to use a database).
- Modular Architecture: Separation of concerns by splitting the app into app.py (UI) and auth_logic.py (backend logic).
- Real-time Metrics: Displays user metrics such as projects, tasks, and completed tasks once logged in.
- Responsive Design: User-friendly interface that adapts well to different screen sizes.

# Technologies Used
- Python: Programming language for backend logic.
- Streamlit: Framework for building the web application.
- GitHub: Version control and code repository.
- Streamlit Community Cloud: Hosting platform for deploying the application.

## Installation
To run this project locally, follow these steps:
1. Clone the Repository:
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
2. Create a Virtual Environment (optional but recommended):
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install Dependencies:
   pip install -r requirements.txt
4. Run the Application:
   streamlit run app.py
   
# Usage
1. Navigate to the application in your browser (usually at http://localhost:8501).
2. Enter the credentials:
   - Email: kessingtongodspower@gmail.com
   - Password: kess123#
3. Click the Login button to access the dashboard.
4. Once logged in, you can view your project metrics.
5. Click Logout to return to the login screen.

# Future Enhancements
- Integrate a real database for user authentication.
- Implement password hashing for security.
- Add features like user registration and password recovery.
- Enhance the UI with more interactive components.

# License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Acknowledgments
- Hielite Academy for providing the foundational knowledge.
- Streamlit Community for the amazing framework and support.

# Secure-Login-Dashboard
The Secure Login Dashboard is a web application designed to provide a seamless user authentication experience using the Streamlit framework.

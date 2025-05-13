# SMS Spam Detector

## Description

The SMS Spam Detector is a web application that classifies SMS messages as spam or not. It uses a machine learning model (Random Forest) to detect if a given message is spam based on its content.

This app provides an easy-to-use interface where users can input an SMS message and receive a classification indicating whether the message is likely to be spam or not.

## Features

* **SMS Spam Classification**: Users can input any SMS message, and the app will classify it as spam or not.
* **Flask Web Interface**: A simple web interface to interact with the app.
* **Deployed on Heroku**: The app is hosted on Heroku for easy access and deployment.

---

## How to Run the Project Locally

### Prerequisites

Before you start, make sure you have the following installed on your local machine:

* **Python 3.x** (You can download it from [here](https://www.python.org/downloads/))
* **Pip** (Package manager for Python)
* **Git** (To clone the repository)

### Steps to Run Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nyiel/sms-spam-detector.git
   cd sms-spam-detector
   ```

2. **Install dependencies**:
   Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally**:

   ```bash
   python app.py
   ```

   This should start the Flask development server. You should see output indicating the server is running on `http://127.0.0.1:5000`.

4. Open your browser and go to `http://127.0.0.1:5000` to interact with the app locally.

---

## How to Interact with the Application

1. **Access the Web Interface**:

   * Open the application in your browser (either via the local link or Heroku URL).

2. **Input an SMS Message**:

   * On the homepage, there will be a form to input an SMS message.

3. **Get the Classification**:

   * After submitting the form, the app will classify the message as **Spam** or **Not Spam** and display the result on the screen.

---

## Deployment

This app is deployed on **Heroku**. You can access it via the following URL:

[Your Heroku URL](https://sms-spam-detector-02fa39e55123.herokuapp.com/)

---

## Technologies Used

* **Python** (Backend)
* **Flask** (Web Framework)
* **Gunicorn** (Web Server for production)
* **Heroku** (App Hosting)

---

## Contributing

1. Fork the repository.
2. Create a new branch for your feature/bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a Pull Request to the main repository.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

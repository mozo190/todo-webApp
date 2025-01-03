# What is this project about?

This project is a simple implementation of a web application using Streamlit. The application includes a contact form and a homepage showcasing various projects. The contact form allows users to send messages via email, while the homepage displays information about the developer and their projects.

## Features

- **Contact Form**: Users can send messages through a contact form. The form includes fields for name, email address, and message. Upon submission, the message is sent to a specified email address.
- **Homepage**: The homepage provides information about the developer, including their skills and experience. It also displays a list of projects with descriptions and links to the source code.

## Technologies Used

- **Python**: The primary programming language used for the application.
- **Streamlit**: A framework used to create the web application.
- **smtplib**: A Python library used to send emails.
- **pandas**: A library used for data manipulation and analysis.
- **SSL**: Used for secure email transmission.

## Files

- `pages/Contact_Us.py`: Contains the code for the contact form.
- `send_email.py`: Contains the function to send emails.
- `Home.py`: Contains the code for the homepage.
- `data.csv`: A CSV file containing data about the projects displayed on the homepage.
- `images/`: A directory containing images used in the application.

## How to Run

1. Install the required packages:
    ```sh
    pip install streamlit pandas
    ```

2. Run the Streamlit application:
    ```sh
    streamlit run Home.py
    ```

3. Open your web browser and navigate to the provided URL to view the application.

## Contact

For any questions or suggestions, feel free to contact the developer through the contact form on the application.
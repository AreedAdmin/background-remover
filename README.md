# Background Remover

This is an open-source Flask-based web application that allows users to remove the background from images using the **rembg** library. It offers a user-friendly drag & drop interface for uploading images, processes them on the server, and displays a history of processed images.

## Features

- **Image Background Removal:** Automatically removes the background from uploaded images.
- **Drag & Drop Interface:** Simple and intuitive file upload.
- **Processed Image History:** Displays thumbnails of all processed images.
- **Docker Support:** Easily deploy the application using Docker.

## Project Structure
areed_rem_bg/
├── static/
│   ├── processed/    # Directory for processed images
│   └── style.css     # Custom styles
├── templates/
│   └── index.html    # Main HTML template
├── venv/             # Virtual environment (should not be tracked)
├── app.py            # Flask application
├── requirements.txt  # Project dependencies
├── Dockerfile        # Docker configuration
├── .gitignore        # Git ignore rules
└── README.md         # Project documentation

## Installation and Running Locally

### Prerequisites

- Python 3.9 or later
- pip

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/areedAdmin/background-remover.git
   cd background-remover

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   ```

4. **Access the application:**

   Open your web browser and navigate to `http://localhost:2000`.

## Running with Docker

1. **Build the Docker image:**

   ```bash
   docker build -t background-remover .
   ```

2. **Run the Docker container:**

   ```bash
   docker run -d -p 2000:2000 background-remover
   ```

3. **Access the application:**

   Open your web browser and navigate to `http://localhost:2000`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License
This project is open-sourced under the MIT License - see the LICENSE file for details.

## Acknowledgments
- [rembg](https://github.com/danielgatis/rembg) for the background removal library.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Docker](https://www.docker.com/) for the containerization platform.
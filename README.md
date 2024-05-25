# Vite + Flask Project

This repository contains a web application that uses Vite for the front end and Flask for the back end. This setup combines the fast development experience of Vite with the powerful backend capabilities of Flask.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites
- Node.js (v14 or later)
- Python (v3.8 or later)
- pip (Python package installer)

### Front End (Vite)

1. **Clone the repository:**
   ```sh
   git clone https://github.com/adityab894/depression.git
   cd Mindfulmoments
   ```

2. **Install dependencies:**
   ```sh
   npm install
   ```

3. **Build the front end:**
   ```sh
   npm run
   npm run dev
   ```

### Back End (Flask)

Split the terminal in code editor or opne new terminal without closing the previous one...
1. **Navigate to the backend directory:**
   ```sh
   cd server
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   or
   python package_installer.py // file is there which has all the requirements.....
   ```


## Project Structure

```
vite-flask-app/
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── routes.py
│   ├── venv/
│   ├── requirements.txt
│   └── run.py
└── README.md
```

- **frontend/**: Contains the Vite front-end code.
- **backend/**: Contains the Flask back-end code.
- **venv/**: Python virtual environment (should be excluded from version control).
- **requirements.txt**: Lists the Python dependencies.

## Configuration

### Vite Configuration
Vite configuration can be found and modified in `frontend/vite.config.js`.

### Flask Configuration
Flask configuration can be found and modified in `backend/app/__init__.py`.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

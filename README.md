# Student Performance Indicator

## Project Overview

The Student Performance Indicator project is a data analysis and visualization tool designed to assess and predict student performance based on various attributes. This project aims to provide insights into factors affecting student performance and to identify potential areas for improvement.

## Table of Contents

- [Student Performance Indicator](#student-performance-indicator)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Installation](#installation)
  - [Usage:](#usage)
  - [Data](#data)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)
  - [Additional Information](#additional-information)
  - [Contact](#contact)

## Features

- **Data Analysis:** Analyzes student data to identify patterns and trends.
- **Visualization:** Provides visual representations of the data to facilitate understanding.
- **Prediction Model:** Implements a machine learning model to predict student performance based on input features.
- **Interactive Dashboard:** An interactive dashboard for exploring different aspects of student performance.

## Technologies Used

- **Python:** The primary programming language used for data analysis and model implementation.
- **Pandas:** For data manipulation and analysis.
- **NumPy:** For numerical computations.
- **Matplotlib:** For data visualization.
- **Seaborn:** For advanced data visualization.
- **Scikit-Learn:** For machine learning models and evaluation.
- **Jupyter Notebook:** For developing and testing code.
- **Flask:** For web-based interactive App.
- **Aws:** Deployment purpose.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AnoopGeorge418/Student-Performance-Indicator.git

2. **Navigate to the project directory:**
    ```bash
    cd Student-Performance-Indicator

3. **Create and activate a virtual environment:**
    ```bash
    conda create -p venv python==version_number -y
    activate venv/

4. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt

## Usage:

1. **Run Setup.py**
    ```bash
    python setup.py

2. **Run exception.py**
   ```bash
   python src/exception.py

3. **Run logger.py**
   ```bash
   python src/logger.py

4. **Run data_ingestion.py**
   ```bash
   python src/components/data_ingestion.py

5. **Run eda student performance.ipynb**
   ```bash
   Run it in jupyter notebook - shift + enter

6. **Run model training.ipynb**
   ```bash
   Run it in jupyter notebook - shift + enter

7. **Create a folder .ebextensions**
   ```bash
   Add a file - python.config
   for deployment purpose

8. **Launch the app:**
   ```bash
   python app.py

9.  **Open the web browser and go to:**
    ```bash
    http://localhost:5000


## Data
The project uses a dataset containing student information. The dataset includes attributes such as:

- Student ID
- Gender
- Age
- Parental Level of Education
- Lunch
- Test Preparation Course
- Math Score
- Reading Score
- Writing Score
**The dataset is available in the `notebook/data/`. Make sure to review the dataset and update the file path in the scripts if necessary.**

## Contributing
Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/YourFeature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/YourFeature).
5. Create a new Pull Request.
   
## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/AnoopGeorge418/Student-Performance-Indicator?tab=MIT-1-ov-file#) file for details.

## Acknowledgements
[Anoop George] - Project Author
[Any libraries, frameworks, or tools used] - Python, Git, Github, AWS
[Inspiration sources] - Youtube

## Additional Information
Project Structure
notebook/data/: Contains the dataset used for analysis.
notebook/ - contains eda and model training file
app.py: flask app.
requirements.txt: Lists the dependencies required for the project.
LICENSE: The license file for the project.

## Contact
**For any questions or feedback, please reach out to [Email](anoopgeorge418@gmail.com) or open an issue on the GitHub repository.**
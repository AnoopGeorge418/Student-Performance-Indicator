# **`Project WorkFlow Planning`:**

**1. Sett up `Github Repo` And link it with `Vscode`** 

**2. Create `Conda` Environment for the Project in Vscode and named it as `venv`(`conda create -p python==version -y`)**

**3. Set Up `Setup.py`**
    - Helps to create this project as a package and distribute the project, So others can install project in their system using pip (More like a library) 

**4. Set Up `Requirements.txt`** 
    - Contains all the libraries and pankages that needed to be installed for this project.
    - Install using `pip -r requirements.txt`.

**5. Create a `src` folder and `__init__.py`, `exception.py`, `logger.py`, `utils.py` files.**

**6. Create `component` folder inside `src` and `__init__.py - To add this to package`, `data_ingestion.py - To Load data and more`, `data_transformation.py`, `model trainer` all this files are for `Training` purpose.**

**7. Create `pipeline` folder inside `src` folder inside `train_pipeline.py`, `__init__.py`, `predict_pipeline.py`**


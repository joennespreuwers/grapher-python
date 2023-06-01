## Python Program Installation Guide

This guide provides step-by-step instructions for installing and running a Python program on your local machine. The installation process involves cloning a Git repository, installing the required dependencies, and running the `app.py`.

### Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your machine:

- Python (version 3.11)
- Git

### Installation Steps

1. **Clone the Git repository:**

   Open your terminal or command prompt and navigate to the directory where you want to clone the repository. Then, execute the following command to clone the repository:

   ```
   git clone https://github.com/joennespreuwers/grapher-python
   ```


2. **Install the required dependencies:**

   Change into the cloned directory by executing the following command:

   ```
   cd grapher-python
   ```

   Once you're in the correct directory, install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This command will use `pip`, the Python package installer, to install all the dependencies specified in the `requirements.txt` file.

3. **Run the Python program:**

   After installing the dependencies, you can now run the Python program. In the terminal or command prompt, execute the following command:

   ```
   python grapher-python/app.py
   ```

   This command will execute the `app.py` file, which is the entry point of the program.

Congratulations! You have successfully installed and executed the Python program on your local machine.

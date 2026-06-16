### Takosa App Demo

1. First create a virtual environment within the source directory.
    `python -m venv .venv`

2. Activate the virtual environment: `source .venv/bin/activate`

3. Install project dependencies: `pip3 install -r requirements.txt`
    a. You may need to install `openpyxl` separetly since that was not added in the requirements.txt file.
    b. Install openpyxl - `pip3 install openpyxl`

4. Save your two text files somewhere within the project folder. 
(I have a `src/input` folder where you can delete the sample data and add the data you wish to use)

5. Open a terminal and run the app, the format is as follows:
    a. `python src/main.py <file1path> <file2path> <output.xlsx>` or
    b. `python3 src/main.py <file1path> <file2path> <output.xlsx>`

    Here is the command I will be running for this demonstration:

    `python3 src/main.py src/input/access_points_sample2.txt src/input/access_points_sample3.txt output.xlsx`

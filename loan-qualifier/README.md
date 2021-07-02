# <a id="Top-of-Page">Here is the loan-qualifier project!</a>
***
## <a id="Contents">Cotents:</a>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
[Bottom of Page](#Bottom-of-Page)<br>
***
## <a id="Project-Description">Project Description</a>
This project provides automated calculations to identify qualifying loans.

#### A summary of what's under the hood:
We start with some fundamental calculations on a list of prices for given loans.
 - Using the loan qualifier command-line interface (CLI), when the qualifier is ran, the tool will prompt the user to save the results as a CSV file.
 - Using the list of qualifying loans, when prompted to save the results, the user can opt out of saving the file.
 - Using the list of qualifying loans, when the user chooses to save the loans, the tool will prompt for a file path to save the file.
 - Using the loan qualifier CLI, when the user chooses to save the loans, the tool will save the results as a CSV file.
 - If there are no qualifying loans, the qualifier program will notify the user and exit, given there is nothing to save.

#### Unit testing:
***
## <a id="Technologies">Technologies</a>
<a href="https://docs.python.org/release/3.7.10/"><img src="https://img.shields.io/badge/python-3.7.10%2B-green">
<a href="https://jupyter-notebook.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/jupyter--notebook-6.4.0-blue"></a>
<a href="https://github.com/google/python-fire"><img src="https://img.shields.io/badge/fire-0.4.0-red"></a>
<a href="https://github.com/tmbo/questionary"><img src="https://img.shields.io/badge/Questionary-1.9.0-red"></a>
<a href="https://docs.pytest.org/en/latest/"><img src="https://img.shields.io/badge/PyTest-0.0.0-orange"></a><br>
<a href="qualifier/requirements.txt" title="qualifier/requirements.txt">Requirements List</a>
***
## <a id="Installation-Guide">Installation Guide</a>
<a href="https://github.com/jasonjgarcia24/fintech-analytics-toolbox">fintech-analytics-toolbox</a> distribution in the works...<br>
    
<center><img src="https://media.giphy.com/media/k7LxZAzC9V70s/giphy.gif" /></center>

***
## <a id="Usage">Usage</a>
Run loan-analyzer with `python loan-qualifier.py`. No input variables are required, and the below image displays the expected terminal output:<br>
<center><img src="img/python_loan-qualifier.png" title="Terminal results of loan-qualifier.py" /></center><br>

The expected .csv output is shown below:<br>
<center><img src="img/loan-qualifier_output-csv.png" title="CSV results of loan-qualifier.py" /></center>

***
## <a id="Contributors">Contributors</a>
Currently just me :)<br>
***
## <a id="License">License</a>
Each file included in this repository is licensed under the <a href="https://github.com/jasonjgarcia24/fintech-analytics-toolbox/blob/main/LICENSE">MIT License.</a>
***
[Top of Page](#Top-of-Page)<br>
[Contents](#Contents)<br>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
<a id="Bottom-of-Page"></a>
# Here is the loan-qualifier project!<a id="Top-of-Page">
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
## Project Description<a id="Project-Description">
This project provides automated calculations to identify qualifying loans.

#### A summary of what's under the hood:
We start with some fundamental calculations on a list of prices for given loans.
 - Using the loan qualifier command-line interface (CLI), when the qualifier is ran, the tool will prompt the user to save the results as a CSV file.
 - Using the list of qualifying loans, when prompted to save the results, the user can opt out of saving the file.
 - Using the list of qualifying loans, when the user chooses to save the loans, the tool will prompt for a file path to save the file.
 - Using the loan qualifier CLI, when the user chooses to save the loans, the tool will save the results as a CSV file.
 - If there are no qualifying loans, the qualifier program will notify the user and exit, given there is nothing to save.

#### Unit testing:
Unit testing is performed on all modules contained within the loan-qualifier projectTo perform unit testing, at the root path run `pytest tests` or simply `pytest`.<br>
#### Project layout:
<p><a href="tree.txt"><img src="img/project_tree.png" title="loan-qualifier project tree"></a></p>

***
## Technologies<a id="Technologies">
<a href="https://docs.python.org/release/3.7.10/"><img src="https://img.shields.io/badge/python-3.7.10%2B-green">
<a href="https://jupyter-notebook.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/jupyter--notebook-6.4.0-blue"></a>
<a href="https://github.com/google/python-fire"><img src="https://img.shields.io/badge/fire-0.4.0-red"></a>
<a href="https://github.com/tmbo/questionary"><img src="https://img.shields.io/badge/Questionary-1.9.0-red"></a>
<a href="https://docs.pytest.org/en/latest/"><img src="https://img.shields.io/badge/PyTest-0.0.0-orange"></a><br>
<a href="requirements.txt" title="requirements.txt">Requirements List</a>
***
## Installation Guide<a id="Installation-Guide">
<a href="https://github.com/jasonjgarcia24/fintech-analytics-toolbox" title="github.com/jasonjgarcia24/fintech-analytics-toolbox">fintech-analytics-toolbox</a> distribution in the works...<br>
    
<center><img src="https://media.giphy.com/media/k7LxZAzC9V70s/giphy.gif" title="pink ice chest is best"/></center>

***
## Usage<a id="Usage">
Run loan-analyzer with `python app.py`. No input variables are required in calling loan-qualifier app, however user CLI inputs are required. The below image displays the expected terminal prompts with user inputs:<br>
<center><img src="img/appy_terminal_run_input.png" title="Terminal results of loan-qualifier.py" /></center><br>

The expected .csv output is shown below:<br>
<center><img src="img/appy_terminal_run_output.png" title="CSV results of loan-qualifier.py" /></center>

***
## Contributors<a id="Contributors">
Currently just me :)<br>
***
## License<a id="License">
Each file included in this repository is licensed under the <a href="https://github.com/jasonjgarcia24/fintech-analytics-toolbox/blob/main/LICENSE" title="github.com/jasonjgarcia24/fintech-analytics-toolbox/blob/main/LICENSE">MIT License.</a>
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
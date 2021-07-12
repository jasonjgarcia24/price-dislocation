# <a id="Top-of-Page">Welcome to the Price Dislocation Analysis Tool!</a>
#### An analysis of arbitrage profitability throughout two Bitcoin exchanges.
***
## <a id="Contents">Cotents</a>
[Project Description](#Project-Description)<br>
[Technologies](#Technologies)<br>
[Installation Guide](#Installation-Guide)<br>
[Usage](#Usage)<br>
[Contributors](#Contributors)<br>
[License](#License)<br>
[Bottom of Page](#Bottom-of-Page)<br>
***
## Project Description<a id="Project-Description">
This project models automated price dislocation calculations to identify arbitrage oppotunities between two Bitcoin exchanges.

#### A summary of what's under the hood:
Using Jupyter notebook, this tool sorts through historical trade data for Bitcoin on two exchanges: Bitstamp and Coinbase. By applying three phases of financial analysis, the tool will determine if any arbitrage opportunities exist for Bitcoin. The three phase include:
1. Collect the data.
2. Prepare the data.
3. Analyze the data.

#### Methods for identifying arbitrage opportunities:
The following is a generalized summary of this tool's functions for identifying arbitrage opportunities:
1. Measure the arbitrage spread between the two exchanges by subtracting the lower-priced exchange from the higher-priced one. Then generate the summary statistics for each arbitrage spread, where the spread is greater than zero.
2. Calculate the spread returns by dividing the instances that have a positive arbitrage spread (that is, a spread greater than zero) by the price of Bitcoin from the exchange we’re buying on (that is, the lower-priced exchange).
3. Determine the number of times the trades with positive returns exceed the 1% minimum threshold that you need to cover your costs.
4. Generate the summary statistics of the spread returns that are greater than 1%.
5. Calculate the potential profit, in dollars, per trade by multipling the spread returns that were greater than 1% by the cost of what was purchased.
    - We'll make sure to drop any missing values from the resulting DataFrame.
6. Generate the summary statistics and plot the results.
7. Calculate the potential arbitrage profits that can be made on each day.
8. Using the cumsum function, plot the cumulative sum.
    
#### Project layout:
The layout of essentials for this project is show below.
<p><a href="tree.txt"><img src="img/project_tree.png" title="price-dislocation project tree"></a></p>

***
## Technologies<a id="Technologies">
<a href="https://pandas.pydata.org/docs/" title="https://pandas.pydata.org/docs/"><img src="https://img.shields.io/badge/pandas-1.2.5-green"></a>
<a href="https://docs.python.org/release/3.7.10/" title="https://docs.python.org/release/3.7.10/"><img src="https://img.shields.io/badge/python-3.7.10%2B-green">
<a href="https://jupyter-notebook.readthedocs.io/en/stable/" title="https://jupyter-notebook.readthedocs.io/en/stable/"><img src="https://img.shields.io/badge/jupyter--notebook-6.4.0-red"></a><br>
<a href="requirements.txt" title="requirements.txt">Requirements List</a>
***
## Installation Guide<a id="Installation-Guide">
To install <a href="https://github.com/jasonjgarcia24/price-dislocation" title="github.com/jasonjgarcia24/price-dislocation">price-dislocation</a>, type <code>git clone https://github.com/jasonjgarcia24/price-dislocation.git</code> into bash in your prefered local directory.<br><br>
Alternatively, you can navigate to the same address (<code>https://github.com/jasonjgarcia24/price-dislocation.git</code>) and download the full <code>main</code> branch's contents as a zip file to your prefered local directory.<br>

***
## Usage<a id="Usage">
Observe price-dislocation with <code>crypto_arbitrage.ipynb</code>. No input variables are required.<br>

***
## Contributors<a id="Contributors">
Currently just me :)<br>
***
## License<a id="License">
Each file included in this repository is licensed under the <a href="https://github.com/jasonjgarcia24/price-dislocation/blob/main/LICENSE" title="github.com/jasonjgarcia24/price-dislocation/blob/main/LICENSE">MIT License.</a>
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
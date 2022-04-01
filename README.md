# Election Analysis
## Overview of Election Audit
This analysis was conducted in order to review the results of a county level election. This analysis was requested by the Election Commission to review and validate the election results. 

<ins>The specific requests by the Election Commission:
1. Find the total votes cast
2. Determine votes cast by county
3. Identify county with largest turnout
4. Determine votes cast for each candidate
5. Identify the winner of the election

### The Data
The data provided by the Election Commission was a .csv file containing all votes cast for the election. The data was organized by three headers: "Ballot ID," "County," and "Candidate."

A copy of the original data can be found [here.](https://github.com/sever1sd/election_analysis/blob/51d3ba5176f3b8d00dd99a16275cc9bcc104151d/Resources/election_results.csv)

### The Analysis
The analysis was performed using a script using the programming language Python and the code editing program Visual Studio Code. The script was designed to aggregate votes by candidate and county. Then it determined the winner by identifying candidate had the most votes.

#### <ins>Script Breakdown

Initializing Variables:

Counting Votes:

Determining County Winner:

Determining Candidate Winner:

Code Output:

A copy of the script can be found [here.](https://github.com/sever1sd/election_analysis/blob/51d3ba5176f3b8d00dd99a16275cc9bcc104151d/PyPoll_Challenge.py)

## Election-Audit Results
The final talley of the election results were written onto a text file and saved [here.](https://github.com/sever1sd/election_analysis/blob/51d3ba5176f3b8d00dd99a16275cc9bcc104151d/analysis/election_analysis.txt) 

<ins>**A summary of the results is as follows:**

<ins>Election Results:
* Total Votes: 369,711
* Winning Candidate: Diana DeGette
    * Winning Number of votes: 272,892
    * Winning Percentage: 73.8%
* Largest County Turnout: Denver County
    * Denver Number of Votes: 306,055
    * Denver Percentage of Total: 82.8%

<ins>Additional Election Information
* Other Candidates:
    * Second Place: Charles Casper Stockham
        * Vote Count: 85,213
        * Vote Percentage: 23.0%
    * Third Place: Raymon Anthon Doane
        * Vote Count: 11,606
        * Vote Percentage: 3.1%
* Other Counties:
    * Second Highest Turnout: Jefferson
        * Vote Count: 38,855
        * Vote Percentage: 10.5%
    * Lowest Turnout: Arapahoe
        * Vote Count: 24,801
        * Vote Percentage: 6.7%

<ins>**A screenshot of the text file output:**
![alt text]()

## Audit Summary
This script was beneficial in auditing the local election because it was able to quickly and reliably aggregate and analyze the data. Due to the speed and accuracy of this audit, it is recommended that future election audits be conducted similarly. The script utilized for this audit can also be used in future election audits with minor modifications or expanded for more robust analyses.

Some general modifications that to be considered for expanding the analysis could be including an analysis of the number of votes for each candidate per county. This will allow for identifying trends and understand the impact of population size per county. Inversely, identifying number of votes for each candidate in a given county would assess their popularity for each county.

Some modifications to the code for use in future analysis should be updating the directory pathing for the data sources. This is necessary for the script to call to the correct information. Additionally, if more candidates or counties were included in the election, then the script would need to be updated to accommodate for the additional candidates and counties. This primarily would need to occur where results are written to text files or printed to the terminal. 

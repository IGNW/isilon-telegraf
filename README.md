# Repo Status
Isilon API Status

![Isilon API Testing](https://github.com/IGNW/isilon-telegraf/workflows/Isilon%20API%20Testing/badge.svg)

# isilon-telegraf
Repo for testing out Isolon-Telegraf integration using the Isolon SDK

# Requires Python 3.6.x
In Python 3.7 and later, the Python language added the **async** keyword.  In the Isilon Python Library has a variable called **async**.

This causes issues.  It would be an easy fix, but nobody has updated the code that generates the API code since 2017.

If newer Python is needed, manually patching the library after importing would be required.

# Helper Files
## Dumping all the Statistics Keys to CSV
The Isilon documentation for all the statistics keys does not exist.  This tool dumps out all the key names and the key descriptions into a CSV.  If you upload that to GitHub, you git a nice little chart with the ability to filter data.  The `write_all_nfs_stat_descriptions_to_csv.py` file does this.  Look at the `nfs_stats.csv` file in this repo for the list as of April 2020.

## Displaying the Contents of a Key
After having a list of stats, would be nice to easily look at the contents.  Use the `stats_explorer.py` command line tool.  Some examples of using the command are:
- python3 stats_explorer.py -h
- python3 stats_explorer.py cluster.node.count.all

Just add the a Statistics Key name after the end of the file and it will output the api data to the command line.  This tool is for helping to explore the Statistics API while developing a program.


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


# Adding an API/Status Only User
This is a 2 part process.

## Create User
- Log into the Isilon as an admin.
- Navigate to Access -> Membership and Roles -> Users
- Select `LOCAL: System`from the Providers Drop Down
- Click `Create user` on the right of the window
- Fill out with the following values in the pop up window
    - User name: ro_api_user
    - Password: ***desired_password***
    - Full Name: RO API User
    - Enable the account: ***checked***
- Click `Create user` at the bottom of the window

## Add to correct role
- Click on the `Roles` tab
- Scroll down to `StatisticsAdmin` and click the `View/Edit` button
- In the pop up window click `Edit role`
- Click `Add a member to this role`
- Select `LOCAL:System` from the Provider drop down
- Select the `Search` button
- Select `ro_api_user` from the Search Results section
- Click `Select` to add the user to the role
- Click `Save changes`
- Click `Close`

Now test and verify your new user can pull Stats from the API but cannot log into the GUI.
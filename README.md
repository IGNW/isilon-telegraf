# Repo Status
Isilon API Status

![Isilon API Testing](https://github.com/IGNW/isilon-telegraf/workflows/Isilon%20API%20Testing/badge.svg)

# isilon-telegraf
Repo for testing out Isolon-Telegraf integration using the Isolon SDK

# Requires Python 3.6.x
In Python 3.7 and later, the Python language added the **async** keyword.  In the Isilon Python Library has a variable called **async**.

This causes issues.  It would be an easy fix, but nobody has updated the code that generates the API code since 2017.

If newer Python is needed, manually patching the library after importing would be required.


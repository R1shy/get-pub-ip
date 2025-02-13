# Get Pub IP

This is a python script for getting your public IP (using the ipify API) and emailing it to yourself.

# Why does this exist?

Because I don't want to set a static IP for my rasberry pi and I don't want to pay for a DNS.

# Isn't this malware technically?

## NUH UH.

# How do I use this?

- have: python and a wifi connection, maybe a gmail account
    - this runs on 3.13 I don't want to test for earlier
- clone the repo using 
``` git clone htttps://github.com/R1shy/get-pub-ip ```

- run ``` pip install -r requirements.txt```
- make a file called ``` special_vars.py ```
add a variable for:
    - the sending email
    - the recieving email
    - the app password (google how to get it)

- with the file made run the script with py(thon)(3) depending on your os
- most linux distros use python
- mac uses python3
- windows uses py

# REALLY IMPORTANT NOTE:

IF YOUR ON LINUX REMEMBER TO USE A VENV


# License

Please don't use this for malware :)

# Thanks:
- the people who made the ipify API
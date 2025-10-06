# Get Pub IP

This is a python script for getting your public IP (using the ipify API) and emailing it to yourself.

# Why does this exist?

Because I don't want to set a static IP for my rasberry pi and I don't want to pay for a DNS.



# How do I use this?

- have: python and a internet (wifi or ethernet) connection, maybe a gmail account

clone the repo using

```bash
git clone https://github.com/R1shy/get-pub-ip
```

go into the dir 
```bash
cd get-pub-ip
```

get deps (you need uv)
```bash
uv sync
```

then either use:
```bash
uv run main.py # use locally
```
or
```bash
docker compose -f docker-compose.yml up # use -d if you want it to be containerized
```


# Thanks:
- the people who made the ipify API

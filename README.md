# DDoS Attack Script

## Description
This script is designed to perform a DDoS attack by sending a high number of HTTP requests to a target URL. It utilizes multiple IP addresses and multiprocessing to increase the intensity of the attack.

## Author
[joshua Apostol]

## proof:

![Alt text](https://i.imgur.com/motFzn6.jpeg)

![Alt text](https://i.imgur.com/kJDQOfr.jpeg)

## Configuration
- **total_requests**: Total number of requests to be sent.
- **requests_per_second**: Number of requests per second.
- **num_ip_addresses**: Number of IP addresses to use.
- **target_url**: The target URL for the attack.

## Usage
1. Update the `config.py` file with the desired configuration.
2. Run the `DDoS.py` script:

## Instructions
1. **Save each script** in separate files as indicated above.
2. **Update the `target_url`** in `config.py` with the actual URL you want to test.
3. **Run the main script** using `python DDoS.py`.

This structure separates configuration, main logic, and helper functions, making the code more modular and easier to manage. Remember to use this script responsibly and legally. Unauthorized use can lead to severe legal consequences.


```sh
python DDoS.py



how to run?
use a: https://shell.cloud.google.com/?hl=en_US&fromcloudshell=true&show=terminal

or

https://replit.com/

but the best you wan't to run this use Codespace

install:

python3 -m pip install aiohttp

git clone https://github.com/Justerw/DDoS

cd DDoS

python3 DDoS.py

# speed_test 1.0
Simple speed testing tool relying on "speedtest.net" python-cli

## Usage
either manually configure script output path, time interval between subsequent tests
OR
run the GUI script which interface the test script easily and offers easier way to set the output path, time interval

### Output would be to a .txt file :
```
Date:

2016-07-03 13:35:02.885000

Speed test:

Retrieving speedtest.net configuration...

Retrieving speedtest.net server list...

Testing from Etisalat (86.97.84.164)...

Selecting best server based on latency...

Hosted by Boomerang Rayaneh (Kish) [203.83 km]: 234.404 ms

Testing download speed........................................

Download: 0.09 Mbit/s

Testing upload speed..................................................

Upload: 0.00 Mbit/s


Date:

2016-07-03 13:41:44.081000

Speed test:

Retrieving speedtest.net configuration...

Retrieving speedtest.net server list...

Testing from Etisalat (86.97.84.164)...

Selecting best server based on latency...

Hosted by du (Dubai) [8.65 km]: 67.538 ms

Testing download speed........................................

Download: 0.09 Mbit/s

Testing upload speed..................................................

Upload: 0.00 Mbit/s



```

### Note:
_I have used python 2.7.x on windows os_

speedtest-cli package is *required* to be installed on the system:

```
>>> pip install speedtest-cli
```

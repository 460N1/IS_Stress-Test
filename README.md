# Internet Security - Stress Testing DOS Tool

<img src="https://img.shields.io/badge/author-Agon%20Hoxha-red.svg"> <img src="https://img.shields.io/github/license/460N1/IS_SulmimDOS.svg">  [![](https://img.shields.io/github/release-date/460N1/IS_SulmimDOS.svg)](https://github.com/460N1/IS_SulmimDOS/)  ![](https://img.shields.io/github/release/460N1/IS_SulmimDOS.svg)  ![Size](https://github-size-badge.herokuapp.com/460N1/IS_SulmimDOS.svg) <a href="https://github.com/460N1/IS_SulmimDOS/tree/Shqip"><img src="https://img.shields.io/badge/langauge-change-black.svg"></a>

This was a task in Internet Security for creating a tool which allows site stress testing.

You can use it freely, as long as it's not misuse.

RawCap.exe has other use conditions (https://www.netresec.com/?page=RawCap).

```
usage: ISSulm.py [-h] [-p PORT] [-s SOCKETS] [-d] [-r] [-q] [--https] [host]

  host                              Host which we will stress test.
  -h, --help                        Shows these instructions.
  -p PORT, --port PORT              Target port (default 80).
  -s SOCKETS, --sockets SOCKETS     Number of sockets to be used (default 100).
  
  -d, --detaje                      Shows more information during execution (verbose).
  -q, --qete                        Doesn't show anything during execution.
  -r, --random-ua                   Uses random user-agent.
  --https                           Uses HTTPS for requests.

```

***

Included is also a .bat file which will start the attack, and start packet capture at the same time. It also opens the packet capture (.pcap) file as soon as packet capture ends.

Everything can be edited. In the batch file, getintopc.com is the target, you can replace it with any site you want, and add arguments based on the usage of ISAttack.py above.

Special attention must be paid to RawCap.exe. In the batch script, the number 4 represents the interface which was used during development.

For you, this will probably be different. To know which number you should use, just execute RawCap.exe and remember the number of the interface you wish to use, and replace it in the batch file.

***

If this file is spread among other hosts, and executed at the same time, it can simulate a DDoS attach. Not a thing I recommend to do, just mentioning that it could be done.

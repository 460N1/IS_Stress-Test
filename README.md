# Internet Security - Stress Testing DoS Tool <a href="#"><img src="https://www.freeiconspng.com/uploads/us-flag-icon-6.png" width=30 height=30></a> <a href="https://github.com/460N1/IS_SulmimDOS/tree/Shqip"><img src="https://cdn3.iconfinder.com/data/icons/finalflags/256/Albania-Flag.png" width=30 height=30></a>

[![](https://img.shields.io/badge/author-Agon%20Hoxha-red.svg)](https://www.github.com/460N1/)
[![](https://img.shields.io/github/license/460N1/IS_Stress-Test.svg?kill_cache=1)](https://github.com/460N1/IS_SulmimDOS/blob/master/LICENSE)
[![](https://img.shields.io/github/release-date/460N1/IS_Stress-Test.svg?kill_cache=1)](https://github.com/460N1/IS_SulmimDOS/releases)
[![](https://img.shields.io/github/release/460N1/IS_Stress-Test.svg?kill_cache=1)](https://github.com/460N1/IS_SulmimDOS/archive/0.94.zip)
[![](https://img.badgesize.io/460N1/IS_Stress-Test/master/IS_SulmimDOS/ISStress.py.svg?kill_cache=1)](https://github.com/460N1/IS_SulmimDOS/blob/master/IS_SulmimDOS/ISStress.py)

This was a task in Internet Security for creating a tool which allows site stress testing.

You can do anything you want with these files, but MIT license applies.

RawCap.exe has other use conditions (https://www.netresec.com/?page=RawCap).

```
usage: ISAttack.py [-h] [-p PORT] [-s SOCKETS] [-d] [-r] [-q] [--https] [host]

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

If this file is spread among other hosts, edited a little bit and executed at the same time, it can simulate a DDoS attack. That's not something I recommend doing, just thinking out loud.

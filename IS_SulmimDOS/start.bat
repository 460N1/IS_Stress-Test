@ECHO OFF

REM /**************************\
REM |   ---  Agon Hoxha ---    |
REM |  Python application for  |
REM |     site stress test     |
REM \**************************/

	START cmd /c python ISStress.py getintopc.com -q

REM --- Creating new concurrent process.
REM --- For help, execute ISAttack.py --help from cmd.

	RawCap.exe 4 Proof.pcap

REM --- Decides the network interface which RawCap.exe will sniff.
REM --- For you, this command might be different.
REM --- Decides the packet capture file name.

	START Proof.pcap

REM --- Opens the file to show the captured packets.
REM --- Just to make sure that everything is working.

EXIT
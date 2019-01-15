@ECHO OFF

REM --- /****************************************************\
REM --- |         AUTHOR:  Agon Hoxha,  140704110004         |
REM --- |    SUBJECT: Internet Security,  VITI: 2018/2019    |
REM --- |    TASK: Developing Python application for site    |
REM --- |                stress testing,   #6                |
REM --- \****************************************************/

	START cmd /c python ISStress.py getintopc.com -q

REM --- Creating new concurrent process.
REM --- Calling Python script and setting target.
REM --- Using quiet mode (tool shows no output).
REM --- For help, execute ISAttack.py --help from cmd.

	RawCap.exe 4 Proof.pcap

REM --- Decides the network interface which RawCap.exe will sniff.
REM --- For you, this command might be different.
REM --- Decides the packet capture file name.

	START Proof.pcap

REM --- Opens the file to show the captured packets.
REM --- Last two commands are not needed for the tool,
REM --- just to make sure that everything is working.

EXIT
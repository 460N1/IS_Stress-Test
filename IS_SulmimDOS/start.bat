@ECHO OFF

REM /**************************\
REM |   ---  Agon Hoxha  ---   |
REM |  Python aplikacion, per  |
REM |    site stres testim.    |
REM \**************************/

	START cmd /c python ISStress.py getintopc.com -q

REM Per ndihme, ekzekuto sulmo.py --help nga cmd.

	RawCap.exe 4 Vertetimi.pcap

REM Percakton network interface qe do t'e sniff RawCap.exe
REM Ne nje host tjeter, kjo do mund te jete ndryshe.
REM Percakton emrin e file ku ruhen paketat e derguara.

	START Vertetimi.pcap

REM Ekzekutojme file qe te shohim paketat qe kemi derguar.
REM Vetem pre t'e testuar se a eshte duke funksionuar.

EXIT
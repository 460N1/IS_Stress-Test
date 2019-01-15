@ECHO OFF

REM --- /************************************************\
REM --- |       AUTORI:  Agon Hoxha,  140704110004       |
REM --- |  LENDA: Siguria ne Internet,  VITI: 2018/2019  |
REM --- |  DETYRA:  Zhvillim i aplikacionit qe mundeson  |
REM --- |  stress testing te nje sajti te caktuar,   #6  |
REM --- \************************************************/

	START cmd /c python ISStress.py getintopc.com -q

REM --- Krijojme proces te ri.
REM --- Thirret skripta e python dhe percaktohet caku.
REM --- Perdorim mode te qete (pa shfaq tekst).
REM --- Per ndihme, ekzekuto sulmo.py --help nga cmd.

	RawCap.exe 4 Vertetimi.pcap

REM --- Percakton network interface qe do t'e sniff RawCap.exe
REM --- Ne nje host tjeter, kjo do mund te jete ndryshe.
REM --- Percakton emrin e file ku ruhen paketat e derguara.

	START Vertetimi.pcap

REM --- Ekzekutojme file qe te shohim paketat qe kemi derguar.
REM --- Aspak e nevojshme, vetem te vertetojme se a kemi qene
REM --- duke derguar paketa apo jo.

EXIT
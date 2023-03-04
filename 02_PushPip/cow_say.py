import cowsay
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", action="store_true")
parser.add_argument("-e")
parser.add_argument("-f")
parser.add_argument("-W", type=int)
parser.add_argument("-T")
parser.add_argument("message", action="store", default="", nargs="?")
parser.add_argument("state", choices=["-b", "-d", "-g", "-p", "-s", "-t", "-w", "-y"])
params = parser.parse_args()
print(params)
"""if (params.l == True and params.message == ""):
    print(cowsay.list_cows())
else:
    print(cowsay())"""

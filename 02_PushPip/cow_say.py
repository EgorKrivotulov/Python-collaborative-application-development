import cowsay
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-l", action="store_true")
parser.add_argument("-e", default="oo")
parser.add_argument("-f", default="default")
parser.add_argument("-n", action="store_false")
parser.add_argument("-W", type=int, default=40)
parser.add_argument("-T", default="  ")
parser.add_argument("-t", dest="state", action="append_const", const="t", default=[""], required=False)
parser.add_argument("-b", dest="state", action="append_const", const="b", default=[""], required=False)
parser.add_argument("-d", dest="state", action="append_const", const="d", default=[""], required=False)
parser.add_argument("-p", dest="state", action="append_const", const="p", default=[""], required=False)
parser.add_argument("-g", dest="state", action="append_const", const="g", default=[""], required=False)
parser.add_argument("-s", dest="state", action="append_const", const="s", default=[""], required=False)
parser.add_argument("-w", dest="state", action="append_const", const="w", default=[""], required=False)
parser.add_argument("-y", dest="state", action="append_const", const="y", default=[""], required=False)
parser.add_argument("message", action="store", default="", nargs="?")
params = parser.parse_args()
print(params)
if (params.l == True and params.message == ""):
    print(cowsay.list_cows())
else:
    print(cowsay.cowsay(params.message,
                        cow=params.f,
                        preset=max(params.state),
                        eyes=params.e,
                        tongue=params.T,
                        width=params.W,
                        wrap_text=params.n))

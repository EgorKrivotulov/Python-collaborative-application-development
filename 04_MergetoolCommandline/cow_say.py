import cmd
import cowsay
import shlex
class mycmd(cmd.Cmd):
    intro = "How and what should We say?"
    prompt = "<>: "

    def do_exit(self, arg):
        'End command line'
        return 1
    def do_cowsay(self, arg):
        args = cow_parse(shlex.split(arg))
        print(cowsay.cowsay(message=args['message'], eyes=args['-e'], tongue=args['-T'], cow=args['-f']))
    def do_list_cows(self, arg):
        print(cowsay.list_cows())
    def do_make_bubble(self, arg):
        print(cowsay.make_bubble(shlex.split(arg)[0]))
    def do_cowthink(self, arg):
        args = cow_parse(shlex.split(arg))
        print(cowsay.cowthink(message=args['message'], eyes=args['-e'], tongue=args['-T'], cow=args['-f']))

def cow_parse(tokens):
    args = {'-f':'default', 'message':'', '-e':'oo', '-T':'  '}
    used_tokens = set()
    for i in range(0, len(tokens)-1):
        print(tokens[i], tokens[i] in args.keys())
        if tokens[i] in args.keys() and tokens[i] != 'message':
            args[tokens[i]] = tokens[i+1]
            used_tokens.add(tokens[i])
            used_tokens.add(tokens[i+1])

    texts = list(set(tokens).difference(used_tokens))
    if len(texts) == 0:
        texts[0] = ''
    if len (texts) != 1:
        print("WARNING: Can't choose from that options for message:")
        print(texts)
    for i in tokens:
        if i in texts:
            args['message'] = i
            break
    return(args)
def bubble_parse(tokens):
    args = {'l':'<', 'r':'>'}
    used_tokens = set()
    for i in range(0, len(tokens)-1):
        print(tokens[i], tokens[i] in args.keys())
        if tokens[i] in args.keys() and tokens[i] != 'message':
            args[tokens[i]] = tokens[i+1]
            used_tokens.add(tokens[i])
            used_tokens.add(tokens[i+1])

    texts = list(set(tokens).difference(used_tokens))
    if len(texts) == 0:
        texts[0] = ''
    if len (texts) != 1:
        print("WARNING: Can't choose from that options for message:")
        print(texts)
    for i in tokens:
        if i in texts:
            args['message'] = i
            break
    return(args)
            

if __name__ == "__main__":
    mycmd().cmdloop()

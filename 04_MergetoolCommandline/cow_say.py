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
        print(arg)
        print(shlex.split(arg))
        print(cowsay.cowsay(shlex.split(arg)[0]))
    def do_list_cows(self, arg):
        print(cowsay.list_cows())
    def do_make_bubble(self, arg):
        print(cowsay.make_bubble(shlex.split(arg)[0]))
    def do_cowthink(self, arg):
        print(cowsay.cowthink(shlex.split(arg)[0]))
if __name__ == "__main__":
    mycmd().cmdloop()

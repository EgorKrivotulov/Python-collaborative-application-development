import cmd
import cowsay

class mycmd(cmd.Cmd):
    intro = "How and what should We say?"
    prompt = "<>: "

    def do_exit(self, arg):
        'End command line'
        return 1
if __name__ == "__main__":
    mycmd().cmdloop()

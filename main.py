import sys, os, random, string
from writer import *

def IP(ip):

    values = ip.split('.')

    if int(values[0]) < 0 or int(values[0]) > 255: return False
    if int(values[1]) < 0 or int(values[1]) > 255: return False
    if int(values[2]) < 0 or int(values[2]) > 255: return False
    if int(values[3]) < 0 or int(values[3]) > 255: return False

    return True

 #Flag, Value
    # -i IP value
    # -h Hostname
    # -p Path - None, use default location
    # -f FolderName
def main():
    args = {}
    lenArgs = len(sys.argv)
    if (lenArgs > 1 and '--h' == sys.argv[1]):
        print("Help:")
        print("-i IP Address of format iPv4 only xxx.xxx.xxx.xxx")
        print("-h Hostname for project file and IP mask")
        print("-p Path to write project folder")
        print("-f Name of project folder")
        exit(0)

    #Check for flags
    for flag in range(1, lenArgs, 2):
        args[sys.argv[flag]] = sys.argv[flag + 1]

    # -i - IP generation
    if('-i' in args.keys()):
        if not IP(args['-i']):
            print("Invalid IP Address format.")
    else:
        gen = (input("No IP flag found, generate unique IP? y/n? ").lower() == 'y')
        if(not gen):
            exit(0)
        args['-i'] = "192." + str(random.randint(1,255)) + "." + str(random.randint(1,255)) + "." + str(random.randint(1,255))

    # -h - Hostname
    if ('-h' not in args.keys()):
        hostname = input("No Hostname found, input host name: ")
        args['-h'] = hostname

    # -p - Filepath
    if('-p' not in args.keys()):
        gen = (input("File path not found, generate using $HOME/Desktop? y/n? ").lower() == 'y')
        if (not gen):
            exit(0)
        args['-p'] = os.environ['HOME'] + "/Desktop/"

    else:
        path = ""
        if(os.path.exists(args['-p'])):
            if args['-p'][-1] != '/':
                args['-p'] += '/'
        else:
            print("Invalid file path for '-p'.  Exiting...")
            exit(0)

    # -f - Folder name
    if('-f' not in args.keys()):
        foldername = input("No folder name found, input folder name: ")
        args['-f'] = foldername


    #End parameter checks
    print("Generating folders...")
    writeFiles(args)

    #Dump completed IP and hostname, inform about installing hostnames
    #Do you want to include a README and .gitignore file??
main()
import os
import shutil

def writeFiles(args):

    #Folder structure for generation
    structure = { args['-f']: ["config", args['-h']],
                  "config": [],
                  args['-h'] : ["classes", "view"],
                 "view" : ["css", "js", "img"],
                 "classes" : []}

    #Writes files once the Directories are initialized
    files = {"config": ["bootstrap.sh", "site.conf"],
             args['-h']: ["load.php"],
             "classes": ["Database.php", "Session.php"],
             "view": ["index.php"],
             args['-f']: ["Vagrantfile"],
             }

    #Folder name gathered from CLI arguments
    folder = args['-p'] + args['-f'] + "/"

    #Paths of the folders and files
    path = {"config" : folder,
            args['-h'] : folder,
            "view" : folder  + args['-h'] + "/",
            "classes" : folder + args['-h'] + "/",
            args['-f'] : args['-p']}


    print("Creating", folder, "file structure")
    os.mkdir(folder, 0o777)
    writeCustomFiles(args['-i'], args['-h'])

    for key in structure.keys():
        print("------------ " + key + " -------------")
        for item in structure[key]:
            print(path[key] + key + "/" + item)
            os.mkdir((path[key] + key + "/" + item), 0o777)


        for file in files[key]:
            print(path[key] + key + "/" + file)
            shutil.copyfile(("files/"+file),path[key] + key + "/" + file)
    print("\n")

    if(input("Do you want to include a README.md y/n? ").lower() == 'y'):
        print("Writing README.md...")
        f = open(folder + "README.md", "w")
        f.write(" ")
        f.close()
    if (input("Do you want to include a .gitignore y/n? ").lower() == 'y'):
        print("Writing .gitignore...")
        f = open(folder + ".gitignore", "w")
        f.write(" ")
        f.close()

    print("Finished successfully...")
    print("Access with IP " + args['-i'])
    print("Hostname " + args['-h'])

def writeCustomFiles(IP, host):

    Vagrantfile = "Vagrant.configure(2) do |config|\n" \
                "\tconfig.vm.synced_folder '.', '/vagrant', disabled: true\n" \
                "\tconfig.vm.box = \"debian/contrib-jessie64\"\n" \
                "\tconfig.vm.network \"private_network\", ip: \"" + IP + "\"\n"\
                "\tconfig.vm.hostname = \""+ host +".dev\"\n" \
                "\tconfig.hostsupdater.aliases = [\""+ host +".dev\"]\n" \
                "\tconfig.vm.synced_folder \"./"+ host +"/\", \"/srv/"+ host +"\", create: true\n" \
                "\tconfig.vm.synced_folder \"./config/\", \"/var/config_files\", create: true\n" \
                "\tconfig.vm.provision :shell, path: \"./config/bootstrap.sh\"\n" \
                "\tconfig.vm.provider \"virtualbox\" do |vb|\n" \
                "\t\tvb.memory = \"1024\"\n" \
                "\tend\n" \
                "end"

    Site = "<VirtualHost _default_:80>\n" \
            "\tServerName "+ host +".dev\n"\
            "\tServerAdmin webmaster@localhost\n"\
            "\tDocumentRoot /srv/"+host+"/view\n"\
            "\t<Directory /srv/"+host+"/view>\n"\
                "\t\tRequire all granted\n"\
                "\t\tAllowOverride all\n"\
            "\t</Directory>\n"\
            "\tErrorLog ${APACHE_LOG_DIR}/error.log\n"\
            "\tCustomLog ${APACHE_LOG_DIR}/access.log combined\n"\
            "</VirtualHost>"

    print("Writing site.conf into config/...")
    f = open("files/site.conf", "w")
    f.write(Site)
    f.close()

    print("Writing Vagrantfile in root folder...")
    f = open("files/Vagrantfile", "w")
    f.write(Vagrantfile)
    f.close()
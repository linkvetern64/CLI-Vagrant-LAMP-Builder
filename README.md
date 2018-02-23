# CLI-Vagrant-LAMP-Builder

Command line LAMP and Vagrant Project Builder
-
This CLI allows you to build and generate Vagrant and config files for LAMP stacks.

Prerequisites
-
* Oracle Virtualbox - https://www.virtualbox.org/wiki/Downloads
* (Windows only) GitBash - https://git-scm.com/downloads
* Vagrant -     https://www.vagrantup.com/downloads.html
* Vagrant Plugins
* GitHub - https://github.com

    (These links we're the most recent versions as of 9/30/2017)
    If you're unfamiliar with the Git tools.  A handy learning tool is available here.
    https://try.github.io/levels/1/challenges/1

Installation
-
* VirtualBox

    <b>NOTE</b> before installing <u>Virtualbox</u>.  Enable virtualization within your BIOS or OS.
    Installing virtualbox should be straight forward.

* GitBash

    GitBash client is only necessary for Windows users.  If you are on a Mac or Linux device you can skip
    this step.  Otherwise navigate through the link above.  The steps as well should be pretty straight forward.
    <b>Note: </b> On windows you may encounter issues with GitBash unless you operate as Administrator.
    This can be achieved by right-clicking on the program before running and hitting
    "Run as Administrator".

* Vagrant

    Again, installation should be rather straight forward.  However all machines are different so pay attention
    as you install in case any errors should occur.

* GitHub

    Most importantly having a github account will be the means of cloning and allowing you to
    use this project.
    On the website, create an account.  This will be essential for being able to clone and use the code.

    In the GitBash you will want to now clone this repository.  You can achieve that by running the command:

        "git clone git@github.com:linkvetern64/asymmetrik-bcr.git" for ssh
        "git clone https://github.com/linkvetern64/asymmetrik-bcr.git" for https


* Vagrant Plugins

    Once you have Vagrant and GitBash installed.  Open the GitBash CLI and type in

        "vagrant plugin install vagrant-hostsupdater"
        "vagrant plugin install vagrant-hostmanager"

    -- hostsupdater is at (version. 1.0.2) as of 9/30/2017

    -- hostmanager is at (version. 1.8.7) as of 9/30/2017

Executing
-
Now that we have all the dependencies installed.  through the GitBash or CLI enter the cloned git-repo
you cloned above.

This can be accomplished using the "cd" command.  Once you enter the folder, you should now be able to run

    "vagrant up"

If this does not work.  Make sure you see a file called Vagrantfile.  This file is how vagrant knows how to initialize itself.
now wait until Vagrant finishes filling up the terminal with output.

you can now open up your web browser and in the navigation bar enter "<b>[HOSTNAME]</b>.dev".
This will take you to the local server Vagrant initialized with the git project loaded.

In order to turn off the Vagrant VM and shutdown the server simply run.

    "vagrant destroy"


How to Operate
-

To run the program, type
    
    python3 main.py [parameters]
    
Parameter flags are:

<b>-i</b> : Specific iPv4 address for vagrant to host on

<b>-h</b> : Host folder name, where web application lives

<b>-p</b> : Specific path to write project structure

<b>-f</b> : project structure folder name


If any of the required flags are missing, the CLI will prompt you for the information.

The folder structure is written to your -p path or it will use $HOME/Desktop.

An example input will look like:

    python3 main.py -i 192.168.1.200 -h App -p /Users/user/Desktop -f ProjectOne
    
The order of the flags does not matter.



Future Updates
-
Custom latest library installs, i.e. (Do you want to include bootstrap4, JQuery, etc..)
Import library list and build libraries for project and write them to index

Known Bugs / Fixes
-
Content unavailable.

Authors
-
Joshua Standiford





This is wordpress password bruter v1.0 (no threading yet, but give me some time and I'll try to safely implement it).

Any comments, ideas and improvements are more than welcome so send me a message and I`m sure going to listen ;D


##### HELP #####

[+] Wordpress Password Bruteforcer by op7ic
[+] contact : op7ica@gmail.com
Usage:
    This tool will attempt to get you an access to wordpress 

    To crack single password for a user:
    options: -d <dict> -u <user> -t <target>
    To crack passwords for multiple users:
    options: -d <dict> -U <user dict> -t <target>
     
    example:
    -d /tmp/passwords.txt -U /tmp/users.txt -t http://127.0.0.1
   
Options:
  -h, --help            show this help message and exit
  -d FILE, --dictionary=FILE
                        Password dictionary to use
  -U FILE, --usernames=FILE
                        Username dictionary to use
  -v, --verbose         Be Verbose
  -u USERNAME, --username=USERNAME
                        Username to check the passwords against
  -t TARGET, --target=TARGET
                        Target to assess
                        
                        

This is wordpress password bruter v1.0 (no threading yet, but give me some time and I'll try to safely implement it).

Any comments, ideas and improvements are more than welcome so send me a message and I`m sure going to listen ;D



Help
========

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
                        
                        
                        
License
========
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.                        
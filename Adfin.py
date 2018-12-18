from urllib2 import Request, urlopen, URLError, HTTPError
def Space(j):
        i = 0
        while i<=j:
                print " ",
                i+=1
print "\033[31m      ____    _____  __  _____"
print "\033[31m     |  _ \\  | ____| \  \/  //"
print "\033[31m     | || || | |___   \    //"
print "\033[00m     | || || |  ___|  /    \\"
print "\033[00m     | ||_|| | |___  / // \ \\"
print "\033[00m     |____|| |____/ /_//  /_//"
print " "
print "\033[31m_" * 51
print "\033[00m_" * 51
print " "
print "\033[33mAuthor : @P4R45173_51573M"
print "\033[33mTeam   : [ D4RK_EXPLOITER ]"
print "\033[33mTools  : AdminFinder"
print "\033[33mTanks  : NighCore , root@Wahyudi_kun"
print " "
print "\033[31m_" * 51
print "\033[00m_" * 51

def miminEA():
        f = open("Kon.txt","r");
        print (" ")
        print("\033[31m(ex webnya : bokep.com atau www.bokep.com ) \033[31m")
        print "\033[00m"
        link = raw_input("D4RK_EXPLOITER@root : ")
	print "\033[92m \n\nlink admin : \n"
        while True:
                sub_link = f.readline()
                if not sub_link:
                        break
                req_link = "http://"+link+"/"+sub_link
                req = Request(req_link)
                try:
                        response = urlopen(req)
                except HTTPError as e:
                        continue
                except URLError as e:
                        continue
                else:
                        print "OK => ",req_link

miminEA()

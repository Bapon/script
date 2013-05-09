import subprocess
def main():
    #print"hopo"
    #subprocess.call("pwd")
    #print "mysql"
    #subprocess.call(["zypper", "install", "mysql-community-server"])
    #subprocess.call("reboot")
    #subprocess.call(["systemctl", "enable", "mysql.service"])
    #subprocess.call(["systemctl","start", "mysql.service"])
    subprocess.call("mysql_secure_installation")
if __name__ == "__main__":
   main()  
   

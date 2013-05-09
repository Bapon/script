import sys, subprocess
def main():
    #print"hopo"
    #subprocess.call("pwd")
    #print "mysql"
    #subprocess.call(["zypper", "install", "mysql-community-     server"])
    #subprocess.call("reboot")
    #subprocess.call(["systemctl", "enable", "mysql.service"])
    #subprocess.call(["systemctl","start", "mysql.service"])
    #subprocess.call("mysql_secure_installation")
    #subprocess.call(["zypper", "install", "apache2"])
    #subprocess.call(["systemctl", "enable", "apache2.service"])
    #subprocess.call(["systemctl", "start", "apache2.service"])
    #subprocess.call(["zypper", "install", "apache2-mod_php5"])
    #subprocess.call(["systemctl", "restart", "apache2.service"])
    #info_php = open("/srv/www/htdocs/info.php", "w")
    #code = ('''<?php
    # phpinfo();
    # ?>''')
    # info_php.write(code) 
    subprocess.call(["zypper", "install", "php5-mysql"])

if __name__ == "__main__":
   main()  
   

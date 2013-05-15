import sys, os, subprocess
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
    #info_php.write(code) 
    #subprocess.call(["zypper", "install", "php5-mysql"])
    #phpmyadmin = open("/etc/apache2/conf.d/phpMyAdmin.conf", "w")
    #wcoad = ('''Alias/phpMyAdmin /srv/www/htdocs/phpMyAdmin
    #Alias/phpmyadmin /srv/www/htdocs/phpMyAdmin''')
    #phpmyadmin.write(wcoad)
    #subprocess.call(["systemctl", "restart", "apache2.service"])
    #subprocess.call(["a2enmod", "rewrite"])
    #print "virtual host"
    #f_in=open("/etc/apache2/listen.conf").read()
    #text=f_in.replace("#NameVirtualHost *:80", "NameVirtualHost *:80")
    #f_out =open("/etc/apache2/listen.conf", "w").write(text)
    #print"quantum.conf"
    #bapon= open ("/etc/apache2/vhosts.d/vhost.template").read()
    #text= bapon.replace("/vhosts/dummy-host.example.com/cgi-bin", "/cgi-bin")
    #text=text.replace("dummy-host.example.com", "quantum.com")
    #text=text.replace("Errorlog", "#Errorlog")
    #text=text.replace('AllowOverride None', 'AllowOverride All')
    #text=text.replace('ServerName quantum.com', ' ServerName quantum.com\n ServerAlias quantum.org.bd') 
    #bapon1=open ("/etc/apache2/vhosts.d/quantum.conf", "w").write(text)  
    print "_default"
    
    #file_in= open ("/etc/apache2/vhosts.d/quantum.conf").read()
    #text=file_in.replace('vhosts/quantum.com', 'htdocs')
    #text=text.replace('quantum.com', 'localhost')
    #text=text.replace('ServerAlias quantum.org.bd', '#ServerAlias quantum.org.bd')
    #file_out= open ("/etc/apache2/vhosts.d/_default.conf", 'w').write(text)
    print "create index file"
    #subprocess.call(["mkdir", "/srv/www/vhosts/quantum.com", "-p", "755"])
    #gias=open("/srv/www/vhosts/quantum.com/index.html", "w")
    #index_coad= "<html>it works</html>"
    #gias.write(index_coad)
    subprocess.call(["rcapache2","reload"])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__ == "__main__":
   main()  
   

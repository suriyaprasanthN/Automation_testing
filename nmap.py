import os
import sys
ip = input("Enter the ip :")
FTP ='nmap -Pn -sV -p 21 --script=banner -oN tcp_21_ftp_nmap.txt '+ip+''
SSH='nmap -Pn -sV -p 22 --script=banner,ssh2-enum-algos,ssh-hostkey,ssh-auth-methods -oN tcp_22_ssh_nmap.txt '+ip+''
SMTP='nmap -Pn -sV -p 25 --script=banner -oN tcp_25_smtp_nmap.txt '+ip+''
DNS='nmap -Pn -sU -sV -p 53 --script=banner -oN udp_53_dns_nmap.txt '+ip+''
HTTP='nmap -Pn -sV -p 80,443 --script=banner -oN tcp_port_protocol_nmap.txt '+ip+''
POP3='nmap -Pn -sV -p 110,995 --script=banner  -oN tcp_port_pop3_nmap.txt '+ip+''
RPC='nmap -Pn -sV -p 111,135 --script=banner,msrpc-enum,rpc-grind,rpcinfo -oN tcp_port_rpc_nmap.txt '+ip+''
NTP='nmap -sU -p 123 --script ntp-info '+ip+''
SMB='nmap -Pn -sV -p 445 --script=banner --script-args=unsafe=1 -oN tcp_445_smb_nmap.txt '+ip+''
IMAP='nmap -Pn -sV -p 143,993 --script=banner -oN tcp_port_imap_nmap.txt '+ip+''
LDAP='nmap -Pn -sV -p 389,3268 --script=banner -oN tcp_port_ldap_nmap.txt '+ip+''
SNMP='nmap -Pn -sV -p 1433 --script=banner --script-args=mssql.instance-MSSQL=1433,mssql.username=sa,mssql.password=sa -oN tcp_1433_mssql_nmap.txt '+ip+''
NFS='nmap -Pn -sV -p 111,2049 --script=banner -oN tcp_111_2049_nfs_nmap.txt '+ip+''
MySQL='nmap -Pn -sV -p 3306 --script=banner -oN tcp_3306_mysql_nmap.txt '+ip+''
RDP='nmap -Pn -sV -p 3389 --script=banner -oN tcp_3389_rdp_nmap.txt '+ip+''
VNC='nmap -Pn -sV -p 5900 --script=banner --script-args=unsafe=1 -oN tcp_5900_vnc_nmap.txt '+ip+''
AJP='nmap -Pn -sV -p 8009 -n --script ajp-auth,ajp-headers,ajp-methods,ajp-request -oN tcp_8009_ajp_nmap.txt '+ip+''

os.system(FTP)
os.system(SSH)
os.system(SMTP)
os.system(DNS)
os.system(HTTP)
os.system(POP3)
os.system(RPC)
os.system(NTP)
os.system(SMB)
os.system(IMAP)
os.system(LDAP)
os.system(SNMP)
os.system(NFS)
os.system(MySQL)
os.system(RDP)
os.system(VNC)
os.system(AJP)


import paramiko
import sys

def ssh_connect( _host, _username, _password ):
    try:
        _ssh_fd = paramiko.SSHClient()
        _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        _ssh_fd.connect( _host, username = _username, password = _password )
    except Exception as e:
        print('Authorization Failed!Please check the username,password or your device is connected to the Internet.')
        exit()
    return _ssh_fd

def ssh_exec_cmd( _ssh_fd, _cmd ):
    return _ssh_fd.exec_command( _cmd )

def ssh_close( _ssh_fd ):
    _ssh_fd.close()

def print_ssh_exec_cmd_return(_ssh_fd,_cmd):
    stdin,stdout,stderr=ssh_exec_cmd(_ssh_fd,_cmd)
    err_list = stderr.readlines()
    if len( err_list ) > 0:
        for err_content in err_list:
            print('ERROR:' + err_content)
        exit()
    for item in stdout:
        print(item)

if __name__ == '__main__':
    sshd = ssh_connect('192.168.1.121',sys.argv[1], sys.argv[2])
    print('Executing \''+sys.argv[3]+'\' command,remote controlling raspberrypi.')
    if len(sys.argv) == 4:
        print_ssh_exec_cmd_return(sshd,'cd Raspberry_pi_study;cd SAKS;cd RemoteControl;python main.py '+sys.argv[3])
    else:
        print_ssh_exec_cmd_return(sshd,'cd Raspberry_pi_study;cd SAKS;cd RemoteControl;python main.py '+sys.argv[3]+' '+sys.argv[4])
    ssh_close(sshd)
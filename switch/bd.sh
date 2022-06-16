#!/usr/bin/expect
set timeout 10
set host "192.168.90.158"
set username "admin"
set password "baisheng@123"
set more "\n"
log_file shebei
log_user 0
spawn ssh $username@$host "dis cu"
expect "*Password*" {send "$password\r"}
expect {
    "*More" {
        send "$more\r"
        exp_continue
    }
interact

}
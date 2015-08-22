#!/bin/bash

prefix="http://"
host="10.0.0.2:5000"

echo "$prefix$host"

http "$prefix$host/user/"
http "$prefix$host/user/1/"

http "$prefix$host/account/"
http "$host/account/1/"

http "$prefix$host/address/"
http "$prefix$host/address/1/"

http "$prefix$host/event/"
http "$prefix$host/event/1/"

http "$prefix$host/transaction/"
http "$prefix$host/transaction/1/"
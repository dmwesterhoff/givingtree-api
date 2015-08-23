#!/bin/bash

prefix="http://"
#host="10.0.0.2:5000"
host="192.168.1.78:5000"

echo "$prefix$host"

http "$prefix$host/users/"
http "$prefix$host/users/1/"

http "$prefix$host/organizations/"
http "$prefix$host/organizations/1/"

http "$prefix$host/accounts/"
http "$host/accounts/1/"

http "$prefix$host/addresses/"
http "$prefix$host/addresses/1/"

http "$prefix$host/events/"
http "$prefix$host/events/1/"

http "$prefix$host/transactions/"
http "$prefix$host/transactions/1/"

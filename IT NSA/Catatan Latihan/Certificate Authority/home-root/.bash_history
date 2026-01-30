cat /etc/bash/bash_completion.sh 
ls /etc/
apk add nano
nano /usr/share/bash-completion/completions/openssl
openssl req -x509 \
openssl req -x509 -sha256 -days 365 -nodes -newkey rsa:2048 -subj "/CN=lkslab-1.com/C=ID/L=Jawa Tengah" -keyout rootCA.key -out rootCA.crt
ls
mv rootC* certs/
cd certs/
ls
ls
mkdir server
cd server/
openssl genrsa -out server.key 2048
cat server.key 
openssl req -new -key server.key -out server.csr -config csr.conf 
ls
cat server.csr 
history 
ls /root/
ls /root/ -lA
ls /root/ -la
ls /home/
history > /etc/.bash_history
set -o | grep history
echo $HISTFILE
openssl x509 -req -in server.csr -CA ../rootCA.crt -CAkey ../rootCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
ls
cat server.crt 
ls
ls /root/ -A
cd certs/server/
openssl req -new -key server.key -out server.csr -config csr.conf 
rm server.csr 
openssl req -new -key server.key -out server.csr -config csr.conf 
openssl x509 -req -in server.csr -CA ../rootCA.crt -CAkey ../rootCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
rm server.crt 
openssl x509 -req -in server.csr -CA ../rootCA.crt -CAkey ../rootCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
ls
cd certs/
ls
openssl req -x509 -sha256 -days 365 -nodes -newkey rsa:2048 -subj "/CN=LKS LAB/C=ID/L=Jawa Tengah/O=Foo/OU=Bar" -keyout LKS-LAB.key -out LKS-LAB.crt
ls
cd server/
openssl req -new -key server.key -out server.csr -config csr.conf 
openssl x509 -req -in server.csr -CA ../rootCA.crt -CAkey ../rootCA.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
openssl x509 -req -in server.csr -CA ../LKS-LAB.crt -CAkey ../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
cd certs/
cd server/
openssl req -new -key server.key -out server.csr -config csr.conf 
openssl x509 -req -in server.csr -CA ../LKS-LAB.crt -CAkey ../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
cd certs/server/
openssl req -new -key server.key -out server.csr -config csr.conf 
openssl x509 -req -in server.csr -CA ../LKS-LAB.crt -CAkey ../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
cd certs/
cd server/
openssl req -new -key server.key -out server.csr -config csr.conf 
openssl x509 -req -in server.csr -CA ../LKS-LAB.crt -CAkey ../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile cert.conf 
cd certs/server/
ls
mkdir coba
cd coba/
openssl req -new -key ..\server.key -out server.csr 
openssl req -new -key ../server.key -out server.csr 
ls
cat server.csr 
openssl req -new -key ../server.key -out server.csr -addext "subjectAltName = DNS:lkslab-1.com"
openssl req -new -key ../server.key -out server.csr -extension "subjectAltName = DNS:lkslab-1.com, DNS:*.lkslab-1.com"
openssl req -new -key ../server.key -out server.csr -extension "subjectAltName = DNS:lkslab-1.com, DNS:*.lkslab-1.com"
openssl req -new -key ../server.key -out server.csr -addext "subjectAltName = DNS:lkslab-1.com, DNS:*.lkslab-1.com"
ls
openssl x509 -req -in server.csr -CA ../../LKS-LAB.crt -CAkey ../../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -addext "subjectAltName = DNS:lkslab-1.com, DNS:*.lkslab-1.com"
openssl x509 -req -in server.csr -CA ../../LKS-LAB.crt -CAkey ../../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extensions "subjectAltName = DNS:lkslab-1.com, DNS:*.lkslab-1.com"
ls
cd ..
ls
mkdir backup
mv server.{crt,key} backup/
ls
cp coba/* .
ls
ls
cp backup/server.key .
ls
cd coba/
openssl req -new -key ../server.key -out server.csr -addext "subjectAltName = DNS.1:lkslab-1.com, DNS.2:*.lkslab-1.com"
openssl x509 -req -in server.csr -CA ../../LKS-LAB.crt -CAkey ../../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extensions "subjectAltName = DNS.1:lkslab-1.com, DNS.2:*.lkslab-1.com"
cd ..
cp coba/* .
ls
openssl req -new -key ../server.key -out server.csr
cd coba/
openssl req -new -key ../server.key -out server.csr
openssl x509 -req -in server.csr -CA ../../LKS-LAB.crt -CAkey ../../LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile <(printf "subjectAltName=DNS:lkslab-1.com,DNS:*.lkslab-1.com")
cp * ../
ls
cd ..
ls
openssl x509 -noout -text -in server.crt 
openssl x509 -noout -text -in ../LKS-LAB.crt 
cd ..
ls
openssl req -x509 -sha256 -days 365 -nodes -newkey rsa:2048 -subj "/CN=LKS LAB/C=ID/L=Jawa Tengah/O=Otong Inc./OU=Any" -keyout RootCAKey_LKS-LAB.key -out RootCA_LKS-LAB.crt
ls
rm LKS-LAB.*
ls
cd server/coba/
rm ../backup -rf
ls ..
ls
cd ..
openssl x509 -req -in server.csr -CA ../RootCA_LKS-LAB.crt -CAkey ../RootCAKey_LKS-LAB.key -CAcreateserial -out server.crt -days 365 -sha256 -extfile <(printf "subjectAltName=DNS:lkslab-1.com,DNS:*.lkslab-1.com")
rm coba -r
ls
ls

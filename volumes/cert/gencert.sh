caname="geoshop-ca"
expdays="365"
domain=$@

if [ ! -f $caname.key ]
then
  openssl genrsa -days $expdays -out $caname.key 2048
  openssl req -days $expdays -nodes -new -x509 -key $caname.key -out $caname.crt \
  -subj '/CN=GeoshopDemo Root CA/C=AT/ST=Zurich/L=Zurich/O=Geoshop'
fi

echo "Generating key"
openssl genrsa -days $expdays -out $domain.key 2048

cat csr.conf.base | sed "s/_DOMAIN_/$domain/g" > csr.conf
echo "Generating sign request"
openssl req -days $expdays -new -key $domain.key -out $domain.csr -config csr.conf

echo "Signing the key"
openssl x509 -req -in $domain.csr -CA $caname.crt -CAkey $caname.key \
  -CAcreateserial -out $domain.crt -days $expdays \
  -extfile csr.conf -sha256
rm csr.conf

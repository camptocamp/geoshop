caname="geoshop-ca"
domain=$@

if [ ! -f $caname.key ]
then
  openssl req  -nodes -new -x509  -keyout $caname.key -out $caname.crt -subj '/CN=GeoshopDemo Root CA/C=AT/ST=Zurich/L=Zurich/O=Geoshop'
fi

rm -rf $domain.crt $domain.key $domain.csr

echo "Generating key"
openssl genrsa -out $domain.key 2048

cat csr.conf.base | sed "s/_DOMAIN_/$domain/g" > csr.conf
echo "Generating sign request"
openssl req -new -key $domain.key -out $domain.csr -config csr.conf

echo "Signing the key"
openssl x509 -req -in $domain.csr -CA $caname.crt -CAkey $caname.key \
  -CAcreateserial -out $domain.crt -days 365 \
  -extfile csr.conf -sha256
rm csr.conf

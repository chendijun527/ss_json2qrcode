# ss_json2qrcode
A command line tool generating Shadowsocks QR code from config JSON

-Accepted JSON input:
```
{
	"local_port":1234,
	"server_password": [
		["abc.xyz.com:4321", "password","aes-128-cfb"] 
	]
}
```

-Prerequisite:
`qrcode` and `image` Python packages are installed

[Visit Shadowsocks](http://shadowsocks.org/en/config/quick-guide.html)

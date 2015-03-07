# ss_json2qrcode
A command line tool generating Shadowsocks QR code from config JSON

### Prerequisite
* Python package `qrcode`
* Python package `image`

###  Accepted JSON input
* (1) Config JSON provided by a Shadowsocks service provider
```
{
	"local_port":1234,
	"server_password": [
		["abc.xyz.com:4321", "password","aes-128-cfb"] 
	]
}
```

[Visit Shadowsocks](http://shadowsocks.org/en/config/quick-guide.html)

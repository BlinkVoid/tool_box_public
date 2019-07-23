# Normal Usage #
## first time use ##

**Env Setup**
1. *Install Python*
2. *Install requirements using pip*
3. *Install GPG software*
4. *make sure the binary and key ring directories are set up*

**Generate key pair**

1. If the key is intended for long term use, do not set it with a expiry date, need to be very careful about encrytion and backup options.
2. It is advised to set a passphrase on the key so that there is an extra line of defense with the private key
3. Sample command

```python
aGPG = GPG_PROG(data_path, binary_path)
aGPG.generate_keypair()
```

**Export key file**
1. List out available key pairs, and select the one to backup
2. Run backup command to backup the keys for a later use.

>note：the backed up key file can be imported via other GPG software.

```python
keys = aGPG.list_keys()
aGPG.export_keyfile(keys[0]['fingerprint'], 'passphrase', 'rkey_export_file')
```

## normal usage ##

1. load the software class
2. load keys
3. encrypt file using the appropriate key recipients
4. decrypt file using the appropriate key

*Sample command:*
```
aGPG = GPG_PROG(data_path, binary_path)
keys = aGPG.list_keys()
recipient_list = [keys[0]['fingerprint']]
aGPG.encrypt_file(plainfName, encryptedfName, recipient_list)
aGPG.decrypt_file(file_2_decrypt, outfName)
```
## QR usage ##
Call method to share
**Env Setup**
1. require package ***qrcode***, ***pyzbar***
2. require setup a QR scanner as IO device in order for the optical communication to work.
3. alternatively, can use mobile phone to scan generated QR code, transfer in via USB.
4. convert the file to QR code for sharing
5. receive QR code and decode for GPG usage

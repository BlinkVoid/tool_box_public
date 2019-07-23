#!/usr/bin/env python
# coding: utf-8
# ==================================================
# install:
# pip3 install python-gnupg
# note: please make sure that `python-gnupg` is installed, instead of `gnupg` python package.
# otherwise, configuraiton will be a nightmare

# note - gpg needs to be installed first:
# brew install gpg
# apt install gpg

# you may need to also:
# export GPG_TTY=$(tty)
# copyright attribute:
# original source code: https://gist.github.com/ryantuck/56c5aaa8f9124422ac964629f4c8deb0

# Package List:
# 1. https://pythonhosted.org/python-gnupg/#encryption
# 2. https://github.com/lincolnloop/python-qrcode
# ==================================================
# Author: BlinkVoid
# Date: 22072019
# intruction of use: see readme.md
# version 1.0
# ==================================================
import gnupg
import qrcode
from pyzbar import pyzbar
from PIL import Image
#this particular data path is for storing key rings, so it can be changed to any arbitrary absolute path
data_path = "E:\\Programs\\GnuPG\\data_dir_key_rings"
#binary path for windows, dependant on where the program was installed.
# for this particular instance, program was not installed at system drive
# linux OS will require modifying the datapath and binary path
binary_path = "E:\\Programs\\GnuPG\\bin\\gpg.exe"

class GPG_PROG():
    def __init__(self, data_path, binary_path):
        self.gpg = gnupg.GPG(gnupghome=data_path, gpgbinary=binary_path)
        #for Debugging only
        #if something went wrong, try turn on verbose sign to check
        #gpg = gnupg.GPG(gnupghome="E:/Programs/GnuPG/data_dir_key_rings", binary="E:\\Programs\\GnuPG\\bin\\gpg.exe", verbose=True)
    def generate_keypair(self):
        input_name_email = input("Input your name and email for GPG: ")
        input_passphrase = input("Input your passphrase for the key: ")
        input_key_type = input("Select key type (example: RSA, DSA): ")
        input_key_length = input("Key length: (example: 1024, 2048, 4096): ")
        input_expire_date = input('''The expiration date for the primary and any secondary key.
        You can specify an ISO date,
        A number of days/weeks/months/years,
        an epoch value, or 0 for a non-expiring key.
        (Example: “2009-12-31”, “365d”, “3m”, “6w”, “5y”, “seconds=<epoch>”, 0)''')
        input_data = self.gpg.gen_key_input(
            name_email=input_name_email,
            passphrase=input_passphrase,
            key_type=input_key_type,
            key_length=input_key_length,
            expire_date=input_expire_date,
        )
        key = self.gpg.gen_key(input_data)
        print("Generated key: {0}".format(key))
        return(key)

    def export_keyfile(self, fingerprint, aPassphrase, keyfName):
        # create ascii-readable versions of pub / private keys
        ascii_armored_public_keys = self.gpg.export_keys(fingerprint)
        ascii_armored_private_keys = self.gpg.export_keys(
            keyids=fingerprint,
            secret=True,
            passphrase=aPassphrase,
        )
        # export
        # can take argumet to rename the output key file, but won't do here.
        with open(keyfName+'.asc', 'w') as f:
            f.write(ascii_armored_public_keys)
            f.write(ascii_armored_private_keys)
        return(0)

    def import_keyfile(self):
        filename = input('''Input key file name, key file must be placed under the same path as the python script.
                            Without the .asc file extension: ''')
        with open(filename+".asc") as f:
            key_data = f.read()
        import_result = self.gpg.import_keys(key_data)
        return(import_result)

    def list_keys(self):
        keys = self.gpg.list_keys()
        return(keys)

    def encrypt_file(self, plainfName, encryptedfName, recipient_list):
        with open(plainfName, 'rb') as f:
            status = self.gpg.encrypt_file(
                file=f,
                recipients=recipient_list,
                output=encryptedfName+'.gpg',
            )
        print(status.ok)
        print(status.status)
        print(status.stderr)
        print('~'*50)
        return(status)
    def decrypt_file(self, file_2_decrypt, outfName):
        # decrypt file
        aPassphrase = input("Input your passphrase for the private key: ")
        with open(file_2_decrypt, 'rb') as f:
            status = self.gpg.decrypt_file(
                file=f,
                passphrase=aPassphrase,
                output=outfName,
            )
        print(status.ok)
        print(status.status)
        print(status.stderr)

class QR_TRANSMIT():
    def __init__(self):
        self.qr = qrcode.QRCode(
            version=10,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=5,
            border=4,
        )
        self.decode = pyzbar.decode
    def pack_data(self, data, pic_2_save):
        self.qr.add_data(data)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill_color="black", back_color="white")
        img.save(pic_2_save+'.png')
        return(img)
    def receive_data(self, image_fName):
        code = self.decode(Image.open(image_fName))
        message = message[0].data.decode()
        print(message)
        return(message)

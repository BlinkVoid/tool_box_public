# tool_box_public

**0x0 Date: July 2019**

Decided to share some of the tools I've made.
Would welcome any improvement advices/merge to improve the usability of the tools.

**0x1 GnuPG**

It's always fascinating to encrypt and decrypt files and share across the internet.
The premise of this tool was to build a script that can encrypt certain secret in an air-gap machine or warm machine(only turns on when used) that require actively reducing the internet communication as much as possible.

For installation, files can be transferred via trusted USB files.

The secret sharing part can be done via optical methods, i.e. convert text into QR code and using another device to scan.
Experimented with several encryption libraries such as ***cryptography***, ***Crypto*** and ***python-gnupg*** and decided to use **GnuPG**.
Reason being:
1. GnuPG comes with a GUI software that can compensate the usage
2. GnuPG has a better support for the package
3. it can implement with RSA, which then can possible extend the usage into more complex cases that the tool hasn't covered yet, such as share with multiple participants, signing and verifying messages, etc.

The detailed instruction is in [README.gnupg_experiment.md · GitHub](https://github.com/BlinkVoid/tool_box_public/blob/master/README.gnupg_experiment.md)

**0x2 TBD**

Still under construction, will update when finish

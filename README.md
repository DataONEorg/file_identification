# Enabling identification of specific metadata formats with command line tools
[ToC]


## File Command:
## Libmagic:
## DataONE file formats:  
## Using custom magic file:
## Python Unittest:
## Installing and Using magic file:
  * ### On Linux:
  * ### On Mac :

## References:


## Week 2 (06/04/2018)

[ToC]


## Day 1

### Creation of Environment for submitting changes.
* https://www.kernel.org/doc/html/v4.14/process/submitting-patches.html
* https://filemagic.readthedocs.io/en/latest/guide.html
* https://github.com/file/file

DataONE File Formats:

* https://cn.dataone.org/cn/v2/formats

- add support for the "http://www.openarchives.org/ore/terms" format ID

#### Formatting of Magic file for submission
* Restructured magic file as per the [instructions](https://github.com/file/file) for submission of magic files.
* The below description needs to be still updated.

  Provide complete information with entry:
  * One line short summary
  * Optional long description
  * File extension, if applicable
  * Full name and contact method (for discussion when entry has problem)
  * Further reference, such as documentation of format

* Added entry in magic and unittest file for "http://www.openarchives.org/ore/terms" format ID

### linking custom magic files
* https://unix.stackexchange.com/questions/213611/update-magic-file-list-and-or-submit-my-own)
* https://stackoverflow.com/questions/2124749/compiling-libmagic-statically-c-c-file-type-detection/2125150#2125150


## Day 2

### Server for testing libmagic

Server: dev-orc-1.test.dataone.org
User name: pratik
Authentication by ssh key

The following command can be used to create a key pair for accessing DataONE servers:

```
ssh-keygen -t rsa -b 4096 -C "DataONE key for ${USER}" \
             -f "${USER}.dataone.org.rsa.4096"
```

This will produce two files in the current directory. The one ending in .pub is the public portion of the key and should be placed in the sshpublickey folder. The other file is your private key, and that should be placed in
`${HOME}/.ssh` (or referenced by your `.ssh/config file`) and `chmod
0600`.

Note that a passphrase should always be used when creating a SSH key. An unprotected SSH key is highly vulnerable to breach.

### Using custom magic entries on Ubuntu

* check for the `file` command version using  `file -v`
```shell
  file-5.25
  magic file from /etc/magic:/usr/share/misc/magic
```
* In the ***/etc/magic*** file place your entries in it.

``` shell
pratik@dev-orc-1:~/github_repos/file_identification$ file examples/resourcemap/00_resourcemap.xml
examples/resourcemap/00_resourcemap.xml: XML 1.0 document, ASCII text

pratik@dev-orc-1:~/github_repos/file_identification$ file examples/resourcemap/00_resourcemap.xml
examples/resourcemap/00_resourcemap.xml: http://www.openarchives.org/ore/terms
```



### Clone [`file`](https://github.com/file/file) repo

* https://unix.stackexchange.com/questions/315558/file1-5-28-invalid-argument-when-using-bytes-parameter

* Trying to install the package while including our changes. Created a new repo [file_pratik](https://github.com/pratikshrivastava/file_pratik) which have old and new magic files.
* Add custom magic file [dataone](https://github.com/DataONEorg/file_identification/blob/master/magic_files/dataONE) to magic/Magdir folder.
* Add "$(MAGIC_FRAGMENT_DIR)/dataone \ “ entry in Makefile.am

* ***`autoconf`***
  * if issues with above command then follow the steps below:
    * sudo apt-get install autoconf automake libtool
    * sudo apt-get install make pkg-config check g++ librsync-dev libz-dev libssl-dev uthash-dev libyajl-doc
    * autoreconf -fvi
* ***`./configure`***
* ***`make`***
  * this step should create the magic.mgc file
* make check -no errors
* sudo make install
This step will place the ***`magic.mgc`*** file in ***`/usr/local/share/misc/`*** folder.

* make installcheck - no errors
* remove libmagic `sudo apt-get purge libmagic1 file`
* The new magic.mgc file would be created in magic folder of the repo.
``` shell
pratik@dev-orc-1:~/github_repos/file/magic$ ls -lrt magic.mgc
-rw-r--r-- 1 pratik pratik 5222264 Jun  5 14:11 magic.mgc
```

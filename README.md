### HTMLImgRelative
The script scans html file in specified and child directories, then replaces remote images paths with local ones and downloads them to the local drive.
May be useful for building archives with offline html documentation.
 
### Requirements:
 
* bs4
* requests
* validators
 
### Installing steps

 * For bash/zsh shells (Linux, macOS and other *nix systems):
 	1. Open directory where repository files had been placed 
 	'cd /path/to/directory/contained/main.py'
 	2. Execute install_req.sh script
 	'./install_req.sh '
 	
 * For Windows:
 	
 	#todo
 	
 	
 ### Usage:

1. `source ./bin/activate`
2. `python3 HTMLImgRelative.py /path/to/directory/with/html/files`

Functionality has been tested on python 3.8 and 3.10 on macOS and Ubuntu. Other systems will be tested soon.


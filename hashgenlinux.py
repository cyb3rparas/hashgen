#! /usr/bin/python
import hashlib
from termcolor import colored
print(colored("                  H3y Guys! W3lc0me t0 hashg3n hashg3nerat0r!!",'cyan',attrs=['bold']))
print(colored("            c00k y0ur hasH in a single flash,with0ut int3rnet access! ",'cyan',attrs=['bold']) )
print(colored("                         ****C0ded by 0daymaroon****",'cyan',attrs=['bold']))
print()
print(colored("         Available Algorithms-- md5,sha1,sha224,sha256,sha384 and sha512",'cyan',attrs=['bold']))
print()
string=input(colored("Enter the string you want to hash: ",'blue'))
algorithm=input(colored("Enter the encoding algorithm you want to use: ",'blue'))
if(algorithm.lower()=="md5"):
	hash=hashlib.md5()
elif(algorithm.lower()=="sha1"):
	hash=hashlib.sha1()
elif(algorithm.lower()=="sha224"):
	hash=hashlib.sha224()
elif(algorithm.lower()=="sha256"):
	hash=hashlib.sha256()
elif(algorithm.lower()=="sha384"):
	hash=hashlib.sha384()
elif(algorithm.lower()=="sha512"):
	hash=hashlib.sha512()
else:
	print()
	print(colored("ERROR!! This encoding algorithm is not supported or is wrong!!",'red'))
	exit(0)


hash.update(string.encode())
print()
print(colored("Yay! Your hash is "+hash.hexdigest(),'green'))

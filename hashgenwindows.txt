#! /usr/bin/python
import hashlib
print("                  H3y Guys! W3lc0me t0 hashg3n hashg3nerat0r!!")
print("            c00k y0ur hasH in a single flash,with0ut int3rnet access! ")
print("                         ****C0ded by 0daymaroon****")
print()
print("         Available Algorithms-- md5,sha1,sha224,sha256,sha384 and sha512")
print()
string=input("Enter the string you want to hash: ")
algorithm=input("Enter the encoding algorithm you want to use: ")
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
	print("ERROR!! This encoding algorithm is not supported or is wrong!!")
	input()
	exit(0)


hash.update(string.encode())
print()
print("Yay! Your hash is "+hash.hexdigest())
input()

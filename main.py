#!/usr/bin/python3

import argparse

import array
import binascii
import os
import sys
from MyImage import MyImage
from PIL import Image

def count_blocks():
    return

def get_size(file: str):
    return os.path.getsize(file)

def get_RGB(file: str):
    (r,g,b) = Image.open(file).convert('RGB')
    return (r,g,b)

def read_byte():
    return None

def write_byte():
    return None

def encode_data(file: str, text: str):
    myImage = MyImage(file)
    length = to_binary(len(text),64) #max text length 64 bits
    print("length of msg ",length)


    print("Encrypt complete")

def encode_file():

    print("Encrypt complete")

def to_binary(value, size: int):
    bin_value = bin(value)
    if len(bin_value) > size:
        raise Exception("value can not fit in ", size, " bits")
    while len(bin_value) < size:
        bin_value = "0"+bin_value
    return bin_value

def main():
    parser = argparse.ArgumentParser(description='Steganography')
    parser.add_argument('-c', '--cover', dest='cover_image', help='cover image', required=True)
    parser.add_argument('-s', '--secret', dest='secret_data', help='secret data')
    parser.add_argument('-sf', '--secret_file', dest='secret_file', help='secret file')
    parser.add_argument('-o', '--output', help='Set to put in decode mode. default="encode"')
    args = parser.parse_args()

    if args.output:
        raise Exception("implement") #decode image
    else: 
        if os.path.exists(args.cover_image):
            if (args.secret_data is not None): 
                encode_data(args.cover_image, args.secret_data)
                raise Exception("implement") #encode text into cover
            elif (args.secret_image is not None):
                raise Exception("implement") #encode file into cover
            else:
                raise Exception("You should not be here")
        else:
            raise Exception("File does not exist")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Bye..")

#./main.py -c good_boy.png -s "Hello"
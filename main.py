print('''

StegMe is a tool uses Steganography to encode your Text inside an Image.

    #############     #############     #############     #############     ##        ##      #############
    #                       #           #                 #                 # #      # #      #
    #                       #           #                 #                 #  #    #  #      #
    #                       #           #                 #                 #   #  #   #      #
    #############           #           ############      #    ########     #    ##    #      ############
                #           #           #                 #           #     #          #      #
                #           #           #                 #           #     #          #      #
                #           #           #                 #           #     #          #      #
    #############           #           #############     #############     #          #      #############

Anyone with Knowledge how to use can use this tool without hesitation.
                                Or
You can visit the official website :    https://stegme.pythonanywhere.com

    How to Use:

    1.  First you have to choose that you want to Encode some Message or want to Decode an Image sent by your friend using this Tool...
    2.

''')

import os
import sys
import matplotlib.image as mplib_img

from message_encoder import Stego_Encode
from message_decoder import Stego_Decode
from convert import Text_to_binary, Binary_to_text


def Message_Encode():

    message = input("Please Provide the Message to encode :\t")
    message_data = Text_to_binary(message)

    image_path = input("Please Provide the path to the Image with Extention (i.e .png, .jpg etc) to Start Encoding :\t")
    abs_image_path = os.path.abspath(image_path)
    #print(abs_image_path)

    new_image = input("Please Provide the name for your new image:\t")

    print("adding png")
    new_image = new_image.split('.')[0] + '.png'

    # Encoder and pixel data of the new encoded image
    encoder = Stego_Encode(abs_image_path, message_data.convert_to_binary())
    pixels = encoder.encode()


    mplib_img.imsave(new_image, pixels)

    print("Phew!! Done with Encoding")

def Message_Decode():

    image_path = input("Please Provide the path to the Image with Extention (i.e .png, .jpg etc) to Start Decoding :\t")
    abs_image_path = os.path.abspath(image_path)
    #print(abs_image_path)

    decoder = Stego_Decode(abs_image_path)
    decoder.convert_to_pixels()

    Message = decoder.decode()

    Message = Message.rstrip('`')

    print("Phew!! Done with Decoding")
    print(f"This is your Message : {Message}")


choice = ''

while choice != 'q':
    print("\n\tWhat do you want to do:\n\tChoose an Option... or Ctrl+C to Exit\n")
    choice = input("\te. Message Encoding      d. Message Decoding      q. Quit\n")

    if choice.lower() == 'e':
        encode = Message_Encode()
    elif choice.lower() == 'd':
        decode = Message_Decode()
    elif choice.lower() == 'q':
        sys.exit()
    else:
        print("Wrong Choice! Please Choose an option to process further or 'q' to Exit")

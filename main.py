"""
Instruction for digiCam side, install digitCamControl
Instruction for alright side, log onto whatsapp web on Google Chrome webdriver when first launch
When you're running your program made with alright,
you can only have one controlled browser window at a time.
Running a new window while another window is live will raise an error.
So make sure to close the controlled window before running another one
"""

import os

from alright import WhatsApp
from dotenv import load_dotenv

import digiCamControlPython as dccp

load_dotenv()

image_mode = "Save_to_PC_only"
image_directory = "C:\\Images\\"

test_message = os.getenv('TEST_MESSAGE')
test_image = os.getenv('TEST_IMAGE')
mobile_prefix = os.getenv('MOBILE_PREFIX')
sample_mobile_number = os.getenv('SAMPLE_MOBILE_NUMBER')


def pr_green(skk): print("\033[92m{}\033[00m".format(skk))


def main():
    # Camera set up
    camera = dccp.Camera()
    camera.setTransfer(image_mode)
    camera.setFolder(image_directory)

    # Whatsapp set up
    messenger = WhatsApp()
    pr_green("Begin new photobooth grouping")
    phone_number = input("Type in phone number here: ")
    messenger.send_direct_message(mobile_prefix + phone_number, test_message, saved=False)
    print("If message not received or end of shoot, [ctrl + c] to quit")

    while True:
        input("Photobooth ready, [enter key] to take picture")
        image_name = camera.capture().strip('"')
        print(image_name)
        user_input = input(
            "Photo ready for review, digicamcontrol window, input [enter key] to send photo, [x] then [enter key] to delete photo")
        if user_input != "x":
            image_absolute_directory = image_directory + image_name
            print(image_absolute_directory)
            messenger.send_file(image_absolute_directory)


if __name__ == "__main__":
    main()

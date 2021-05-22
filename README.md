# Hacky Hour 08/06/2020
![Screen Shot 2020-08-04 at 2 09 13 PM](https://user-images.githubusercontent.com/21957723/89355485-5640f400-d670-11ea-8421-4f2d6ecba664.png)

Source code for the August 6 2020 Hacky Hour!  Demonstrates how a computer vision application can be used in manufacturing to confirm that a worker has chosen the correct component for assembly of a product.  The CV application finds the roi associated with an illuminated LED on a tray shelve.  It then checks to see if the workers hand has picked up the correct component using a hand detection model and overlapping rectangles algorithm between roi and hand detection bounding box.  The bounding box of hand detector turns green when the correct component is chosen and remains red until that occurs.

## Repo Programs
| Folder                     	| Description                                                                                              	|
|----------------------------	|----------------------------------------------------------------------------------------------------------	|
| tray-program          	| Program creates an roi associated with an illuminated LED on a tray shelve. It then checks to see if the workers hand has picked up the correct component using a hand detection model and overlapping rectangles algorithm between roi and hand detection bounding box and is configured to run on a PC or Mac|
| tray-pi 	| Program creates an roi associated with an illuminated LED on a tray shelve. It then checks to see if the workers hand has picked up the correct electronics component using a hand detection model and overlapping rectangles algorithm between roi and hand detection bounding box and is configured to run on a Raspberry Pi with NCS 2 Device from Intel|
|

## Running
Create a project in the dashboard for the applications

Use the alwaysAI CLI to build and start these apps on Linux Device with NCS 2 connected:

Go to the tray-rpi directory and enter the following commands

Configure (once): `aai app configure`

Build: `aai app install`

Run: `aai app start`

If you are using a Mac or Windows 10 PC do the following:

Go to the tray-program directory and enter the following CLI commands

Configure (once): `aai app configure`

Build: `aai app install`

Run: `aai app start`


## Support
Docs: https://dashboard.alwaysai.co/docs/getting_started/introduction.html

Realsense API Docs: https://alwaysai.co/docs/edgeiq_api/real_sense.html

Community Discord: https://discord.gg/R2uM36U

Email: contact@alwaysai.co

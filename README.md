# hacky-hour-0806202
Source code for the August 6 2020 Hacky Hour!  Demonstrates how a computer vision application can be used in manufacturing to confirm that a worker has chose the correct component for assembly of a product.  The cv application finds the roi associated with an illuminated LED on a tray shelve.  It then checks to see if the workers hand has picked up the correct component using a hand detection model and overlapping rectangles algorithm between roi and hand detection bounding box.  The bounding box of hand detector turns green when the correct component is chosen and remains red until that occurs.
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

Build: `aai app deploy`

Run: `aai app start`

If you are using a Mac or Windows 10 PC do the following:

Go to the tray-program directory and enter the following commands

Configure (once): `aai app configure`

Build: `aai app install`

Run: `aai app start`


## Support
Docs: https://dashboard.alwaysai.co/docs/getting_started/introduction.html

Realsense API Docs: https://alwaysai.co/docs/edgeiq_api/real_sense.html

Community Discord: https://discord.gg/R2uM36U

Email: contact@alwaysai.co


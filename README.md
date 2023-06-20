This is a self writted text chat software which has been writted in python using multiple threads and libraries.
These include:
tkinter   - For UI
socket    - For Network Comunication
time      - For .sleep() offsets so that the send always comes after the recv is open
threading - For multi-threading so that it can comunicate effciently withought the need for carrier messages like the "E" series servers and "test" series clients
PIL       - Used for image computation in releases 2.0.0 onward
os        - Used for file locating so that images can be read and written alleviating the need to cache in RAM

Version history:
"E" series servers
"test" series clients
are proof of concept code which is short and meant to prove that it works
the files "imagecli" and "imageser" were used for testing of small snippets of code for image transmittion
client and server version with the numbering structure "x.x.x" are the latest version of the code and support the newest features

!!Beware that the code isnt backwards compatible identify the correct pairs to be used in conjuction!!

Profile picture setup:
name your square profile picture in the folder the client is located on naming it "my_image.png"
!!Beware that if images are cached in the client folder if the same user with a different profile picture logs on their profile will not be updated do this by deleting the png file with their name on it in the folder which the client script located!!

Standard ports:
SockA:49153 (Send socket (From Client))    - "porta"
SockB:49154 (Recv socket (From Client))    - "portb"
SockC:49155 (image thread called "IM()")   - "portc"

You can change your port settings by going to the start function and adding 1-2 lines of code after the entry code.
!!Beware that changing the port settings on the client you must do it on the server too!!
!!Beware that portc = portb + 1 and is not recommended to be changed!!

Admin Commands:
To execute these commands go to the chat entry box and you can enter the following commands:
admin -s            - Saves the chat history to file and sends you a message saying the file name
admin -l |Filename| - Loads the chat history remmember to type the filename with ".txt" at the end
admin -c            - Clears the chat history except for the last 10 messages to be used when the list on the server is too long and cpu/ram usage becomes undesirebly high
admin -t : [Text]   - Message all users as server "Console"
/Debug              - Toggles Debug Client side
admin -sd           - Shuts down server in 10 seconds has countdown starting from 10 then waits till 5 and coutdown till 1

!!Caution Admin commands are not restricted yet!!

Server Options:
sde                 - Shut down enable              - Allows admin to shut down server (cannot remote shutdown withought this being set as TRUE) (Default = False)

2.0.1 - 1 |Updates to| 2.0.1  - Added a file called "Cons.png" for anything that comes from the server such as "Console" messages or responses to admin commands
2.x.x - x Confirmed Compatibility:    
Server          Client
2.0.0           2.0.0
2.0.1           2.0.0
2.0.1           2.0.1
2.0.1           2.0.1 - 1
2.0.1 - 2       2.0.1 - 2

2.0.0 clients/servers and 2.0.1 clients/servers shouldn't be paired up as the timeings for the image thread are different: check the compatifility chart
!!WARNING messages are not encrypted and the server isnt protected by a password!!

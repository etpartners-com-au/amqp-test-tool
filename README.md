# README #

This README would normally document whatever steps are necessary to get your application up and running.

Go make a real wiki page....

This is a blocking client - its should send and THEN exit.


## Install
You will need the proton library:

    pip install python-qpid-proton

Once you have that installed - edit the `client.py` file and then change the username and password.

You will have to use URL quote_plus (like an encoder) to make sure any weird passwords can be sent on the URL.

## Running

Launch the app like this:

    python client.py
	
Make sure you set `messagePattern` to match the filelist you want. Go read the python docs for GLOB.


# README #

This README would normally document whatever steps are necessary to get your application up and running.

This is a blocking messaging client - its should send and THEN exit.

The `python-qpid-proton` library REQUIRES compilers - Visual studio community edition with command line support. 
* Install it
* Launch the x64 command line dev tools
* source your python env - `c:\anaconda3\scripts\activate.bat c:\anaconda3`
* then use pip to install the module - it will build a binary whl file that matches python and your architecture.


## Install
You will need the proton library:

    pip install python-qpid-proton

Once you have that installed - edit the `client.py` file and then change the username and password.

You will have to use URL `quote_plus` (like an `encoder`) to make sure any weird passwords can be sent on the URL.

## Running

Launch the app like this:

    python client.py
	
Make sure you set `messagePattern` to match the filelist you want. Go read the python docs for GLOB.


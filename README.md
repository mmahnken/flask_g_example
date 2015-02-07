##Setup  

You'll need to install virtualenv in order to create the environment to run this app.
####Pre-setup    
In your terminal, run 
`which virtualenv`   
If the output is a filepath, you have virtualenv! If not, [install it](https://virtualenv.pypa.io/en/latest/installation.html).   

###Create your env
In this directory, run   
`virtualenv env`   
Then   
`source env/bin/activate`   

###Check your env  
Try   
`which pip`   
Does it output this a path to this directory and then /env/pip? If so, move on.

###Install requirements into your env
Run
`pip install -r requirements.txt`

### Start your server
Run 
`python g_example.py`
And check it out in your browser.



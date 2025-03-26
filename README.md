<h1>How to install django: </h1>
 
1. Make sure Python is already installed in our system 
 
python --version 
 
2. Install django by using pip 
 
pip install django 
pip install django == 1.11.9 
 
D:\>pip install django 
Collecting django 
Downloading  
https://files.pythonhosted.org/packages/51/1a/6153103322/Django-2.1-py3-none
any.whl (7.3MB) 100% || 7.3MB 47kB/s 
 
Collecting pytz (from django) 
  Downloading https://files.pythonhosted.org/packages/30/4e/ 
53b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB) 
    100% || 512kB 596kB/s 
 
Installing collected packages: pytz, django 
Successfully installed django-2.1 pytz-2018.5 
You are using pip version 9.0.3, however version 18.0 is ava 
You should consider upgrading via the 'python -m pip install 
 
3. To check django version: 
 
py -m django --version 
 
ATOM IDE/Editor: 
Install ATOM IDE from the following link  https://atom.io/ 
 
Speciality of ATOM IDE: 
 It is freeware. 
 It is open source. 
 It supports cross platform. 
 It provides several auto completion short-cuts for easy development 
etc 
How to Configure Atom for Python: 
 
1) Terminal Installation: 
File  Settings  Install  In the searchbox just type terminal  platform-ide
terminal 
 
2) Python AutoCompletion: 
File  Settings  Install  In the searchbox just type python  autocomplete-python 
 
3) django: 
File  Settings  Install  In the searchbox just type django  atom-django 
 
4) How to Change Terminal from Powershell to Normal Command Prompt: 
File  Settings  Install  In the searchbox just type terminal  platform-ide
terminal  settings  Shell Override 
 
C:\Windows\System32\cmd.exe 
How to create Django Project: 
 
Once we installed django in our system, we will get 'django-admin' command line tool, 
which can be used to create our Django project. 
 
django-admin startproject  firstProject 
 
D:\>mkdir djangoprojects 
 
D:\>cd djangoprojects 
 
D:\djangoprojects>django-admin start-project firstProject 
 
The following project structure will be created 
 
D:\djangoprojects> 
 | 
 +---firstProject 
    ¦    
    ¦---manage.py 
    ¦ 
    +---firstProject 
        ¦---settings.py 
        ¦---urls.py 
        ¦--wsgi.py 
        ¦-- __init__.py 
 
         
__init__.py: 
It is a blank python script.Because of this special file name, Django treated this folder as 
python package. 
 
Note: If any folder contains __init__.py file then only that folder is treated as Python 
package.But this rule is applicable until Python 3.3 Version. 
settings.py: 
In this file we have to specify all our project settings and and configurations like 
installed applications, middileware configurations, database configurations etc 
 
urls.py: 
 Here we have to store all our url-patterns of our project. 
 For every view (web page), we have to define separate url-pattern. End user can use 
url-patterns to access our webpages. 
 
wsgi.py: 
 wsgi  Web Server Gateway Interface.  
 We can use this file while deploying our application in production on online server. 
 
manage.py: 
 The most commonly used python script is manage.py 
 It is a command line utility to interact with Django project in various ways like to run 
development server, run tests, create migrations etc. 
 
How to Run Django Development Server: 
 
We have to move to the manage.py file location and we have to execute the following 
command. 
 
py manage.py runserver 
 
D:\djangoprojects\firstProject>py manage.py startserver 
 
Performing system checks... 
 
System check identified no issues (0 silenced). 
 
You have 13 unapplied migration(s). Your project may not work properly until you apply 
the migrations for app(s): admin, auth, contenttypes, sessions. 
Run 'python manage.py migrate' to apply them. 
August 03, 2018 - 15:38:59 
Django version 1.11, using settings 'firstProject.settings' 
Starting development server at http://127.0.0.1:8000/ 
Quit the server with CTRL-BREAK. 
 
Now the server started. 

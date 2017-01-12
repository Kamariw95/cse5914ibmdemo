# cse5914ibmdemo
A project using Python and IBMs Alchemy API to search on news articles via the terminal.


Steps to running application:
-----------------------------

1. Make sure **pip** is installed on your machine.
  - Link to directions: https://pip.pypa.io/en/stable/installing/
2. Make sure **virtualenv** is installed on your machine.
  - Link to directions: https://virtualenv.pypa.io/en/stable/installation/

3. Open the Terminal and use the `cd` command to go into the **cse5914ibmdemo** folder
4. Run these commands:
  - `virtualenv env`
  - `source env/bin/activate`
  - `pip install -r requirements/base.txt`

5. Once those finish, use the `cd` command again to go into the **alchemy_site** folder (The one with **manage.py** in it).
6. Create a file called **hidden.py** inside of **../alchemy_site/main/alchemy_service/alchemy_settings** that has a variable called `API_KEY`.
7. Place the value for the `API_KEY` for that variable.
8. Run this command: `python manage.py runserver` in the Terminal

**The app should run without problems!**

**NOTE:** Going forward, you'll have to run this to run the application:
  - `source env/bin/activate` in the **cse5914ibmdemo** folder, with the **env** folder.
  - `python manage.py runserver` in the **alchemy_site** folder, where the **manage.py** file is.

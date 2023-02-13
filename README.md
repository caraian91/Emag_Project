# Emag Selenium Project

📚
Site tested: emag.ro\
Design pattern used: Page Object Model (POM)\
Methodology: Test Driven Development (TDD)

📝 
To import project\
1.Click on the right button Code-> we copy the url \
2.We open a folder in our laptop where we want to import the project (important to have Git installed on our computer)\
3.Right click-> Git Bash Here-> in the console we write the command: git clone (put the link before clone from click on Code->copy link) \
4.Done -> The project has been imported.

📝 
Commands in **cmd** file for **Behave** and **Selenium**\
Libraries to install:
* pip install -u selenium
* pip install behave
* pip install behave-html-formatter
* pip install webdriver-manager

📝 
To run the BDD tests use in **Terminal**:
* behave -f html -o behave-report.html

Happy Testing!

\
\
⏩
Troubleshoot:\
a. If it doesn't work with pip, try the command:  
* py -m pip install selenium\

b. If that doesn't work either:\
* File -> Settings -> Click pe Project: [name_project] -> Python Interpreter -> +
Search 'selenium' -> Install Package\
The same for the rest of the Libraries

c. In the last instance, you create a new project, install what you need with pip and manually copy the necessary folders and files. 

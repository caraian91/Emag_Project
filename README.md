Emag BDD Automation Framework

📚
Site tested: emag.ro\
Design pattern used: page object model\
Methodology: behavior driven development

To import project\
-> git clone (put the link before clone from click on Code->copy link)

📝 
Commands in **cmd** file for **Behave** and **Selenium**\
Libraries to install:
* pip install -u selenium
* pip install behave
* pip install behave-html-formatter
* pip install webdriver-manager

📝 
To run the BDD tests use in **Terminal**:
* behave -f html -o behave-report.html --tags=emag

Happy Testing!


\
\
⏩
Troubleshoot:\
a. If it doesn't work with pip, try the command:  
* py -m pip install selenium\

b. If that doesn't work either:\
* File -> Settings -> Click pe Project: [nume_proiect] -> Python Interpreter -> +
Cautati 'selenium' -> Install Package\
The same for the rest of the Libraries

c. In the last instance, you create a new project, install what you need with pip and manually copy the necessary folders and files.
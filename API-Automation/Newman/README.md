# Newman Command line tool to the run POSTMAN collection
### API Testing Dashboard 

**To run Newman into your machine you need to install some tools**

- Download -> NodeJS -> [﻿nodejs.org/en/download/prebuilt-installer](https://nodejs.org/en/download/prebuilt-installer) 
- check on cmd -> node --version
- check on cmd -> npm --version
- install on cmd -> npm -g i newman
- install on cmd -> npm -g i newman-reporter-htmlextra
- Download / export Postman collection on your local machine
- save it on your Downloads or other folder
- go to downloads folder and type cmd in search bar
- cmd will open type -> newman run "Postman Collection Example" -r cli,htmlextra
- it will start running all test cases and it will create a folder which name is newman
- go to newman folder and open it. you will get html page 
- double click on html page it will redirect to your browser
- then it will show you beautiful api testing Dashboard, title is Newman Run Dashboard

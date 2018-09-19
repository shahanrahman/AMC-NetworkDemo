# AMC-NetworkDemo

Overview of current pages as follows: 

base/selenium_driver.py -- contains all custom built methods to be used across the framework. 
Custom methods avoids long and confusing lines of code.

pages/home/ *.py -- Contain custome built xpaths as identifiers for each page as well as functionality to be performed on each page.
This folder will need massive updates upon approval of framework type. 

test/home/*.py -- contains test cases to be executed. 

utilities/logger.py -- contains logging function which is used across all test cases. Please see shudder.log to vuew full logging. currently it is setup in debug mode which will 
print all test steps executed along with elements selected. 



Test Cases: 

TC01 -- Valid Login 

1. Navigate to www.Shudder.Com/login 
2. login using correct credentials 
3. Click Login and navgate to home page 
4. Verify login successful
5. Click and navigate to 'My Account' 
6. Log out 

TC02 -- Invalid Login 
1. Navigate to www.Shudder.Com/login 
2. login using incorrect credentials 
3. Click Login
5. Verify user is displayed invalid credentials message 

To Execute the TC01 && TC02 using pyCharm via Terminal enter the following 'py.test -s -v tests/home/Login_tests.py' 
Please note this will first execute valid login first and once logged out it will continue on to TC02. 

------------------------------------------------


TC03 -- Home Page Header link verification 
1. Navigate to www.Shudder.Com/login 
2. login using correct credentials 
3. Click Login and navgate to home page 
4. Verify login successful
5. First Validate all header links are avilable 
6. Click on each header link and navigate to each page 

To Execute the TC03 using pyCharm via Terminal enter the following 'py.test -s -v tests/home/MembersPage_tests.py 


TC-04 -- Search Movie on Shudder
 This test case is going to do excatly what the title states. 
 
 1. Login and verify login successful 
 2. Execute all test described in TC03 
 3. Navigate to search and search for movie starting with 'dead' (this can be updated directly in the test case and is not hard coded)



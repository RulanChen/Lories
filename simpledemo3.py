import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Current Version 0.100
#V0.100 Add Browser Auto input and processing Demo code;
#Please add thread based time clock function in next version,
#I think you may need this function to manage your agent command send with time change,etc.
driver = webdriver.Firefox()
driver.get("http://192.168.0.5:8888/DEMO/")#set your server address here
assert "Test_Final" in driver.title
elem = driver.find_element_by_name("q")#get action input element here
sensory = driver.find_element_by_name("q2")#get sensory information element here
#tips:myInput is used for general command send(u:up,d:down,l:left,r:right,q:stop,g:continue,s:laser,o:degree scan);
#myInput2 is used for speed set,can set from 0 to +oo value
#myInput3 is used for self status check and action input(action is not implemented yet),(self status command is v,it will return Stand_up,Stand_left,Stand_right,Stand_down,Go_up,Go_down,Go_left,Go_right)
#myTextarea it used to show sensor scan results, when the s type command send, it return 0, and after this sensor hit with the wall will return 1; o type command will return 9 when it send, if it hit with the wall return 1.
#myTextarea1 at this time it only used to display agent self status check results,Stand_up,Stand_left,Stand_right,Stand_down,Go_up,Go_down,Go_left,Go_right
#myTextarea2 if s  command scan the object, it will return this object gray-level matrix here,later you can used it in classification part.
while True:#main loop, start your AI code here;<here is some demo code>
    #sensory.get_attribute("value") is used to got agent sensor information,
    #infor=sensory.get_attribute("value")
    #infor=int(infor)
    #here is a simple demo,modify it to your own AI code
    #if (infor ==0):
    elem.send_keys("l")
        #else:
        ##elem.send_keys("r")
    elem.send_keys(Keys.RETURN)

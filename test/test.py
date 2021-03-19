import OMDriver.OMDriver as driver #importing the OMDriver

token="<YOUR_TOKEN>" #Enter Your Unique Token here
project_id="<PROJECT_ID>" #Enter the project ID
headers = {
            "private_key": token,
            "content-type": "application/json"
        } #Creating a Json Header for API Call

call=driver.OMDriver(headers,project_id) #Initiating the Class parameterized constructor
print(call.getData(module="<MODULE_NAME>",page="<PAGE_NAME>",object="<OBJECT_NAME>",attribute="<ATTRIBUTE_NAME>")) #Getting Specific attribute
print(call.getData(module="<MODULE_NAME>",page="<PAGE_NAME>",object="<OBJECT_NAME>")) #Getting Specific Object's Attributes
print(call.getData(module="<MODULE_NAME>",page="<PAGE_NAME>")) #Getting Specific Page's Objects and Attributes
print(call.getData(module="<MODULE_NAME>")) #Getting Specific module's pages,objects and attributes
print(call.getData(attribute="<ATTRIBUTE_NAME>")) #Getting all possible attributes
print(call.getData(object="<OBJECT_NAME>",attribute="<ATTRIBUTE_NAME>")) #Getting all possible attributes Under Specific Object
'''
 Vice Versa You can find any Specific Keys or Values
'''

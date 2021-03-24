# OMDriver
Simplify Object Manager, a **FREE cloud based** Object Repository making it easier for you to **build, manage and maintain** test objects. SimplifyOM helps you achieve a smoother team collaboration and significantly cut down on your time and efforts spent across the testing process / test automation.

 

To begin with SimplifyOM, kindly check out our [YouTube][https://www.youtube.com/channel/UCec7wlOfvGKTfwNloSApryQ/playlists] videos and follow the tutorial.

 

Having SimplifyOM as a part of your testing process / test automation will help you relish the following benefits

 

Cloud based Object Repository: Significantly cut down on your time and effort spent on merging, resolving duplicate/redundant objects and maintaining them -- helping your team make the most out of their time.

 

**Smoother Integration with your Existing Framework**: SimplifyOM SDK is a perfect solution for integrating your existing framework to SimplifyOM Object Repository enabling you:  

* Ease Object Repository Management by eliminating the need to maintain a local repository
* Central repository leading to better team collaboration
 

**Organizing your Objects across Projects**: Now save your valuable time by grouping the related page, making object repository management and maintenance easier.

 

**Object Identification made easier**: We identify all possible web attributes for you to carry out flawless automation. Not just that, we also offer you tailor made css and multiple xpaths thus relieving you from the never ending activity of scratching your head with objects. 

 

**Team Collaboration**: As a cloud based object repository you can now collaborate and manage your project teams effortlessly and help them carry out the automation tasks quickly within the applications they already use.  

## Getting Started

Checklist to get started with SimplifyOM!!

* Login to your SimplifyOM account or register a new one
* Obtain a development token from Profile Section in SimplifyOM.

### Prerequisites

Make Sure Python3 is installed.

### Installing

OMDriver Can be directly installed using pip.

```
pip install OMDriver
```

## Running the tests
```
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
```
## ScreenShots


## Authors

* **Simplify3x** - *Initial work* - [Github](https://github.com/Simplify3x)


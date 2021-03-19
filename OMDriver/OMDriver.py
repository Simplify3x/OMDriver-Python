import requests
import json
def get_modules(url,headers,project_id,module=None,page=None,object=None,attribute=None):
    modules=dict()
    flag=False
    page_url = url + "/" + project_id + "/modules"
    response=requests.get(page_url,headers=headers)
    tmp=response
    response=response.json()
    count=0
    flag2=False
    modules2=dict()
    error=""
    if tmp.status_code == 200:
        for i in response["data"]:
            if module==None :
                modules2["name"]=i["name"]
                modules2["pages"]=get_pages(url,headers,project_id,i["name"],page,object,attribute)
                if type(modules2)!=str  and type(modules2)!=dict:
                    error = modules2["error"]
                    pass
                else:
                    modules[str(count)] = json.dumps(modules2)
                    count=count+1
                    flag2=True
            else:

                if module==i["name"]:
                    modules2 = get_pages(url, headers, project_id, i["name"], page,object,attribute)
                    if type(modules2)!=str  and type(modules2)!=dict:
                        error=modules2["error"]
                        pass
                    else:
                        flag = True
                        modules=modules2
                        flag2=True
                        break
    else:
        modules["error"]="Invalid Token"
    if flag2==False:
        modules["error"] = error
    if(flag==False and module!=None):
        modules["error"] = "Could'nt Find the Given module"

    return modules

def get_pages(url,headers,project_id,module=None,page2=None,object=None,attribute=None):
    pages=dict()
    flag=False
    flag2=False
    page_url=url+"/"+project_id+"/page"
    param = {
            "module": module
        }
    response=requests.get(page_url,headers=headers,params=param)
    response = response.json()
    count = 0
    page=dict()
    error=""
    for i in response["data"]:
        if page2==None:
            page["name"]=i["name"]
            page["objects"]=get_objectsandAttributes(url,headers,project_id,module,page2,object,attribute)
            if type(page)!=str  and type(page)!=dict:
                error = page["error"]
                pass
            else:
                pages[str(count)] = json.dumps(page)
                count = count + 1
                flag2=True
        else:

            if page2==i["name"]:
                page = get_objectsandAttributes(url, headers, project_id, module, page2,object,attribute)
                if type(page)!=str  and type(page)!=dict :
                    error=page["error"]
                    pass
                else:
                    pages=page
                    flag=True
                    flag2=True
                    break
    if flag==False and page2!=None:
        pages["error"] = "Could'nt Find the Given page"
    elif flag2==False:
        pages["error"] = error
    return pages


def get_objectsandAttributes(url,headers,project_id,module=None,page=None,object=None,attribute=None):
    objects=dict()
    page_url = url + "/" + project_id + "/objects"
    flag=False
    if page == None:
        param={
                "module" : module
            }
        response = requests.get(page_url, headers=headers, params=param)
    else:
        param = {
                "module" : module,
                "page" : page
            }
        response = requests.get(page_url, headers=headers, params=param)
    tmp=response
    response = response.json()
    objects2=dict()
    count = 0
    flag_2=False
    if tmp.status_code == 200:
        for i in response["data"]:
            if object==None:
                if attribute==None:
                    objects2["name"]=i["name"]
                    objects2["attributes"]=i["attributes"]
                    objects[str(count)]=json.dumps(objects2)
                    count=count+1
                else:
                    for y in i["attributes"]:
                        if y["name"] == attribute:
                            objects2["name"] = i["name"]
                            objects2["attributes"]={"name" : y["name"],"value" : y["value"]}
                            objects = json.dumps(objects2)
                            flag_2=True
                            break


            else:
                if object==i["name"]:
                    flag=True
                    if attribute==None:
                        objects2 = i["attributes"]
                        objects= json.dumps(objects2)
                    else:
                        for y in i["attributes"]:
                            if y["name"]==attribute:
                                objects2= y["value"]
                                objects=json.dumps(objects2)
                                flag_2=True
                                break

        if flag==False and object!=None:
            objects["error"] = "Could'nt Find the Given Object or Attribute"
        if flag_2==False and attribute!=None and flag==True:
            objects["error"] = "Could'nt Find the Given Attribute or Attribute"
    else:
        objects["error"]="Could'nt Find the Given page"
    return objects

class OMDriver:
    def __init__(self,page_url,headers,project_id):
        self.page_url=page_url
        self.headers=headers
        self.project_id=project_id
        self.localstorage=dict()

    def getData(self,module=None,page=None,object=None,attribute=None):
        key=""
        if module!=None:
            key=key+module
        if page!=None:
            key=key+page
        if object!=None:
            key=key+object
        if attribute!=None:
            key=key+attribute
        key = self.headers["private_key"] + self.project_id + key
        if key in self.localstorage.keys():
            response=self.localstorage[key]
        else:
            response=get_modules(self.page_url,self.headers,self.project_id,module,page,object,attribute)
            self.localstorage[key]=response

        return response


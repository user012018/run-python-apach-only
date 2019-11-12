#!D:\Program\Python27\python.exe
# -*- coding: UTF-8 -*-
# //coding: utf-8
# coding=utf-8
# vim: set fileencoding=utf-8 :
print "Content-Type: text/html\r\n"
#~ print ("<meta charset="utf-8">")


import urllib2,json
import xmltodict
import locale,os
language, output_encoding = locale.getdefaultlocale()

from lxml import etree
from json2html import *


# 6.35
print('----')

dictlist={u'photo': {u'access_key': u'e921562897161088a9', u'src': u'https://pp.userapi.com/c840330/v840330414/40cb7/tA2sLhxEWLw.jpg', u'user_id': 100, u'src_xbig': u'https://pp.userapi.com/c840330/v840330414/40cb9/6N3O-lKoxh4.jpg', u'text': u'', u'created': 1515289000, u'pid': 456246228, u'height': 960, u'src_xxbig': u'https://pp.userapi.com/c840330/v840330414/40cba/Cucxvz4JFxs.jpg', u'width': 960, u'src_big': u'https://pp.userapi.com/c840330/v840330414/40cb8/vzFVj3KZb8U.jpg', u'src_small': u'https://pp.userapi.com/c840330/v840330414/40cb6/GcQ9GTLpuIE.jpg', u'aid': -7, u'post_id': 51954, u'owner_id': -100693264}, u'type': u'photo'}

dictlist=[{"title":"NAME","field":"NAME","responsive":0},{"title":"ARTICUL","field":"ARTICUL","responsive":0},{"title":"PRICE","field":"PRICE","responsive":0},{"title":"OSTATOK","field":"OSTATOK","responsive":0}]



jsonstring=json.dumps(dictlist)
print json2html.convert(json = jsonstring).encode('UTF-8')







jsonstring=json.dumps([
    {"id":1, "name":"Oli Bob", "progress":12, "location":"United Kingdom", "gender":"male", "rating":1, "col":"red", "dob":"14/04/1984", "car":1, "lucky_no":5, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":2, "name":"Mary May", "progress":1, "location":"Germany", "gender":"female", "rating":2, "col":"blue", "dob":"14/05/1982", "car":"true", "lucky_no":10, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":3, "name":"Christine Lobowski", "progress":42, "location":"France", "gender":"female", "rating":0, "col":"green", "dob":"22/05/1982", "car":"true", "lucky_no":12, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":4, "name":"Brendon Philips", "progress":100, "location":"USA", "gender":"male", "rating":1, "col":"orange", "dob":"01/08/1980", "car":false, "lucky_no":18, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":5, "name":"Margret Marmajuke", "progress":16, "location":"Canada", "gender":"female", "rating":5, "col":"yellow", "dob":"31/01/1999", "car":false, "lucky_no":33, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":6, "name":"Frank Harbours", "progress":38, "location":"Russia", "gender":"male", "rating":4, "col":"red", "dob":"12/05/1966", "car":1, "lucky_no":2, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":7, "name":"Jamie Newhart", "progress":23, "location":"India", "gender":"male", "rating":3, "col":"green", "dob":"14/05/1985", "car":true, "lucky_no":63, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":8, "name":"Gemma Jane", "progress":60, "location":"China", "gender":"female", "rating":0, "col":"red", "dob":"22/05/1982", "car":"true", "lucky_no":72, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":9, "name":"Emily Sykes", "progress":42, "location":"South Korea", "gender":"female", "rating":1, "col":"maroon", "dob":"11/11/1970", "car":false, "lucky_no":44, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    {"id":10, "name":"James Newman", "progress":73, "location":"Japan", "gender":"male", "rating":5, "col":"red", "dob":"22/03/1998", "car":false, "lucky_no":9, "lorem":"Lorem ipsum dolor sit amet", "elit consectetur adipisicing "},
    ])
print json2html.convert(json = jsonstring).encode('UTF-8')


jsonthrow=json.dumps([{"NAME":"\u0410\u041a\u041a\u0423\u041c\u0423\u041b\u042f\u0422\u041e\u0420","ARTICUL":"000915105CC","PRICE":"19\u00a0450,00","OSTATOK":"1,00"},{"NAME":"\u0422\u0415\u0420\u041c\u041e-\u0422\u041e\u0420\u0426\u0415\u0412\u041e\u0419 \u0421\u041e\u0415\u0414\u0415\u041d\u0418\u0422\u0415\u041b\u042c","ARTICUL":"000979940","PRICE":"240,00","OSTATOK":"74,00"},{"NAME":"\u0422\u0415\u0420\u041c\u041e-\u0422\u041e\u0420\u0426\u0415\u0412\u041e\u0419 \u0421\u041e\u0415\u0414\u0415\u041d\u0418\u0422\u0415\u041b\u042c","ARTICUL":"000979941","PRICE":"225,00","OSTATOK":"47,00"}])
# print json2html.convert(json = jsonstring).encode('UTF-8')
print json2html.convert(json = jsonthrow)



# print(type([{"title":"NAME","field":"NAME","responsive":0},{"title":"ARTICUL","field":"ARTICUL","responsive":0},{"title":"PRICE","field":"PRICE","responsive":0},{"title":"OSTATOK","field":"OSTATOK","responsive":0}]))

jsonthrow=json.dumps(
[{'title':"Name", 'field':"name"},
    {'title':"Progress", 'field':"progress", 'align':"right", 'sorter':"number"},
    {'title':"Gender", 'field':"gender"},
    {'title':"Rating", 'field':"rating", 'align':"center"},
    {'title':"Favourite Color", 'field':"col"},])
# print json2html.convert(json = jsonstring).encode('UTF-8')
print('<hr>----------------------------<br>')
print json2html.convert(json = jsonthrow)



columns=[
    {"formatter":"responsiveCollapse", "width":30, "minWidth":30, "align":"center", "resizable":"false", "headerSort":"false"},
    {"title":"Name", "field":"name", "width":200, "responsive":0},
    {"title":"Progress", "field":"progress", "align":"right", "sorter":"number", "width":150},
    {"title":"Gender", "field":"gender", "width":150, "responsive":2},
    {"title":"Rating", "field":"rating", "align":"center", "width":150},
    {"title":"Favourite Color", "field":"col", "width":150},
    {"title":"Date Of Birth", "field":"dob", "align":"center", "sorter":"date", "width":150},
    {"title":"Driver", "field":"car", "align":"center", "width":150},
    ]

jsonstring=json.dumps(columns)
print('<hr>----------------------------<br>')
print json2html.convert(json = jsonstring).encode('UTF-8')




columns=[
    {"title":"Name", "field":"name", "width":200, "responsive":0}, #//never hide this column
    {"title":"Progress", "field":"progress", "align":"right", "sorter":"number", "width":150},
    {"title":"Gender", "field":"gender", "width":150, "responsive":2}, #//hide this column first
    {"title":"Rating", "field":"rating", "align":"center", "width":150},
    {"title":"Favourite Color", "field":"col", "width":150},
    {"title":"Date Of Birth", "field":"dob", "align":"center", "sorter":"date", "width":150},
    {"title":"Driver", "field":"car", "align":"center", "width":150}
    ]

jsonstring=json.dumps(columns)
print('<hr>----------------------------<br>')
print json2html.convert(json = jsonstring).encode('UTF-8')




tableDataNested = [
    {"name":"Oli Bob", "location":"United Kingdom", "gender":"male", "col":"red", "dob":"14/04/1984", "_children":[
        {"name":"Mary May", "location":"Germany", "gender":"female", "col":"blue", "dob":"14/05/1982"},
        {"name":"Christine Lobowski", "location":"France", "gender":"female", "col":"green", "dob":"22/05/1982"},
        {"name":"Brendon Philips", "location":"USA", "gender":"male", "col":"orange", "dob":"01/08/1980", "_children":[
            {"name":"Margret Marmajuke", "location":"Canada", "gender":"female", "col":"yellow", "dob":"31/01/1999"},
            {"name":"Frank Harbours", "location":"Russia", "gender":"male", "col":"red", "dob":"12/05/1966"},
        ]},
    ]},
    {"name":"Jamie Newhart", "location":"India", "gender":"male", "col":"green", "dob":"14/05/1985"},
    {"name":"Gemma Jane", "location":"China", "gender":"female", "col":"red", "dob":"22/05/1982", "_children":[
        {"name":"Emily Sykes", "location":"South Korea", "gender":"female", "col":"maroon", "dob":"11/11/1970"},
    ]},
    {"name":"James Newman", "location":"Japan", "gender":"male", "col":"red", "dob":"22/03/1998"},
];

jsonstring=json.dumps(tableDataNested)
print('<hr>-----tableDataNested-----------------------<br>')
print json2html.convert(json = jsonstring).encode('UTF-8')



nestedTablesTablesData = [
    {"id":1, "make":"Ford", "model":"focus", "reg":"P232 NJP", "color":"white", "serviceHistory":[
       {"date":"01/02/2016", "engineer":"Steve Boberson", "actions":"Changed oli filter"},
       {"date":"07/02/2017", "engineer":"Martin Stevenson", "actions":"Break light broken"},
    ]},
    {"id":1, "make":"BMW", "model":"m3", "reg":"W342 SEF", "color":"red", "serviceHistory":[
       {"date":"22/05/2017", "engineer":"Jimmy Brown", "actions":"Aligned wheels"},
       {"date":"11/02/2018", "engineer":"Lotty Ferberson", "actions":"Changed Oil"},
       {"date":"04/04/2018", "engineer":"Franco Martinez", "actions":"Fixed Tracking"},
    ]},
]


jsonstring=json.dumps(nestedTablesTablesData)
print('<hr>-----tableDataNested-----------------------<br>')
print json2html.convert(json = jsonstring).encode('UTF-8')







exit()





def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
#~ a = a.decode('utf-8').encode('cp1251') 
#~ print u'1\u0430'.encode('UTF-8').decode('UTF-8').encode('cp1251') 
pathfilearchivfile='d:/webserver/domains/localhost/.idea/workspace.xml'
pathfilearchivfile='import.txt'
#~ with open("fromZET_Source_speciallllllllllll111111_.xml", 'r') as content_file:
with open(pathfilearchivfile, 'r') as content_file:
    data = content_file.read()

#~ file = urllib2.urlopen("D:/1C/fromZET_Source_тестхим111111.xml")
#~ data = file.read()
#~ file.close()
data=data




#~ bolsoispisok=[]
data = (json.dumps(xmltodict.parse(data)))
data = json.loads(data)

# data=data['project']['component']
# data=data[u'\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f'][u'\u041a\u0430\u0442\u0430\u043b\u043e\u0433']
data=data[u'\u041a\u043e\u043c\u043c\u0435\u0440\u0447\u0435\u0441\u043a\u0430\u044f\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f'][u'\u041a\u0430\u0442\u0430\u043b\u043e\u0433'][u'\u0422\u043e\u0432\u0430\u0440\u044b']
# print(len(data))
# print (data.keys())
try:
    pass
    # data=data[u'\u0424\u0430\u0439\u043b\u041e\u0431\u043c\u0435\u043d\u0430']
except Exception as e:
    error=1
    #~ print (e)
# del data['leaf']
# del data[u'@ВерсияФормата']
# del data[u'@ИмяКонфигурацииИсточника']



# exit()

# del data[0]

from json2html import *
dictlist={u'photo': {u'access_key': u'e921562897161088a9', u'src': u'https://pp.userapi.com/c840330/v840330414/40cb7/tA2sLhxEWLw.jpg', u'user_id': 100, u'src_xbig': u'https://pp.userapi.com/c840330/v840330414/40cb9/6N3O-lKoxh4.jpg', u'text': u'', u'created': 1515289000, u'pid': 456246228, u'height': 960, u'src_xxbig': u'https://pp.userapi.com/c840330/v840330414/40cba/Cucxvz4JFxs.jpg', u'width': 960, u'src_big': u'https://pp.userapi.com/c840330/v840330414/40cb8/vzFVj3KZb8U.jpg', u'src_small': u'https://pp.userapi.com/c840330/v840330414/40cb6/GcQ9GTLpuIE.jpg', u'aid': -7, u'post_id': 51954, u'owner_id': -100693264}, u'type': u'photo'}
jsonstring=json.dumps(data)
print json2html.convert(json = jsonstring).encode('UTF-8')




stoplist=['FileEditorManager'
           ,'DatabaseView' 
           ,'BookmarkManager'
           ,'ChangeListManager'
           ,'FUSProjectUsageTrigger'
           ,'IdeDocumentHistory','JsBuildToolGruntFileManager','JsBuildToolPackageJson','JsGulpfileManager'
           ,'ProjectView'
           ,'ToolWindowManager'
           ,'XDebuggerManager'
           ,'editorHistoryManager'
           ,'FUSProjectUsageTrigger'
            ]

# for k,v in data.items():
    # begin=1
    #~ print(k, 'corresponds to', v)
for i,v in enumerate(data):
    pass
    # print((v['@name']),'<br>')
    # print('leaf' in v.keys())
    # if 'leaf' not in v.keys(): # [u'leaf', u'@name']
    # if v['@name'] in stoplist:
        # del data[i]
        # pass
    
        # print(v.keys())
        # del data[i]
    # print((v.keys()))
        # print('--------------')


# for i,v in enumerate(data):
    # print data[i]
    # print('--------------')



try:
    pass
    # data=data[u'project']
except Exception as e:
    error=1

    
#~ d.values()[i]    
#~ print data.keys()
#~ print data.items()[49]  
#~ for x in data.keys():
lslocal=[]

for x in data:
    begin=1
    #~ x[u'@Тип']=''
    
    #~ x[u'Свойство']=''
    lslocal.append(x)
    try:
        trying=1
        #~ print x[u'@Тип'].encode('UTF-8').decode('UTF-8').encode('cp1251')

    except Exception as e:
        error=1
        #~ print x[u'@Тип']
        #~ print (e)
    
try:
    data=lslocal
except Exception as e:
    error=1


exit()







from json2html import *
dictlist={u'photo': {u'access_key': u'e921562897161088a9', u'src': u'https://pp.userapi.com/c840330/v840330414/40cb7/tA2sLhxEWLw.jpg', u'user_id': 100, u'src_xbig': u'https://pp.userapi.com/c840330/v840330414/40cb9/6N3O-lKoxh4.jpg', u'text': u'', u'created': 1515289000, u'pid': 456246228, u'height': 960, u'src_xxbig': u'https://pp.userapi.com/c840330/v840330414/40cba/Cucxvz4JFxs.jpg', u'width': 960, u'src_big': u'https://pp.userapi.com/c840330/v840330414/40cb8/vzFVj3KZb8U.jpg', u'src_small': u'https://pp.userapi.com/c840330/v840330414/40cb6/GcQ9GTLpuIE.jpg', u'aid': -7, u'post_id': 51954, u'owner_id': -100693264}, u'type': u'photo'}
jsonstring=json.dumps(data)
print json2html.convert(json = jsonstring).encode('UTF-8')

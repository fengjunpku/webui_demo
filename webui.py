#!/bin/python
#coding=utf-8
import web
import time
import commands
import platform
from web import form

# resource & template
render = web.template.render('templates', base='base')
config = web.storage(static='static')
# url mapping
urls = (
  '/', 'index',
  '/load','load',
  '/run','run'
)
#system name
sysstr = platform.system()
#
myform = form.Form( 
  form.Textbox("boe"), 
  form.Textbox("bax", 
    form.notnull,
    form.regexp('\d+', 'Must be a digit'),
    form.Validator('Must be more than 5', lambda x:int(x)>5)),
  form.Textarea('moe'),
  form.Checkbox('curly'), 
  form.Dropdown('french', ['mustard', 'fries', 'wine'])) 

def ShowPage(pageName):
  dir = 'templates/'
  fileName = dir+pageName+'.html'
  file = open(fileName)
  try:
    content = file.read()
  finally:
    file.close()
  return content

def showabout():
  return render.about()

class index: 
  def GET(self): 
    return render.index()
  def POST(self): 
    return 'x'

class load:
  def GET(self):
    return 'REJECTION'
  def POST(self):
    pagename = web.input().get('page')
    if pagename == 'about' or pagename == 'home':
      return ShowPage(pagename)
    else:
     return  pagename

class run:
  def GET(self):
    return 'REJECTION'
  def POST(self):
    commandname = web.input().get('cmd')
    timeflag = time.time()
    timestruc = time.localtime(timeflag)
    timestr = time.strftime('%Y-%m-%d %H:%M:%S',timestruc)
    if sysstr == "Windows":
      return timestr+'<br>'+sysstr+'<br>Please use in Linux'
    elif sysstr == "Linux":
      (statuscode, output) = commands.getstatusoutput(commandname)
      if statuscode == 0:
        status = '[Sucessed to Run CMD]: '+ str(commandname)
      else:
        status = '[Failed to Run CMD]: '+ str(commandname)
        return timestr+'<br>'+sysstr+'<br>'+str(status)+'<br>'+output+'<br>'
    else:
      return timestr+'<br>'+sysstr+'<br>Please use in Linux'

if __name__=="__main__":
  web.internalerror = web.debugerror
  app = web.application(urls, globals())
  app.run()

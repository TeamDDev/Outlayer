# Outlayer [In progress]

Aim: A web-based software to easify the task of recording the daily expenses and keeping track of daily budget aka **budget-tracker system**.
<br /> 
<br />
Easy to build and manage.
<br />
<br />
Can run over the local server and can be used as a tool, accessible from anywhere after being deployed.
<br />

## **Technology used** : Django, HTML, CSS

## Installation
In your terminal type: 
```git clone https://github.com/TeamDDev/Outlayer.git```
* Open in Visual Studio to build and run.
* For further instructions, visit https://help.github.com


## Our Code Organization:
```
Outlayer/            <-- Repo name
  |---outlayer/             <-- Project Outlayer root
  |    |--- outlayer/                <-- Django root
  |    |     |--- __init__.py
  |    |     |--- asgi.py
  |    |     |--- settings.py 
  |    |     |--- urls.py
  |    |     |--- wsgi.py  
  |    |--- tracker/                  <-- Outlayer app
  |    |     |--- migrations
  |    |     |--- static/css/
  |    |     |      |--- login
  |    |     |      |--- signup
  |    |     |
  |    |     |--- templates/
  |    |     |      |--- regiseration
  |    |     |
  |    |     |--- __init__.py
  |    |     |--- admin.py
  |    |     |--- apps.py
  |    |     |--- forms.py
  |    |     |--- models.py (Database model)
  |    |     |--- tests.py
  |    |     |--- urls.py
  |    |     |--- views.py 
  |    |--- manage.py
  |
  |--- MOMs
  |--- BACKLOGs
  |--- README
       
```

## Working of the Code:
```
                                               ____ templates
                                              /
                                             /
                                            /
         REQUEST ---- urls.py ----- views.py 
                                            \
                                             \
                                              \_____ models.py
```
(The project is still under construction and the instantiation of the project will be updated here once completed).
<br /> 
<br />
**Check out Blogs for more information:**
https://d-dev.medium.com/out-layer-94faca9187c4


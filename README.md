# Template to build python package

This project is a copy/paste template that can be used to create python packages

With this project, you will be able to create a python library that anyone in the team can install with pip with this
kind of command:

```
pip install libname
```

This project will allow you to package your python scripts and distribute them easily to your peers.

If you manage to master this project, you will be able to share your python scripts with the world (and with your team first :p) 

This project allows you to transform your python scripts into a python pip library. 
If you want to integrate your python library with needl.link, there are some additional requirements. 
In this case, read this [documentation](https://wabel.atlassian.net/l/c/i1RzoWhr)

## 0.Quick start

To quickly start developing your python library, follow these steps:

1. Clone the project
```
git clone git@github.com:needl-app/ExternalScriptForNeedLink.git
```
2. Go in the project directory
```
cd ExternalScriptForNeedLink
```
3. Create virtual env
```
python3 -m venv venv
```
4. Install the library you are developing and its dependencies ( requirements )
```
pip install -e .
```
5. Test name_of_your_service_1 service
```
 python libname/name_of_your_service_1/main.py 
```
6. Modify the project to do the job you want it to do
   1. Check project architecture and make sure to follow best practices
   2. Check main.py file of package name_of_your_service_1 to see some examples
      1. you have example of how to connect to a database
      2. you have example of how to load of conf.ini file
      3. you have example of how to use a module from another package
   3. Change service name
   4. Put the logic of your service in main.py
   5. Put the conf you need to configure the service in conf.ini
   6. Update setup.py
   7. Publish your code in a git repository

   8. Install your new custom libray in another python project
```
 pip install git+ssh://git@github.com/needl-app/ExternalScriptForNeedLink.git#c4c147de0580bbe3ff9fd311bf1ab6284e7e21fc/id_rsa
```
Make sure to update the repo url and the commit id after the # symbol. 
And make sure that the id_rsa public key is added to gihtub

7. Call the name_of_your_service_1 service in another python project
```
 from libname.name_of_your_service_1 import main
 main.run() # it will launch your service in ahoter python projet
```

## 1.Project architecture

```
libname/
├── name_of_your_service_1
│   ├── config
│   ├── conf.ini
│   ├── data
│   ├── __init__.py
│   ├── name_of_your_module_y.py
│   └── __pycache__
└── name_of_your_service_2
    ├── conf.ini
    ├── data
    ├── __init__.py
    ├── name_of_your_module_x.py
    └── __pycache__

```

libname is the name of your library. The name we will use in pip install.

Then, we have packages:

- name_of_your_service_1
- name_of_your_service_2

A package ( a folder ) is a set of python modules ( files ).

You can create as many packages as you like. One or more.

To facilitate the maintenance of your application, you should try to follow this good practice:

- A package should be seen as a service. This package must provide only one service.
- A package should ideally contain a single module. The main.py module
- The package could contain a data folder we can be used to store sql queries, csv files (everything that is not code)
- The main.py module should contain a run function. This is the only function to call to start the service.
- The main.py module can be tested quickly with this command: python main.py
- All service configurations must be done in the conf.ini file
- The run function should have only one optional arguments which is the path to an external conf file.
- The env file should not be loaded in the library  but by the user before calling your library.

A service (a package) can call the service of another package.

Some tips:
- if you changed the name of the libray, you need to update setup.p
- if you changed the name of a service, you need to update setup.py
- if you added a service, you need to update setup.py

## 2.To develop locally

To test your script locally, consider installing it locally. This allows you to import the modules of your library into
other modules.

```
pip install -e .
```

If you are viewing the final package, use this command. It is useful for debugging.

```
pip setup.py sdist
```

To test a main module in name_of_your_service_1:
```
python python libname/name_of_your_service_1/main.py 
```

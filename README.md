# The Summit

Welcome to the Summit, a forum and micropublishing platform devoted to the discovery of actionable solutions for global challenges.

## Mission

Our mission is simply to maximize the human potential for collaborative problem-solving and accelerating the realization of a sustainable future on Earth.


## Global Challenges
Inspired by the [Global Issues](https://www.un.org/en/globalissues/) as presented by the United Nations, these are the most pressing global challenges that we are facing the 21st Century.

* Environmental Sustainability
* Energy Sustainability
* Natural Resource Management
* Water Security
* Food Security
* Peace and Conflict
* Gender Inequality
* Income Inequality
* Racial Inequality
* Global Health
* Global Development
* Human Rights
* Animal Rights
* Governance
* Poverty
* Technology
* Urbanization
* Transportation
* Communication
* Education

## Design Philosophy
The user experience is crafted based on these foundational principles:

1.  The Summit is an open commons, and therefore all user-generated is freely available for public access and participation.
2.  All user-generated content is subject to a member rating system in order to create natural self-moderating ecosystems.
3.  Everything that the user does is seamlessly interwoven on a single page.

***
## Pre-Hack Briefing | Tuesday March 18th, 2014
Time TBD.  
We'll Google Hangout about the specs and run through it for any needed modifications.

## Hackathon A | Wednesday 19th, 2014
Time 12-6pm
Great meeting. Marc, Taku, Jeet, and Niels met to discuss 'final' details for the MVP design. Outlined game-mechanics, reputation system, front-end tasks, and back-end tasks.

## Hackathon B | Saturday 22nd, 2014
When: 12pm-6pm EST
Where: Mudd Computer Science Lounge

***

# Virtual Environment Setup

Not a requirement, but we will encourage using the anaconda distribution of python. Please download it [here](https://store.continuum.io/cshop/anaconda/)

### Creating the virtual environment
Anaconda should come with the pip package manager, which you can use to install all of the required packages for developing in an app in Django-MongoDB.

To create a virtual environment in anaconda, first make a new directory called summitProject and change directory to summitProject:

`mkdir summit`
`cd summit`

create a virtual environment within summitProject/:

`$ conda create -p ./env python=2.7.6 pip ipython`

This creates a virtual environment `env` in `summit`. To activate the virtual environment:

`$ source activate ./env`

To deactivate:
`$ source deactivate`

### Installing development packages

We will be using a Django fork that supports non-relational databases, to install all django-related packages:

#### Django-nonrel
`$ pip install git+https://github.com/django-nonrel/django@nonrel-1.6-beta`

#### djangotoolbox
`$ pip install git+https://github.com/django-nonrel/djangotoolbox`

#### Django MongoDB Engine
`$ pip install git+https://github.com/django-nonrel/mongodb-engine`

### Installing MongoDB
Please follow the installation instructions for [setting up MongoDB](http://docs.mongodb.org/manual/installation/) in your system

# Setting up Git
Now that you have your environment set up, create your own fork on the original git repo. In the `summit` directory. Create a file called .gitignore with the following contents:

.Python  
env  
bin  
lib  
include  
.DS_Store  
.pyc  

Initialize a local git repo:

`$ git init`

Connect your local git repo with your forked repo of TheSummit:

`$ git remote add https://github.com/<your-username>/TheSummit`

This is your own personal fork that you will use to develop. Every time we develop in as a group, we will consolidate our code in the master repository. When developing individually, however, we will use our own fork and own branch.

Fetch the master branch from your remote:

`$ git fetch origin master`
`$ git pull origin master`

The git repo files should now be in your local repo. Now make your own branch and switch into it:

`$ git branch <my-branch>`  
`$ git checkout <my-branch>`

This is your own branch that you will use in conjunction with `<my-dev-branch>` (outlined below under **Workflow**) when developing.

### The Master Repository

Add the original repo of TheSummit as your the upstream remote:

`$ git remote add upstream https://github.com/cosmicBboy/TheSummit`

Everytime you want to push changes on your local file to the original repository (we will generally do this as a group), you will have to use the command:

`$ git push upstream master`

# Workflow

Now that you have everything set up, our workflow will be the following:

1.  Navigate to your project
2.  Activate virtual environment: `source activate ./env`
3.  `$ git checkout <my-dev-branch>`
4.  Develop!
5.  `$ git add .` and/or `$ git add -u` to stage changed/deleted files
6.  `$ git commit -m 'commit message'`
7.  `$ git checkout <my-branch>`
8.  `$ git pull origin <my-branch>`
9.  `$ git merge <my-dev-branch>`
10.  `$ git push origin <my-branch>`
11.  Deactivate virtual environment: `$ source deactivate`
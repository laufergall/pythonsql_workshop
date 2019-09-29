# This file

Steps to get python set up for our workshop.

## Install python

Please [download](https://www.python.org/downloads/) and install Python 3.

## Install anaconda

With anaconda you will easily create environments and download and install python packages. 

[Here](https://www.anaconda.com/distribution/) can download the anaconda installer for the Python 3.7 version.

After the installation, you can use a terminal called "Anaconda Prompt" and:
* create an environment: `conda create --name myenv`
* activate your (already created) environment: `conda activate myenv`
* install packages to the environment "myenv", which has been activated: (example) `conda install spyder`

For each project, a different environment can be created and packages installed into them, so that  

For more details, you can go through [this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to get started. 



## Install an IDE

At this point, you could install an IDE so that you can conveniently write and test your code.

I recommend [Spyder](https://www.spyder-ide.org/), excellent for beginners with variable explorer and IPython console, or the more advanced [PyCharm](https://www.jetbrains.com/pycharm/), with with tons of available plugins, e.g. for Docker integration.

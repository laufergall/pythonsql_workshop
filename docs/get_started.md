# This file

Steps to get python, anaconda, and an IDE set up for our workshop.

## Install Python (via Anaconda)

We want to take advantage of anaconda so that we can easily create environments and and install python packages: 

Download [here](https://www.anaconda.com/distribution/) the anaconda installer for the **Python 3.7** version and for your operating system. 

After the installation, you can use a terminal (on Windows: "Anaconda Prompt") and verify your installation with `conda --version`. 

The python console can be accessed by just typing `python`. You can execute something, e.g. `print("Hello world")`, and `quit()` to exit.


## For our workshop

It is recommended to create a different environment for each project, so that the installed packages' dependencies are kept separated.

Please go though these steps to create our workhops' environment:

1. Create an environment (named `pythonsql`): 

```bash
conda create --name pythonsql python=3.7.4
```


2. Activate your (already created) environment: 

```bash
conda activate pythonsql
```

Since no packages have been installed yet, this will throw an error:

(in the python console)
```bash
python
import pandas as pd
```

error: `ModuleNotFoundError: No module named 'pandas'`.

```bash
quit()
```


3. We now install all the project's requirements in one go, by:

```bash
pip install -r requirements.txt
```

Where the file `requirements.txt` can be found in the root folder of this repo.

Now, it should be possible to import pandas:

```bash
python
import pandas as pd
```

(no error)

```bash
quit()
```


4. At this point, you could install an IDE so that you can conveniently write and test your code.

I recommend [Spyder](https://www.spyder-ide.org/), excellent for beginners with a variable explorer and IPython console, or the more advanced [PyCharm](https://www.jetbrains.com/pycharm/), with with tons of available plugins, e.g. for Docker integration.

Example, if you decide to use the Spyder IDE:

```bash
conda install spyder
```

And then launch spyder by just:

```bash
spyder
```

5. For more details, you can go through [this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) to get started with anaconda. 

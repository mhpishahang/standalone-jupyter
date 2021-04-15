# standalone-jupyter
Prepare standalone jupyter apps for running on Windows.


## Prepare the Folder Structure
Create `app` and `app/python` folders.


## Installing Embeddable Python on Windows
1. Go to [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/) and download `Windows x86-64 embeddable zip file` for the python version you need. Here, I choose python 3.7.9.
2. Unzip the zip file directly into `app/python` folder and delete the original zip file as we do not need it anymore. Now, you must have many files in the `app/python` folder. For example, if you execute `app/python/python.exe` the embeddable python terminal runs. Congratulations! Now, we have an isolated light-weight (~14 Mb) python.
3. Open the `app/python/python37._pth` file in a text editor, and uncomment the last line to `import site`.


## Installing pip
The embeddable python by default does not contain pip. Maybe the reseaon is to keep it as light as possible. Certainly, installing packages using pip on an embeddable python is not the most optimum way. However, it looks the easiest one. Let's do it.
1. Download [get-pip.py](https://pip.pypa.io/en/stable/installing/#installing-with-get-pip-py), and put it inside the `app` folder.
2. Open a terminal, `cd` to the `app` folder, and run `.\python\python get-pip.py` to install pip in the embeddable python. I just created a simple batch file (`get-pip.bat`) containing that command in the app folder. Executing that batch file is equivalent to running the command inside the terminal. Now, the embeddable python weights almost 30 Mb.


## Installing Requirements
1. Create `app/requirements.txt` file, and put the list of python packages you need to install inside it. Make sure to put `jupyter`, `jupyterlab`, and/or `jupyter_enterprise_gateway` as some of the requirements.
2. Open a terminal, `cd` to the `app` folder, and run `.\python\python -m pip install --requirement requirements.txt` to install all the packages listed in the requirement file. I just created a simple batch file (`install-requirements.bat`) containing that command in the app folder. Executing that batch file is equivalent to running the command inside the terminal.

## Running the Jupyter App
To run any jupyter application we need to make a `.py` and a `.bat` file. Imagine we want to have an executable jupyter lab app:
1. Create `app/run-jupyter-lab.py` file.
2. Find the `app/python/Scripts/jupyter-lab.exe` executive file.
3. Do right click on the executive file and select the `Open with WinRAR` option. The WinRAR opens a `__main__.py` file.
4. Copy all the content of the `__main__.py` file into the file we created in step 1.
5. Create `app/run-jupyter-lab.bat` file.
6. Add the `.\python\python run-jupyter-lab.py` command into the batch file.
7. Add the `pause` command into the batch file. This command keeps the terminal open when you run jupyter lab.

I have done the same thing for jupyter notebook, and jupyter enterprise gateway apps to show they work as well.

## Distributing the App
One option is to right click on the `app` folder and select the `Add to archive...` option, and then activate the `create SFX archive` option. That makes a self-extracting archive.
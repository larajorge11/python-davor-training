# CONDA

These are some important commands in the execution of conda:

## Windows OS
To activate conda on Windows OS you have to set this command in a powershell terminal:

* `powershell -ExecutionPolicy ByPass -NoExit -Command "& 'C:\Users\jele2\miniconda3\shell\condabin\conda-hook.ps1' ; conda activate 'C:\Users\jele2\miniconda3' "`

If you don't want the (base) environment each time you open a terminal run this:

* `conda config --set auto_activate_base false`

## Linux
To activate conda on Linux OS you have to set this command in bash terminal:
* `source ~/miniconda3/bin/activate`
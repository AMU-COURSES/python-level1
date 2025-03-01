# Install Party: Conda, Environments, and Jupyter

## Table of Contents

## Introduction to Conda

Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies. Conda easily creates, saves, loads, and switches between environments on your local computer. It was created for Python programs, but **it can package and distribute software for any language**.

The conda software use a repository of conda packages, which are collections of files containing a package's metadata and the files needed to install the package. The conda package repositories are called channels. Several channels are available and can be added to the configuration file to install packages from them.

Conda is far from being the only package manager available, but it is one of the most popular in the scientific community for its simplicity and its completeness. It is also a good choice for beginners because it is easy to use and has a lot of documentation.

### Disclaimer

One of the most popular implementations of Conda is Anaconda, which is a distribution of Python that comes with a lot of pre-installed packages. 
However, Anaconda recent changes in its licensing policy have raised concerns about its use in national laboratories like CNRS.
It is necessary to avoid the following software channels, which provide packages covered by the license:
- pkg/main
- pkgs/r
- pkg/msys2

### Installing Conda

To install miniforge, you can follow the instructions on the [miniforge website](https://github.com/conda-forge/miniforge).

Quickly for the linux users, you can install miniforge with the following commands:
```bash
echo my_install_dir=/path/to/somewhere/you/can/write # change this line
# also take care the conda directory can be big, so choose a directory with enough space
mkdir -p $my_install_dir
cd $my_install_dir
wget "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh -p /data/users/$USER/miniforge3 -b
rm Miniforge3-$(uname)-$(uname -m).sh
```

Then you can activate the conda environment with:
```bash
eval "$($my_install_dir/miniforge3/bin/conda shell.bash hook)"
```

To activate the conda environment automatically when you open a new terminal run the following command:
```bash
conda init
```

You can check the conda default channels with:
```bash
conda config --show channels
```

In this document, we will use only a small part of conda functionalities, but you can find more information in the [conda documentation](https://docs.conda.io/projects/conda/en/latest/).

## Environment Management

### Why manage environments?

Let start from the beginning.

#### What is a Computation?

At its core, a computation is a process that transforms input into output using a program. This is the foundation of all digital processes, from simple calculations to complex scientific simulations.

At a low level, all data and programs inside a computer are represented as bits—sequences of zeros (0) and ones (1). These bits encode everything from numbers to text, images, and instructions.

It is important to understand that for the machine, everything is just bit sequences. The meaning of these bits depends on how they are interpreted.
- As **data**, bits represent raw information.
- As a **program**, bits define instructions to process data.
- As an **environment**, bits determine how the program itself is executed.

Caricature of a scientist's perspective on data, programs, and environments.
- **data** = "My research"
- **drogram** = "Code from my colleagues"
- **environment** = "Stuff I don’t care about… but should!"

But for a computation to be reproducible, all three layers must remain the same.
Ignoring the environment can lead to unexpected differences in results, making scientific claims hard to validate.

Imagine running the **same program with the same data**, but getting **different results** because the environment has changed. This happens when:
- Software versions differ.
- System configurations vary.
- External dependencies (like libraries) change.

To ensure computations remain reproducible, we must **capture the environment** alongside the data and program.

The solutions presented here is based on the **Conda** package manager, which is a popular tool for managing software dependencies in scientific computing.

This solution have some limitations, and there are other tools that we will not cover here, but that you may need at some point:
- **Containers (Apptainer, Docker)**: For isolating complete environments.
- **Functional Package Managers (Guix, Nix)**: For fully reproducible environments.

### Creating and managing Conda environments

To facilitate the management of software environments, Conda allows you to create and manage environments. An environment is a collection of software libraries and software versions that can be used to run a study. Environments are isolated from each other, so that you can install different versions of software libraries in different environments.

#### Creating an environment

To create an environment, you can use the `conda create` command. For example, to create an environment called `python_level1` last version of python, you can run the following command:

```bash
conda create -n python_level1 python
```

To activate an environment, you can use the `conda activate` command. For example, to activate the `python_level1` environment, you can run the following command:

```bash
conda activate python_level1
```

You can deactivate the environment with the command `conda deactivate`.

To list the environments that you have created, you can use the `conda env list` command. For example, to list the environments that you have created, you can run the following command:

```bash
conda env list
```

To remove an environment, you can use the `conda remove` command. For example, to remove the `python_level1` environment, you can run the following command:

```bash
conda env remove -n python_level1
```

You need to deactivate the environment before removing it.

### Installing packages

To install packages in an environment, you can use the `conda install` command.

```bash
conda install numpy
```

Useful options:
- `-n` or `--name` to specify the environment, by default the current environment is used, if no active environment, the base environment is used
- `-c` or `--channel` to specify the channel, by default the default channel is used, check the channels with `conda config --show channels`
- `-y` to automatically confirm the installation, by default you will be asked to confirm the installation

To install a package in a specific version, you can use the following syntax:

```bash
conda install numpy=2.1.3
```

You can also specity the package to install at the environment creation:

```bash
conda create -n python_level1 numpy scipy matplotlib
conda activate python_level1
```

We'll stop here for this introduction, but you can find more information below in the section [Go further with Conda](#go-further-with-conda) and in the [conda documentation](https://docs.conda.io/projects/conda/en/latest/).

## Jupyter

### What is Jupyter?

Jupyter is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text. Jupyter is a powerful tool for data analysis, data visualization, and machine learning.

Jupyter is based on the IPython project, which provides an interactive shell for Python. Jupyter extends IPython by adding support for other programming languages, such as R, Julia, and Scala.

Jupyter is widely used in the scientific community for data analysis, data visualization, and machine learning. Jupyter is also used in education for teaching programming and data science.

You can run noteboks in stand alone mode, but in this document we will use JupyterLab that is a more complete interface providing a file browser, a terminal, a text editor, a notebook editor, and other features.

### Installing JupyterLab

To install JupyterLab, you can use the `conda install` command. For example, to install JupyterLab in the `python_level1` environment, you can run the following command:

```bash
conda install jupyterlab
```

To launch JupyterLab, you can use the `jupyter lab` command. For example, to launch JupyterLab in the `python_level1` environment, you can run the following command:

```bash
jupyter lab
```

JupyterLab will open in your default web browser.

### JupyterLab Tour

#### Interface

The JupyterLab interface consists of several components:

- **File Browser**: The file browser allows you to navigate the files and directories on your computer. You can create, open, and save files and directories in the file browser.

- **Main Work Area**: The main work area is where you can view and edit files. You can open files in tabs, move tabs, and resize tabs in the main work area.

- **Notebook Editor**: The notebook editor allows you to create and edit Jupyter notebooks. A Jupyter notebook is a document that contains live code, equations, visualizations, and narrative text. You can run code cells in a Jupyter notebook and see the output of the code cells in the notebook editor.

- **Terminal**: The terminal allows you to run shell commands in a terminal window. You can use the terminal to run shell commands, navigate the file system, and run scripts.

- **Text Editor**: The text editor allows you to create and edit text files. You can create and edit text files in the text editor.

- **Output Area**: The output area displays the output of code cells in a Jupyter notebook. You can see the output of code cells in the output area.

- **Command Palette**: The command palette allows you to search for commands in JupyterLab. You can use the command palette to run commands, open files, and navigate the interface.

- **Notebook Tools**: The notebook tools allow you to perform actions on Jupyter notebooks. You can use the notebook tools to run code cells, insert new code cells, and save notebooks.

- **Kernel Status**: The kernel status displays the status of the kernel in a Jupyter notebook. You can see the status of the kernel in the kernel status.

#### Notebook

A Jupyter notebook is a document that contains live code, equations, visualizations, and narrative text. A Jupyter notebook consists of cells, which are blocks of content that can be executed independently.

There are three types of cells in a Jupyter notebook:

- **Code Cells**: Code cells contain code in a programming language, such as Python, R, Julia, or Scala. You can run code cells to execute the code and see the output of the code.

- **Markdown Cells**: Markdown cells contain text in Markdown format. Markdown is a lightweight markup language that allows you to format text using simple syntax. You can use Markdown cells to write narrative text, create headings, format text, and insert links and images.

- **Raw Cells**: Raw cells contain raw text that is not formatted. You can use raw cells to write text that should not be formatted, such as code that should not be executed.

You can run code cells in a Jupyter notebook by clicking the **Run** button in the toolbar or by pressing **Shift + Enter**. When you run a code cell, the code is executed, and the output of the code is displayed below the code cell.

You can save a Jupyter notebook by clicking the **Save** button in the toolbar or by pressing **Ctrl + S**. You can download a Jupyter notebook as a file by clicking **File > Download As** in the menu bar.

You can use the buttons in the toolbar to perform actions on Jupyter notebooks, such as creating new code cells, inserting new code cells, running code cells, and saving notebooks.

Here a cheat sheet for the JupyterLab shortcuts:

| **Shortcut** | **Action** |
|-------------|-----------|
| **Command Mode (Press `Esc` to Enter)** | |
| `A` | Insert a new cell **Above** |
| `B` | Insert a new cell **Below** |
| `M` | Convert cell to **Markdown** mode |
| `Y` | Convert cell to **Code** mode |
| `X` | **Cut** selected cell(s) |
| `C` | **Copy** selected cell(s) |
| **Edit Mode (Press `Enter` to Enter)** | |
| `Esc` | Switch to **Command Mode** |
| `Tab` | Autocomplete code suggestions |
| `Shift + Tab` | Show **Docstring/Help** for object |
| `Ctrl + /` | Toggle comment for selected line(s) |
| `Ctrl + A` | Select all text in the cell |
| `Ctrl + Z` | Undo last action |
| `Ctrl + Y` | Redo last undone action |
| **Miscellaneous** | |
| `Shift + L` | Toggle **line numbers** in the cell |
| `Shift + Space` | Scroll notebook **up** |
| `Space` | Scroll notebook **down** |
| `Ctrl + F` | Open **find and replace** |
| `Ctrl + S` | **Save** notebook |

More information about the JupyterLab shortcuts can be found in the [JupyterLab documentation](https://jupyterlab.readthedocs.io/en/stable/user/interface.html).

#### Markdown

Markdown is a lightweight markup language that allows you to format text using simple syntax. Markdown is widely used in the scientific community for writing documentation, creating websites, and formatting text.

You can use Markdown in Jupyter notebooks to write narrative text, create headings, format text, and insert links and images. Markdown cells in Jupyter notebooks allow you to write text in Markdown format and see the formatted text in the notebook editor.

Here a cheat sheet for the Markdown syntax:
# Markdown Cheat Sheet (Table Format)

| Feature        | Syntax Example |
|---------------|---------------|
| **Headings**  | `# H1` <br> `## H2` <br> `### H3` <br> `#### H4` <br> `##### H5` <br> `###### H6` |
| **Bold**      | `**Bold**` or `__Bold__` → **Bold** |
| **Italic**    | `*Italic*` or `_Italic_` → *Italic* |
| **Strikethrough** | `~~Strikethrough~~` → ~~Strikethrough~~ |
| **Unordered List** | `- Item 1` <br> `- Item 2` <br> `  - Sub-item` |
| **Ordered List** | `1. First item` <br> `2. Second item` <br> `3. Third item` |
| **Link** | `[Title](https://example.com)` → [Title](https://example.com) |
| **Image** | `![Alt text](https://example.com/image.jpg)` |
| **Inline Code** | `` `print("Hello, World!")` `` → `print("Hello, World!")` |
| **Code Block** | ```python <br> def hello(): <br> &nbsp;&nbsp;&nbsp;&nbsp;print("Hello, World!") <br> ``` |
| **Blockquote** | `> This is a blockquote.` → <br> > This is a blockquote. |
| **Table** | `\| Header 1 \| Header 2 \|` <br> `\| --- \| --- \|` <br> `\| Row 1, Col 1 \| Row 1, Col 2 \|` <br> `\| Row 2, Col 1 \| Row 2, Col 2 \|` |
| **Horizontal Rule** | `---` or `***` |
| **Checkboxes (Task List)** | `- [x] Task 1` <br> `- [ ] Task 2` <br> `- [ ] Task 3` |
| **Escaping Characters** | `Use \* to display an asterisk (*)` |

More information about the Markdown syntax can be found in the [Markdown Guide](https://www.markdownguide.org/).

## Go further with Conda

### Sharing and reproducing environments using environment files

#### Basics

To share and reproduce environments, Conda allows you to export an environment to a file. An environment file is a text file that contains the software libraries and software versions that are installed in an environment. You can create an environment file by running the `conda env export` command. For example, to create an environment file called `environment.yml` for the `pandas` environment, you can run the following command:

```bash
conda env export -n python_level1 > python_level1.yml
```

To create an environment from an environment file, you can use the `conda env create` command. For example, to create an environment called `myenv` from the `environment.yml` file, you can run the following command:

```bash
conda env create -f python_level1.yml -n myenv
conda activate myenv
conda list
```

#### Environment file

The environment file is a text file that contains the software libraries and software versions that are installed in an environment. The environment file is in YAML format, which is a human-readable data serialization format. The environment file contains the following information:

- The name of the environment
- The channels that are used to install the software libraries
- The software libraries and software versions that are installed in the environment

Check the content of the environment file you just created:

```bash
cat python_level1.yml
```

First thing to notice is that the environment file contains much more packages than the ones you installed. This is because the environment file contains the dependencies of the packages you installed. The dependencies are the software libraries that are required to run the packages you installed. The dependencies are installed automatically when you install a package, so you do not need to install them manually.

By default in the recent version (could change other time, check the documentation), the environment file contains the software libraries and software versions and the binary tags of the packages. The binary tags describe the build specification from dependencies. The binary tags increase the reproducibility of the environment because they specify the exact build specification of the packages.

If your goal is to share the environment file with others, you can remove the binary tags from the environment file. To remove the binary tags from the environment file, you can run the following command:

```bash
conda env export -n python_level1 --no-builds > python_level1_no_builds.yml
```

Check the content of the environment file you just created:

```bash
diff -y python_level1.yml python_level1.yml
```

This environment file is more readable and easier to share with others and is platform-independent.

You can also use the `--from-history` option to create an environment file that contains only the software libraries and software versions that you explicitly installed:

```bash
conda env export -n python_level1 --from-history > python_level1_from_history.yml
cat python_level1_from_history.yml
```

Here the environment reproducibility is limited. It is still very usefull to control your dependencies.

#### Hybrid environments (Conda and pip)

In genenal pip comes with python, and them should be already installed in the conda environment. If not, you can install it with:

```bash
conda install pip
```

You can install pip package in the active environment with:

```bash
pip install seaborn scikit-learn
```

Now if you export the environment, you will see the pip packages in the environment file.

```bash
conda env export -n python_level1 > python_level1_pip.yml
cat python_level1_pip.yml
```

#### Customized environments

There is many ways to customize the environments in conda, you can install packages from different channels, you can install packages from different sources, you can install packages from a local directory... But take care, the more you customize the environment, the more you will have to manage it and the more you will have to document it to share it and ensure a raisonnable reproducibility.

Here a simple but useful example to create a build environment.

```bash
conda create -n build_env cmake=3.26 gcc=8.5.0 gxx cfitsio hdf5
conda activate build_env
```

In the case of a build environment, you will need to set some environment variables to use it to build. 
```sh
export CC=$(which gcc)
export CXX=$(which g++)
expoft LD_LIBRARY_PATH=$CONDA_PREFIX/lib
```

To avoid to set these variables each time you activate the environment, you add these in the `activate.d` directory of the environment.

```bash
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo "export CC=$(which gcc)" > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo "export CXX=$(which g++)" >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
echo "export LD_LIBRARY_PATH=$CONDA_PREFIX/lib" >> $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
```

To deactivate the environment, you can remove the environment variables with the `deactivate.d` directory.

```bash
mkdir -p $CONDA_PREFIX/etc/conda/deactivate.d
echo "unset CC" > $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
echo "unset CXX" >> $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
echo "unset LD_LIBRARY_PATH" >> $CONDA_PREFIX/etc/conda/deactivate.d/env_vars.sh
```

Check :
  
```bash
conda deactivate
echo $LD_LIBRARY_PATH
conda activate build_env
echo $LD_LIBRARY_PATH
```


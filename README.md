<div id="top"></div>

<div align="center">
    <h1 style="font-weight:bold;">Pykage</h1>
    <p align="center">Command-Line Tool to simplify the creation of python's packages in non-IDE environments.</p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#how-did-this-project-born">How Did This Project Born?</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Installation</a>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<br/>

## How Did This Project Born

Is a simple story, I was really annoyed of the manual creation of packages in VSCode, and the lack of a plugin for that. Is a simple but neccesary feature that most _Python Devs_ might need from time to time and that takes a little amount of time, but time enough to focus in some other task that you might be doing.

So since I kinda like the CLIs I decided to made this tool.

<p align="right">[<a href="#top">back to top</a>]</p>

### Built With

* [Python](https://www.python.org/)
* [Setuptools](https://github.com/pypa/setuptools)
* [Click](https://github.com/pallets/click)
* [Colorama](https://github.com/tartley/colorama)

<p align="right">[<a href="#top">back to top</a>]</p>

## Installation

```sh
pip install pykage
```

After doing that, the next step is use the CLI. Check [the next section](#usage) for more information.

<p align="right">[<a href="#top">back to top</a>]</p>

## Usage

For a basic usage of the interface you have to prvide a ***name*** for your package and then pykage will create it in your current directory, so make sure you are in the right directory. 

Example:

```sh
pykage [name_of_your_Package]
```

Otherwise if you provide the _--dir_ or _-d_, as the option, followed by the name of the directory where pykage should create the package.

Example:

```sh
pykage --dir [path_of_your_directory] [name_of_your_Package]
```

or

```sh
pykage -d [path_of_your_directory] [name_of_your_Package]
```

<p align="right">[<a href="#top">back to top</a>]</p>

## License

The tool is distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">[<a href="#top">back to top</a>]</p>

## Contact

If you want to contribute or add a feature you might think will improve the development of the project, send me a email, I don't bite!

Personal Email: [josevizcaya0616@gmail.com](josevizcaya0616@gmail.com)
<!-- Improved compatibility of back to top link: See: https://github.com/jfinley6/rockies-double-checker/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/jfinley6/rockies-double-checker">
    <img src="https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Rockies Double Checker</h3>

  <p align="center">
    Every game where the Rockies hit a double, fans will get a chance to get a <del>free</del> double cheeseburger
    at McDonald's for 1$ the day after the game. This site will give you accurate info about the previous game as well as details
    about the promotion.
    <br />
    UPDATE: Mcdonald's has changed the fine print of the promotion to include a 1$ minimum purchase. I've decided to halt planned updates and leave the site as is.
    <br />
    <br />
    <a href="https://rockies-double-checker.onrender.com/">View Demo</a>
    ·
    <a href="https://github.com/jfinley6/rockies-double-checker/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/jfinley6/rockies-double-checker/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With Python and Flask and deployed on Render</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<img src="https://i.imgur.com/jG0SaBO.png" alt="Logo">

This was an idea I had for something to build after learning about the Mcdonald's promotion from a friend. I decided to use Python since I knew that it had strong web scraping
capabilites as well as Flask since I'm always interested in trying new frameworks. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]
* [![JavaScript][JavaScript]][JavaScript-url]
* [![Flask][Flask]][Flask-url]
* [![Render][Render]][Render-url]
* [![Gunicorn][Gunicorn]][Gunicorn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

* pip
  ```sh
  python -m pip install --upgrade pip
  ```

* virtualenv
  ```sh
  python -m pip install --user virtualenv
  ```

### Installation


1. Create the environment (creates a folder in your current directory)
```sh
virtualenv env_name
```
In Linux or Mac, activate the new python environment
```sh
source env_name/bin/activate
```
Or in Windows
```sh
.\env_name\Scripts\activate
```
2. Clone the repo
   ```sh
   git clone https://github.com/jfinley6/rockies-double-checker.git
   ```
3. Install packages
   ```sh
   pip install -r requirements.txt 
   ```
4. Run the Program
   ```sh
   Gunicorn app:app   
   ```
5. Open http://127.0.0.1:8000 in browser

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

John Finley - j.finley92@gmail.com

Project Link: [https://github.com/jfinley6/rockies-double-checker](https://github.com/jfinley6/rockies-double-checker)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/jfinley6/rockies-double-checker.svg?style=for-the-badge
[contributors-url]: https://github.com/jfinley6/rockies-double-checker/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/jfinley6/rockies-double-checker.svg?style=for-the-badge
[forks-url]: https://github.com/jfinley6/rockies-double-checker/network/members
[stars-shield]: https://img.shields.io/github/stars/jfinley6/rockies-double-checker.svg?style=for-the-badge
[stars-url]: https://github.com/jfinley6/rockies-double-checker/stargazers
[issues-shield]: https://img.shields.io/github/issues/jfinley6/rockies-double-checker.svg?style=for-the-badge
[issues-url]: https://github.com/jfinley6/rockies-double-checker/issues
[license-shield]: https://img.shields.io/github/license/jfinley6/rockies-double-checker.svg?style=for-the-badge
[license-url]: https://github.com/jfinley6/rockies-double-checker/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/john-tyler-finley
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
[JavaScript]: https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E
[JavaScript-url]: https://www.javascript.com/
[Flask]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/
[Render]: https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white
[Render-url]: https://render.com/
[Gunicorn]: https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white
[Gunicorn-url]: https://gunicorn.org/

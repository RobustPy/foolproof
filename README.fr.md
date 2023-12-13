<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]<!--[![Forks][forks-shield]][forks-url]-->
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]<!--[![MIT License][license-shield]][license-url]--><!--[![LinkedIn][linkedin-shield]][linkedin-url]-->
[![PyPi version][pypi-shield]][pypi-url]<!--[![Python 2][python2-shield]][python-url]-->
[![Python 3][python3-shield]][python-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <img src="https://raw.githubusercontent.com/NicolasMICAUX/foolproof/main/images/logo.png" alt="Logo" width="160" height="160">
  <h1 align="center">FoolProof</h1>
  <p align="center">
Trouvez toutes les exceptions que votre code et ses dépendances peuvent générer, afin de rendre votre code infaillible !<br/>
<!--
    <a href="https://github.com/NicolasMICAUX/foolproof"><strong>Explorer la documentation »</strong></a>
-->
    <br/><br/>
    <!--
    <a href="https://github.com/NicolasMICAUX/foolproof">Voir la démo</a>
    ·
    -->
    <a href="https://github.com/NicolasMICAUX/foolproof/issues">Report Bug</a>
  </p>
</div>


<!-- ABOUT THE PROJECT -->
## Introduction
<!-- [Screen Shot][product-screenshot] -->
Connaissez-vous "l'effet démo" ? Le fait que votre code dûment testé échoue soudainement dès que vous le montrez à quelqu'un ? Souvent, c'est parce que vous avez oublié de gérer une exception à laquelle vous n'aviez pas pensé.

🪨 FoolProof identifie automatiquement les exceptions que votre code et ses dépendances peuvent déclencher, afin que vous ne soyez plus jamais pris au dépourvu !

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>

<!-- GETTING STARTED -->
## Pour commencer
foolproof est très simple à utiliser.

Installer foolproof avec pip :
```sh
pip install foolproof
```

Pour analyser un module entier `mypackage`, avec toutes les fonctions et méthodes qu'il contient, ajoutez ces lignes au début de votre code :
``python
import mypackage
import foolproof

foolproof(mypackage)
```

Vous pouvez également l'utiliser directement sur une fonction :
```python
import foolproof
from mypackage import main

foolproof(main)
```

<p align="right">(<a href="#readme-top">retour en haut</a>)</p>


<!-- CONTRIBUTING -->
## Contributing
Ideally, I would like to add more features to foolproof, but I don't have much time for it. If you want to contribute, you're more than welcome to do so!

### Roadmap/todo
| Task | Importance | Difficulty | Contributor on it | Description  |
|:-----|------------|------------|-------------------|:-------------|
| Adding links to file | 5/5 | 5/5 | - | More than printing the raise command, we should print the link to the file in which the `raise` is used. This implies a major rework of foolproof, as the python `ast` does not keep the link between ast nodes and files. |

<!--
Non-Code contribution :

| Task | Importance | Difficulty | Contributor on it | Description  |
|:-----|------------|------------|-------------------|:-------------|
|      | ./5        | ./5        | NOBODY            | _e.g._ : ... |
-->

<!--
_For every todo, just click on the link to find the discussion where I describe how I would do it._  
See the [open issues](https://github.com/NicolasMICAUX/foolproof/issues) for a full list of proposed features (and known issues).
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>


### How to contribute
Contributing is an awesome way to learn, inspire, and help others. Any contributions you make are **greatly appreciated**, even if it's just about styling and best practices.

If you have a suggestion that would make this project better, please fork the repo and create a pull request.  
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourAmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Auteur
Cette librairie a été crée par [Nicolas MICAUX](https://github.com/NicolasMICAUX).

## Remerciements
Une grande partie de ce code provient de https://github.com/DontShaveTheYak/deep-ast (https://pypi.org/project/deep-ast/)  
Licence : GNU General Public License v3 (GPLv3)  
Tous les crédits vont à Levi Blaney - @shady_cuz, shadycuz@gmail.com

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/NicolasMICAUX/foolproof.svg?style=for-the-badge
[contributors-url]: https://github.com/NicolasMICAUX/foolproof/graphs/contributors
[stars-shield]: https://img.shields.io/github/stars/NicolasMICAUX/foolproof.svg?style=for-the-badge
[stars-url]: https://github.com/NicolasMICAUX/foolproof/stargazers
[issues-shield]: https://img.shields.io/github/issues/NicolasMICAUX/foolproof.svg?style=for-the-badge
[issues-url]: https://github.com/NicolasMICAUX/foolproof/issues
[pypi-shield]: https://img.shields.io/pypi/v/foolproof.svg?style=for-the-badge
[pypi-url]: https://pypi.org/project/foolproof/
[python2-shield]: https://img.shields.io/badge/python-2.7+-blue.svg?style=for-the-badge
[python3-shield]: https://img.shields.io/badge/python-3.5+-blue.svg?style=for-the-badge
[python-url]: https://www.python.org/downloads/

[//]: # ([license-shield]: https://img.shields.io/github/license/NicolasMICAUX/foolproof.svg?style=for-the-badge)
[//]: # ([license-url]: https://github.com/NicolasMICAUX/foolproof/blob/master/LICENSE.txt)
[//]: # ([product-screenshot]: images/screenshot.png)


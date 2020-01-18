
![logo](https://github.com/bradlindblad/schrutepy/blob/master/static/logo.png?raw=true)

--------------
# The Entire Transcript from the Office in Tidy Format


<p align='center'><a href="https://badge.fury.io/py/schrutepy"><img src="https://badge.fury.io/py/schrutepy.svg" alt="PyPI version" height="18"></a> <a href="https://travis-ci.org/bradlindblad/schrutepy.svg?branch=master" alt="Travis Build Status"><img src="https://travis-ci.org/bradlindblad/schrutepy.svg?branch=master" /></a> <a href='https://coveralls.io/github/bradlindblad/schrutepy?branch=master'><img src='https://coveralls.io/repos/github/bradlindblad/schrutepy/badge.svg?branch=master' alt='Coverage Status' /></a> <a href='https://pyup.io/repos/github/bradlindblad/schrutepy'><img src='https://pyup.io/repos/github/bradlindblad/schrutepy/shield.svg' alt='PyUp' /></a> <a href='https://github.com/psf/black'><img src='https://camo.githubusercontent.com/28a51fe3a2c05048d8ca8ecd039d6b1619037326/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667' alt='Black' /></a> <a href='https://img.shields.io/github/stars/bradlindblad/schrutepy?style=social&label=Star&maxAge=2592000'><img src='https://img.shields.io/github/stars/bradlindblad/schrutepy?style=social&label=Star&maxAge=2592000' alt='Black' /></a> 
</p>

### Also available in R: [schrute package](https://bradlindblad.github.io/schrute/)
<a href="https://bradlindblad.github.io/schrute/"><img src="https://raw.githubusercontent.com/bradlindblad/schrute/master/man/figures/logo.png" alt="schrute R package"  height= "200"></a>



# What is it
The entire text transcripts from the American version of The Office TV show in pandas dataframe. Use this package to practice or learn NLP, text analysis or deep learning.

# Getting started
You can install easily from PyPi


## Install
```
pip install schrutepy
```
## Usage
Pull the transcripts into a data frame with this library's only method:

```
from schrutepy import schrutepy

df = schrutepy.load_schrute()

df.head(5)
```

## Demo
View the full demo on the [website: technistema](https://technistema.com/posts/python-text-analysis-with-the-schrutepy-package/)

# Contributors
- [Lucas Greybuck](https://github.com/hypercompetent)

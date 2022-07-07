# Reuters
Reuters information retrieve
[![PyPI](https://img.shields.io/pypi/v/Reuters)](https://pypi.org/project/Reuters/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/Reuters)](https://pypistats.org/packages/reuters)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Reuters)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/Reuters)
![GitHub contributors](https://img.shields.io/github/contributors/Iceloof/Reuters)
![GitHub issues](https://img.shields.io/github/issues-raw/Iceloof/Reuters)
![GitHub Action](https://github.com/Iceloof/Reuters/workflows/GitHub%20Action/badge.svg)
![GitHub](https://img.shields.io/github/license/Iceloof/Reuters)

## Install
```
pip install Reuters
```

## Usage
- Initializing
```
from Reuters import Reuters
reuters=Reuters('AAPL.O')
```
- Get current price
```
reuters.getPrice()
```
- Get name
```
reuters.getName()
```
- Get market capital
```
reuters.getMarketCap()
```
- Get PE
```
reuters.getPE()
```
- Get recommendation
```
reuters.getRecommendation()
```
- Get return of investment
```
reuters.getROI()
```
- Get return of equity
```
reuters.getROE()
```
- Get company industry
```
reuters.getIndustry()
```

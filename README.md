# Spartan
Spartan is a python application that generates nutritionally-complete diets given a selection of foods.
* Enter price data to generate diets which minimize total cost
* Provides a nutrient composition database for over 7000 foods that can be easily inspected and compared.
* Personal nutritional requirements based on US Food and Nutrition Board [recommendations](https://ods.od.nih.gov/Health_Information/Dietary_Reference_Intakes.aspx)
* Select dietary preferences to exclude food groups
* Customize food constraints to limit quantity of specific foods in generated diets

# Run
A prebuilt Windows executable called `spartan.exe` can be downloaded [here]().
It can also be found under `dist` in this repository.
This has only been tested on Windows 10 but may work on earlier releases.

## From source
On Windows
```shell
git clone https://github.com/josh-minch/frugal-nutrition.git
virtualenv --no-site-packages VIRTUAL
VIRTUAL\Scripts\activate
pip -r requirements.txt
```
On macOS / Linux
```shell
git clone https://github.com/josh-minch/frugal-nutrition.git
virtualenv --no-site-packages VIRTUAL
source VIRTUAL/bin/activate
pip -r requirements.txt

```
Then the application with `python main.py`

# Built with
* [Python 3.6](https://www.python.org/downloads/)
* [Qt for Python's PySide2](https://www.qt.io/qt-for-python/) - GUI toolkit
* [PuLP](http://coin-or.github.io/pulp/) - Linear programming backend
* [Numpy](https://numpy.org/)
* [USDA's FoodData Central SR Legacy](https://fdc.nal.usda.gov/) - Food composition nutrient data
* [QtComboBoxTableWidget](https://github.com/pierrebai/QtComboBoxTableWidget) - Very helpful reference for specific Qt functionality
* [PyInstaller](https://www.pyinstaller.org/) - For the Windows executable
* [Feather Icons](https://feathericons.com/)

# License
This software is licensed under

This project includes open source software licensed under MIT license and BSD license. In compliance with these licenses, all copies and substantial portions of the licensed software retains the original copyright and license notices.
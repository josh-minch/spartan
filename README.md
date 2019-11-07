# Spartan
Spartan is a Python application that generates nutritionally complete diets given a selection of foods.
* Generate diets optimized by nutritional density, minimizing total weight.
* Enter price data to generate diets which minimize total cost.
* Provides a nutrient composition database with over 7000 foods that can be easily inspected and compared.
* Personal nutritional requirements based on US Food and Nutrition Board [recommendations](https://ods.od.nih.gov/Health_Information/Dietary_Reference_Intakes.aspx).
* Choose dietary preferences to exclude certain food groups.
* Customize food constraints to limit quantity of specific foods in generated diets.
* Examine nutritional breakdown of generated diet on a food by food basis.

# Run
A prebuilt Windows executable can be found under releases. Tested on Windows 10, but may work on earlier versions.

## From source
### Prerequisites
* Python 3.6
* venv

### Clone and install dependencies
On Windows
```shell
git clone https://github.com/josh-minch/spartan.git
cd spartan/spartan
virtualenv --no-site-packages VIRTUAL
VIRTUAL/Scripts/activate
pip install -r requirements.txt
```
On macOS / Linux
```shell
git clone https://github.com/josh-minch/spartan.git
cd spartan/spartan
virtualenv --no-site-packages VIRTUAL
source VIRTUAL/bin/activate
pip install -r requirements.txt

```
Then run with
```
python main.py
```

# Built with
* [Python 3.6](https://www.python.org/downloads/)
* [Qt for Python's PySide2](https://www.qt.io/qt-for-python/) - GUI toolkit
* [PuLP](http://coin-or.github.io/pulp/) - Linear programming modeller
* [CBC](https://github.com/coin-or/Cbc) -  Linear programming solver
* [Numpy](https://numpy.org/)
* [USDA's FoodData Central SR Legacy](https://fdc.nal.usda.gov/) - Food nutrient composition data
* [QtComboBoxTableWidget](https://github.com/pierrebai/QtComboBoxTableWidget) - Very helpful reference for specific Qt functionality
* [PyInstaller](https://www.pyinstaller.org/) - For the Windows executable
* [Feather Icons](https://feathericons.com/)
* Logo provided by a [lovely artist](https://janejorda.carbonmade.com/).

# Legal
This software does not currently have a license.

This project includes open source software licensed under the MIT License and the BSD License. In compliance with these licenses, all copies and substantial portions of the licensed software retains the original copyright and license notices.
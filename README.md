
# Kororo Estate

This only a test module based on official documentation in Odoo version 17.0


## Installation

Please follow this step to activate your environment and install all dependencies required.

```bash
  python3 -m pip install --upgrade pip
```
```bash
  python3 -m pip install -r requirements.txt
```

## Notice
If you have installed previous `kororo_estate` please remove or
uninstall all `kororo_estate` module before going to next execution. I have made some changes in ORM and will cause an issue. If you find a problem with installation, kindly report me. This `estate_account` module will installed automaticaly soon after `kororo_estate` module installed.

## Run Locally

Clone the project

```bash
  git@github.com:rizalkororo/kororo_estate.git
```

Clone this module
```bash
  git@github.com:rizalkororo/estate_account.git
```
Go to the project directory

```bash
  mv kororo_estate estate
```

Copy module to project addons

```bash
  cp estate <Odoo_enterprise_project_folder>/odoo/addons
```
```bash
  cp estate_account <Odoo_enterprise_project_folder>/odoo/addons
```

## Usage

Execute this only at the first start to install module estate.

Inside Odoo root project run:
```python
python odoo-bin -c settings.conf -i estate
```
Execute this line for further action
```python
python odoo-bin -c settings.conf
```
Next login to web page with current credential:
```
username: admin
password: admin
```
Change to developer mode by going to `settings -> Developer Tools -> Activate the developer mode`

![App Screenshot](https://i.ibb.co/6WnjYz9/Screenshot-2024-01-01-184455.png)

Back to `Apps` menu, and type `kororo estate` and do installation.
## Tech Stack

**Client:** Odoo, XML, Sass

**Server:** Python, Postgres


## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)




![Logo](https://media.licdn.com/dms/image/C560BAQHQT2VfIyJNyw/company-logo_200_200/0/1630643115276/kororo_logo?e=2147483647&v=beta&t=8zCw-jiGACWxl4MPZyw-qXoUqGIftJJlsK5jFN5oZsg)


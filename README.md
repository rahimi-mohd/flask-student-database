### Flask Student Database (wip)

#### Installation

Git clone this repo.  
Recommended using python virtual environment such for package and dependencies management.

Linux:  

```
python3 -m venv venv
source venv/bin/activate
```

Windows:  

```
python.exe -m venv venv
.\venv\Scripts\activate.ps1
```

Install all packages and dependencies

```
pip install -r requirements.txt
```

Activate db and migrations

```
flask db init
flask db migrate 
flask db upgrade
```

Run `python main.py` and enjoy!

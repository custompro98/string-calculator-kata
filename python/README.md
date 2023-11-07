String Calculator Kata
============
Setup: 
```
PIP_REQUIRE_VIRTUALENV="0" python -m pip install --upgrade virtualenv setuptools
virtualenv venv

# bash/zsh
source venv/bin/activate 

# fish
source venv/bin/activate.fish

pip install --upgrade -r requirements.txt
```

Run: 
`ptw`  
  
Your tests are in `tests/test_add.py` and your function is defined in `string_calculator/add.py`

Clean up:
```
git checkout -- .
deactivate
```
 
Upgrade:
```
virtualenv venv

# bash/zsh
source venv/bin/activate 

# fish
source venv/bin/activate.fish

pip install --upgrade <package>
pip freeze > requirements.txt
```

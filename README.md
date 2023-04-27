# colorpicker
Only tested on Ubuntu 22.04.02

# Prerequisite
**1 Install Scrot** *(Is needed to capture a 1px screenshot)*  
```sudo apt-get install scrot```

**2 Setup venv**  
```python -m venv venv```

**3 Activate venv**  
```source venv/bin/activate```

**4 Install requirements.txt**  
```pip install -r requirements.txt```  

# Run
```python colorpicker.py```

# Add as alias .zshrc/.bashrc  
```alias colorpicker="<path/to/venv/bin/python> <path/to/colorpicker.py>"```
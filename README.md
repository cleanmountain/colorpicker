# colorpicker
Only tested on Ubuntu 22.04.02.

Run colorpicker from the terminal and click anywhere on your screen. 
Get the rgb and hex color of whatever pixel you clicked printed in the terminal.


![image](https://user-images.githubusercontent.com/120788835/234975069-d8b4f7a1-39c1-47fb-b3c6-e756e1c96677.png)


# Prerequisite
**1 Install Scrot** *(Is needed to capture a 1px screenshot)*  
```
sudo apt-get install scrot
```

**2 Setup venv**  
```
python -m venv venv
```

**3 Activate venv**  
```
source venv/bin/activate
```

**4 Install requirements.txt**  
```
pip install -r requirements.txt
```  

# Run
```
python colorpicker.py
```

# Add as alias .zshrc/.bashrc  
```
alias colorpicker="<path/to/venv/bin/python> <path/to/colorpicker.py>"
```

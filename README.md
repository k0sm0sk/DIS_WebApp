# Databases and Information Systems (DIS) - Project

### Authors
* Victor V. Jørgensen - kft410
* Daniel Friis-Hasché - rcb933
* Lars V. Thorup - rlp419
* Vitus N. Legarth - gfn320


## About the game
The game we have made is a Higher or Lower type game, where the player has to choose between two videogames, and guess which one has the highest amount of sold copies.
All videogames showcased in our game, has at least 500.000 sold copies worldwide.

**Note**: *After exloring the dataset, we have noticed that not all entries have correct data regarding total sales and even sometimes cover image. This is a problem with the dataset from Kaggle, and not the cleaning process. E.g. Minecraft should be number 1, but has about 100 million copies less sold in the dataset, than in "real life".*

## Setup / Dependency installation
All dependencies will work on `Python version 3.12.7 and above`. We have **not** tested earlier versions.

In you terminal, navigate to the root folder of the `DIS_WebApp` and install dependencies by running:
```zsh
pip install -r requirements.txt
```


## How to run
Run `app.py` located at `src/app.py` using:
#### MacOS
```zsh
python3 app.py
```
#### Windows
```zsh
python app.py
```
And go to the **local URL** 
```http://127.0.0.1:5000```

*Note that the default url route for localhosts are 127.0.0.1 with a port usually defined as `:5000`. If you cannot access the file via this path, look at the output in the conosole of the terminal you are running the file from, and go to that URL.*


If the run command doesn't work, you can alternatively (from the same filepath) run:
```zsh
flask run --debug
```



### ER Model of our DBMS
![alt text](ER_Model.png)

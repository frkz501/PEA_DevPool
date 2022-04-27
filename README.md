# Sorting hat
## Getting Started
```haskell
git clone https://github.com/frkz501/PEA_DevPool.git
# install requirements
pip install -r requirements.txt
```
## Requirements
1. Python 3.10 (3+ shoul work just fine)
2. Flask 2.1.1 to host app
3. Pandas 1.4.2 to manipulate date as dataframe
Number 2. and 3. should be installed already with
```haskell
pip install -r requirements.txt
```
## Running the program
1. Go to your terminal and
```haskell
python .\main.py
```
2. Prompts like
```haskell
* Serving Flask app 'main' (lazy loading)
 * Environment: production
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080 (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: ***-***-***
```
should be shown
3. Go to your web browser and open 'http://127.0.0.1:8080'
4. Go back to your Terminal and enter the name(s) **names MUST be separated by commas `,`
5. The results of each students will show on the terminal, like:
```haskell
Sorry, Sl, house Hufflepuff is full.
We're assigning Sl to Gryffindor.
Congrats!
Sl is in Gryffindor!
Sorry, Sll, house Hufflepuff is full.
But you're the last one so we will squeeze you in Hufflepuff.
Congrats!
Sll is in Hufflepuff!
```
6. A summary table and a table containing all students should be shown on the web browser in 3.
7. A `.csv` file should be saved in your cwd, containing past students. WHICH will be loaded again in next runtime(s).
## Algorithm
1. Sorting - counted vowel (AEIOU) or thai vowels mod by 4
2. If a house is full - divert to next house in the list : Hufflepuff > Gryffindor > Slytherin > Ravenclaw > Hufflepuff > ...
## Remarks
I'm a beginner here. I have no idea about frontend coding.
I tried (and maybe forced) to include flask in this project. (Also tried to use Google Cloud projects/heroku)
I hope I could better myself at utilizing these tools.
Thanks for having me!
# AromaAtlas Project

## How 'search.py' works

The `search.py` file is responsible for finding perfumes based on the notes entered by the user.

Here is the process in simple steps:

1. **Load the data**

   * The program reads a CSV file (`fra_cleaned.csv`) using pandas.
   * This file contains perfume names and their Top, Middle, and Base notes.

2. **Filter perfumes**

   * It checks each perfume to see if any of the user’s notes appear in its Top, Middle, or Base notes.
   * If at least one note matches, the perfume is included in the results.

3. **Merge additional data**

   * The filtered results are merged with another dataset (`fra_perfumes.csv`) to include more information such as descriptions.
   
## Merging with 'hashmap.py'

4. **Count matches**

   * For each perfume, the program counts how many of the user’s notes are present.
   * For example, if the user enters "rose" and "vanilla" and a perfume contains both, the match count is 2.

5. **Store in HashMap**

   * Each perfume is inserted into a custom HashMap.
   * The key is the perfume name, and the value is the perfume’s data.

6. **Sort results**

   * Results are sorted by:

     * First: number of matches (higher values first)
     * Second: alphabetical order (used when match counts are equal)

---

## Time Complexity


### Search and filtering

* The program checks all perfumes → O(n)

### HashMap

* Each perfume is checked for matching notes → O(n)
* Average case → O(1) per insert
* Total → O(n)

---

## How to run the website

### 1. Run the backend

```bash
python3 app.py
```

You should see:

```
Running on http://127.0.0.1:5000
```

---

### 3. Open the website

Open your browser and go to:

```
http://127.0.0.1:5000
```

Do not open the HTML file directly. 

---


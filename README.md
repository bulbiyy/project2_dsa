# AromaAtlas Project

## How to open the website

### 1. Make sure you have the requirements
* Python 3.10 or higher
* Python libarary:
```bash
pip install flask pandas
```

### 2. Run the backend in terminal

Navigate to archive folder:
```bash
cd archive
```

Start the backend:
```bash
python3 app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```
Make sure to keep this terminal window open to run the server.

---

### 3. Open the website

Open your browser and go to:

```
http://127.0.0.1:5000
```

Do not open the HTML file directly. The features require Flask to be running.

---

## How to use the site
1. Type 1-3 scent notes into the search fields
2. Optionally choose a priority note to ensure its presence in scent suggestions
3. Search the Atlas
4. Results appear in up to three tiers:
   * Tier 1 - Perfect Match: persfumes containing all requested notes
   * Tier 2 - Close Match: perfumes with priority notes + at least one other (only shown when 3 notes are entered)
   * Tier 3 - Priority Match - [erfumes with only your priority note
5. The performance card shows how long each data structure took in milliseconds
6. You can toggle between the Hash Map and Trie to compare results

  
---

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

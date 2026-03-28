# AromaAtlas Project

## What is AromaAtlas?
In the perfume industry, which includes thousands of brands and fragrance collections, customers often lack familiarity with the wide range of options available on the market. At the same time, most people have specific scent preferences that they would like to wear for everyday use or special occasions. AromaAtlas addresses this challenge by helping individuals discover fragrances that match their preferred scent notes, making it easier to find a perfume that truly fits their personal taste.

## Acquiring AromaAtlas

### Downloading the project
1. On GitHub, Find the <> Code dropdown menu
2. Select the Download Zip option
3. In your downloads, extract the folder

## How to open the website (using Terminal)

### 1. Make sure you have the requirements
* Python 3.10 or higher:
```bash
python --version
```

* Python libarary:
```bash
pip install flask pandas
```

### 2. Run the backend

Navigate to archive folder:
```bash
cd archive
```
<sup> *Note that you will need to cd into the project folder in order to cd into archive* </sup>

Start the backend:
```bash
python3 app.py
```

You should see:
```
Running on http://127.0.0.1:5000
```
<sup> *Make sure to keep this terminal window open to run the server.* </sup>

---

### 3. Open the website

Open your browser and go to:

```
http://127.0.0.1:5000
```

<sup> *Do not open the HTML file directly. The features require Flask to be running.* </sup>

---

## How to use the site
1. Type 2-3 scent notes into the search fields
2. Optionally choose a priority note to ensure its presence in scent suggestions
3. Search the Atlas
4. Results appear in up to three tiers:
   * Tier 1 - Perfect Match: perfumes containing all requested notes
   * Tier 2 - Close Match: perfumes with priority notes + at least one other (only shown when 3 notes are entered)
   * Tier 3 - Priority Match - perfumes with only your priority note
5. The performance card shows how long each data structure took in milliseconds
6. You can toggle between the Hash Map and Trie to compare results

# Practical Code Library (AI, Business Analytics, CIS, STQA)

80 files: runnable code, datasets and step files for four subjects.

## Folder structure

    frontend/index.html     the website (single file, works fully offline)
    backend/server.js       small Node.js server (no npm packages needed)
    code_files/             every code file, grouped by subject
      manifest.json         list of all files with title, aim and requirements
      artificial-intelligence/   22 files (18 Python programs + 4 CSV datasets)
      business-analytics/        20 Python programs
      cyber-information-security/ 15 files (Python, Java, router command files, steps)
      stqa/                      23 files (Java, HTML, JSP, log4j, JMeter .jmx, steps)
    Dockerfile, package.json    for deployment

## Run on your computer

Frontend only (no install): double-click frontend/index.html

With the backend (Node.js 16 or newer):

    npm start

Open http://localhost:3000

## Backend API

    GET /api/health
    GET /api/subjects
    GET /api/subjects/<slug>
    GET /api/files/<slug>/<file>
    GET /api/files/<slug>/<file>?download=1

Example: http://localhost:3000/api/files/artificial-intelligence/prac03a_decision_tree_build.py

## Deploy

Option 1 - Static hosting (simplest, frontend only): upload frontend/index.html to Netlify, Vercel, GitHub Pages or any web host.

Option 2 - Node hosting (Render, Railway, etc.): push this folder to GitHub, create a new Web Service, set
Build Command: (leave empty)  Start Command: npm start
The server reads the PORT variable that the host provides.

Option 3 - Docker:

    docker build -t practical-library .
    docker run -p 3000:3000 practical-library

## Running the practical files

- Python files: install the libraries named in the file's requirement line (for example pip install pandas scikit-learn matplotlib), keep the dataset CSV in the same folder as the .py file, then run python file.py
- AI datasets: play_tennis.csv, SVM_Binary_Classification_Dataset.csv, diseases_extended.csv, diabetes.csv (in code_files/artificial-intelligence)
- CIS: pycryptodome is needed for RSA and digital signature (pip install pycryptodome)
- STQA Java files: JDK 11+, Eclipse and Selenium 4 JARs. Create the class in the package named on its first line, or delete that line.
- STQA JMeter: open stqa_prac14_load_test_plan.jmx in Apache JMeter (File > Open).

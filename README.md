# Asynchronous parser of PEP document 

---
![python](https://img.shields.io/badge/Python-3.9.0-green)
![Scrapy](https://img.shields.io/badge/Scrapy-2.5.1-green)
![Regex](https://img.shields.io/badge/Regex-grey)
![flake8](https://img.shields.io/badge/flake8-4.0.1-green)
---
## Contents:
- [Introduction](#introduction)
- [Parsing PEP documents](#parsing-pep-documents)
- [Instruction to start](#instruction-to-start)

---
### <anchor>Introduction</anchor>
The project to write web page parser using Scrapy.
The project implements a parser for collecting version
information _PEP (Python Enhancement Proposals)_

----
### <anchor>Parsing PEP documents</anchor>
The parser collects information (Number, Name и Status) about
PEP documents from website https://peps.python.org/ and
saves in _csv_ file (directory _result_).
The format of file name: _pep_(%datetime%).csv

Also parser counts the number of documents with a certain status,
counts the total number of PEP documents and
saves this information in a _csv_ file (directory _result_)
The format of file name: _status_summary_(%datetime%).csv

----
### <anchor>Instruction to start</anchor>
<details>

1. Clone the repository to the local machine
`git clone git@github.com:Andrey-Kugubaev/scrapy_parser_pep.git`
2. Install and activate the virtual environment
`python -m venv venv` or `python3 -m venv venv`,
then `source venv/Scripts/activate` or `source venv/bin/activate`
3. Install Dependencies `pip install -r requirements.txt`
4. Run parsers `scrapy crawl pep`

</details>
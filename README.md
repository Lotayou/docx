# Chinese document parsing and analysis
This python module is intended to be used by developers to parse microsoft word docx files and give information like datetime stamps for file creation, modification and last access, It also return name of author of the file.

### Installation
Configurations for this project are all in `setup.py` file
Just run `python setup.py install`.
Also, run `pip3 install jiaba` for Chinese parsing and analysis.

### Usage
`python demo.py -f legal_doc.docx -p parse_result.txt -a analysis_result.txt --topK 20`


------------

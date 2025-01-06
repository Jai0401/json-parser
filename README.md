# json-parser(Incomplete...)
### Overview:
- **Description:**  
  This project is a comprehensive JSON parser featuring both a lexer and a parser. Its primary objective is to efficiently parse JSON strings into Python objects.
- **Purpose:**  
  The JSON parser supports all valid JSON data types, including strings, numbers, booleans, arrays, and objects. It incorporates robust error handling and provides an intuitive API for seamless JSON parsing.
- **Features:**  
  - Supports parsing JSON strings with all valid data types  
  - Incorporates error handling mechanisms  
  - Offers a simple and intuitive API for JSON parsing
- **Audience:**  
  Developers who require JSON parsing capabilities in their Python applications

### Setup Instructions:
- **Prerequisites:** Python 3.6 or later
- **Installation:** Install using pip: `pip install json-parser`
- **Configuration:** No configuration required
- **Environment:** Any Python environment
- **First Run:** Import the `json_parser` module and utilize the `lex()` function for tokenization and `parse()` function for constructing Python objects.

### Core Modules:
- **Components:**  
  - `lexer.py`: JSON string tokenization  
  - `parse.py`: JSON token parsing into Python objects
- **Relationships:** The lexer tokenizes the JSON string, and the parser uses these tokens to build a Python object.
- **Functionalities:** Tokenization and parsing of JSON strings into Python objects
- **Architecture:** Modular design with independent lexer and parser modules. The parser relies on tokens generated by the lexer to build Python objects.

### Usage Examples:
- **Scenarios:**  
  - Parsing JSON data from web APIs  
  - Parsing JSON data from files
- **Code Samples:**  
  ```python
  import json_parser

  json_string = '{"key": "value"}'
  tokens = json_parser.lex(json_string)
  json_object = json_parser.parse(tokens)



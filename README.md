# LanceDB Snippet Manager

LanceDB Snippet Manager is a customizable library for efficient storage,
retrieval, and searching of code snippets using LanceDB, a vector database for
AI applications. It leverages advanced embedding techniques for intelligent
snippet management and retrieval, with flexibility to adapt to various use cases.

## Features

- Customizable embedding models and configurations
- Flexible storage and indexing of code snippets
- Generate embeddings for efficient similarity search
- Advanced search capabilities using vector similarity and hybrid search
- Support for multiple programming languages
- Reranking support for improved search results
- Easily extensible for specific use cases

## Installation

To install the LanceDB Snippet Manager, run the following command:

```bash
pip install git+https://github.com/mkpro118/lancedb-snippets.git
```

This will install the latest version of the package directly from the GitHub repository.

## Project Structure

- `snippets.lancedb.config.py`: Defines configuration classes (`DBConfig`, `ST_Config`) for the database and embedding models
- `db_connection.py`: Manages LanceDB connections (`SnippetDBConnection`) and table operations
- `factory.py`: Creates the schema (`SnippetSchemaFactory`) for storing snippets in LanceDB
- `generator.py`: Generates responses (`SnippetGenerator`) based on snippet searches
- `table.py`: Handles operations on individual snippet tables (`SnippetTable`)
- `languages.py`: Defines supported programming languages (`Language` enum) and language detection
- `snippets.py`: Defines the `Snippet` class and related operations

## Usage

Here's a basic example of how to use the LanceDB Snippet Manager:

```python
from snippets.config import ST_Config
from snippets.db_connection import SnippetDBConnection
from snippets.snippets import Snippet
from snippets.languages import Language

# Initialize the database connection
config = ST_Config()
db_connection = SnippetDBConnection.from_uri(config, ".snippet-db")

# Create or get a table
table = db_connection.get_or_create_table(config, "my_snippets")

# Create a snippet
snippet = Snippet(
    text="print('Hello, World!')",
    language=Language.PY,
    filename="hello.py"
)

# Add the snippet to the table
table.add_snippets(snippet)

# Search for snippets
results = table.search("print hello", language="Python")

# Display results
for row in results.iterrows():
    print(f"Language: {row['language']}")
    print(f"Filename: {row['filename']}")
    print(f"Snippet: {row['text']}")
    print("---")
```

## Customization

The library is designed to be highly customizable:

1. **Embedding Models**: You can use different embedding models by customizing the `DBConfig` class in `config.py`. The default uses the BAAI/bge-small-en-v1.5 model, but you can easily switch to other models supported by the sentence-transformers library.

2. **Database Configuration**: The `SnippetDBConnection` class in `db_connection.py` allows you to customize the database connection, including the use of in-memory databases or persistent storage.

3. **Language Support**: The `Language` enum in `languages.py` can be extended to support additional programming languages as needed.

4. **Schema Customization**: The `SnippetSchemaFactory` in `factory.py` allows you to customize the schema for storing snippets, enabling you to add additional metadata fields if required.

5. **Search Customization**: The `search` method in `table.py` supports customizable search parameters and reranking options.

## Basic Usage

Here's a simple example of how to use the LanceDB Snippet Manager:

```python
from snippets.config import ST_Config
from snippets.db_connection import SnippetDBConnection
from snippets.snippets import Snippet
from snippets.languages import Language

# Initialize with custom configuration
config = ST_Config(model="all-MiniLM-L6-v2")  # Using a different embedding model
db_connection = SnippetDBConnection.from_uri(config, ".snippet-db")

# Create or get a table
table = db_connection.get_or_create_table(config, "my_snippets")

# Create and add a snippet
snippet = Snippet(
    text="print('Hello, World!')",
    language=Language.PY,
    filename="hello.py"
)
table.add_snippets(snippet)

# Search for snippets with custom parameters
results = table.search("print hello", language="Python", limit=10)

for row in results.iterrows():
    print(f"Language: {row['language']}")
    print(f"Filename: {row['filename']}")
    print(f"Snippet: {row['text']}")
    print("---")
```

## Advanced Usage

For more advanced usage and customization options, please refer to the individual module documentation:

- `config.py`: Customize embedding models and database configurations
- `db_connection.py`: Customize database connections and table management
- `factory.py`: Customize snippet schema
- `generator.py`: Extend snippet response generation
- `table.py`: Customize search and indexing operations
- `languages.py`: Add support for additional programming languages
- `snippets.py`: Extend the Snippet class with additional functionality

## Dependencies

- LanceDB
- NumPy
- Pandas
- Sentence Transformers (this package depends on `torch`, which is a heavy dependency)
- Tantivy
- Wikipedia-API

For a full list of dependencies, please refer to the `requirements.txt` file.

## Development

This project uses:

- `mypy` for static type checking
- `black` for code formatting
- `isort` for import sorting

Configuration for these tools can be found in `pyproject.toml` and `mypy.ini`.

## Contributing

Contributions are welcome! Whether it's extending language support, adding new embedding models, or improving search algorithms, feel free to submit a [Pull Request](https://github.com/mkpro118/lancedb-snippets/pulls).

## License

This project is licensed under the MIT License.

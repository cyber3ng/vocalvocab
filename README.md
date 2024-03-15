# VocalVocab

VocalVocab is a Python application designed to assist language learners in expanding their vocabulary through the use of Anki flashcards. With VocalVocab, users can generate Anki decks from CSV files containing phrases in their target language, along with their pronunciations and translations. This tool leverages text-to-speech technology to add audio to each flashcard, enhancing the learning experience by allowing users to hear the correct pronunciation of each phrase.

## Features

- Generate Anki decks from CSV files.
- Support for multiple languages.
- Automatic generation of audio for phrases using text-to-speech.
- Customizable deck names and IDs.

## Supported Languages

VocalVocab supports text-to-speech for a wide range of languages, including:

Afrikaans, Arabic, Armenian, Azerbaijani, Belarusian, Bosnian, Bulgarian, Catalan, Chinese, Croatian, Czech, Danish, Dutch, English, Estonian, Finnish, French, Galician, German, Greek, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Kazakh, Korean, Latvian, Lithuanian, Macedonian, Malay, Marathi, Maori, Nepali, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tagalog, Tamil, Thai, Turkish, Ukrainian, Urdu, Vietnamese, and Welsh.

Please ensure your CSV files are appropriately formatted for the language you're targeting, especially when including pronunciations.

## Prerequisites

Before you can use VocalVocab, you must obtain an API key from OpenAI. VocalVocab's text-to-speech feature requires this key to access OpenAI's services.

### Obtaining an OpenAI API Key

1. Visit the [OpenAI API](https://openai.com/api/) website.
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section and follow the instructions to subscribe to a plan and obtain your API key.

### Configuring Your OpenAI API Key

Once you have your OpenAI API key, you need to make it available to VocalVocab by setting it as an environment variable on your system.

#### On Unix/macOS:

Add the following to your `.bashrc` or `.zshrc` file:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

#### On Windows:

1. Search for "Environment Variables" in your Start menu and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. Under the "User variables" section, click on "New..." to create a new environment variable.
4. Set "Variable name" to `OPENAI_API_KEY` and "Variable value" to your actual OpenAI API key.
5. Click "OK" to save the variable, and "OK" again to close each of the open dialogs.

Make sure to replace `'your_api_key_here'` with the actual API key you obtained from OpenAI.

## Installation

Ensure you have Python 3.6+ installed on your system. Clone the repository to your local machine:

```bash
❯ git clone https://github.com/yourusername/vocalvocab.git
❯ cd vocalvocab
```

Install the project and its dependencies:

```bash
❯ pip install .
```

## Usage

VocalVocab allows you to generate Anki decks from CSV files, with options to specify the deck name and ID. Below are examples of how to use these options.

### Create a New Deck

To generate an Anki deck without specifying a deck ID (a random ID will be generated), simply omit the `-i` option. This command creates a deck named "My Language Deck" from the specified CSV file:

```bash
❯ vocalvocab -n "My Language Deck" my-phrases.csv
Deck with ID 1865109643 has been saved to /Users/user/My Language Deck.apkg
```

- `-n` or `--name`: Name of the Anki deck (optional, defaults to "Vocalvocab Deck").

This command generates a new Anki deck with a unique, randomly generated ID.

### Add/Modify an Existing Deck

To generate an Anki deck with a specific ID, use the `-i` option. This is useful for adding new cards to an existing deck without impacting its New, Learn, and Due statistics. Specifying a deck ID allows you to maintain continuity in your learning process by seamlessly integrating new material:

```bash
❯ vocalvocab -n "My Language Deck" -i 1865109643 my-phrases.csv
Deck with ID 1865109643 has been saved to /Users/user/My Language Deck.apkg
```

- `-i` or `--id`: Unique integer ID for the deck. This ID should match the ID of the existing deck you wish to add cards to.

By specifying the `-i` option with the deck ID, you ensure that the newly generated deck will be recognized as part of the existing deck in Anki, thereby preserving your progress statistics. This feature is particularly useful when you want to expand an existing deck with new phrases or vocabulary without starting over or creating a separate deck.

## CSV File Formats

VocalVocab supports two CSV formats: with or without pronunciations.

### With Pronunciations

The CSV file must have exactly three headers: `phrase`, `pronunciation`, and `translation`. 

Example (Chinese with Pinyin and English translation):

```
phrase,pronunciation,translation
你好,Nǐ hǎo,Hello
谢谢,Xièxiè,Thank you
```

### Without Pronunciations

If pronunciations are not available or needed, the CSV file can have empty values for the pronunciation column.

Example:

```
phrase,pronunciation,translation
你好,,Hello
谢谢,,Thank you
```

When a CSV file without pronunciations is used, VocalVocab will still generate audio using text-to-speech but will not display pronunciation text on the flashcards.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

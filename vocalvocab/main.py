import argparse
import csv
import os
import random
from argparse import ArgumentTypeError
from .anki import create_deck, create_note, get_model, write_deck
from .tts import generate_speech
from .util import process_csv


def valid_id(value):
    min_id, max_id = 1 << 30, 1 << 31
    try:
        ivalue = int(value)
        if min_id <= ivalue < max_id:
            return ivalue
        else:
            raise ArgumentTypeError(f"ID must be between {min_id} and {max_id-1}, inclusive.")
    except ValueError:
        raise ArgumentTypeError("ID must be an integer.")
    

def valid_csv_file(csv_file_path):
    expected_headers = ['phrase', 'pronunciation', 'translation']
    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            actual_headers = reader.fieldnames
            if actual_headers != expected_headers:
                raise ArgumentTypeError(f"CSV file must have exactly these headers: {expected_headers}. Found: {actual_headers}")
            
            for row in reader:
                if len(row) != len(expected_headers):
                    raise ArgumentTypeError(f"Error at line {reader.line_num}: Expected {len(expected_headers)} fields but found {len(row)}.")
    except FileNotFoundError:
        raise ArgumentTypeError(f"File not found: {csv_file_path}")
    return csv_file_path 


def main():
    parser = argparse.ArgumentParser(description="Generate Anki decks from CSV input.")
    parser.add_argument('csv_file', type=valid_csv_file, help='Path to the input CSV file')
    parser.add_argument('-n', '--name', type=str, default='Vocalvocab Deck', help='Name of the Anki deck')
    parser.add_argument('-i', '--id', type=valid_id, default=random.randrange(1 << 30, 1 << 31), help='Deck ID')
    args = parser.parse_args()

    # Create deck
    deck = create_deck(args.name, args.id)

    # Define the model
    model = get_model()

    # Process the CSV file
    entries = process_csv(args.csv_file)

    audio_paths = []

    # Generate speech and flashcards
    for entry in entries:
        audio_path = generate_speech(entry['phrase'])
        audio_paths.append(audio_path)
        note = create_note(model, entry, audio_path)
        deck.add_note(note)

    # Save the .apkg file in the current directory
    output_file = os.path.join(os.getcwd(), f"{args.name}.apkg")  
    write_deck(deck, audio_paths, output_file)


if __name__ == '__main__':
    main()

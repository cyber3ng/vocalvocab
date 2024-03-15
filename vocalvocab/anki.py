import genanki
import os


def create_deck(deck_name, deck_id):
    my_deck = genanki.Deck(
        deck_id,  # This is how Anki differentiates between decks
        deck_name
    )
    return my_deck


def create_note(model, entry, audio_path):
    # 'entry' is a dictionary with 'phrase', 'pronunciation', and 'translation' keys
    fields = [entry['phrase'], f"[sound:{os.path.basename(audio_path)}]", entry['translation'], entry['pronunciation']]
    note = genanki.Note(
        model=model,
        fields=fields
    )
    return note


def get_model():
    # The Note Type the deck will use
    my_model = genanki.Model(
        1892538342,  # Random long integer ID that identifies the Note Type
        'VocalVocab',
        fields=[
            {'name': 'Phrase'},
            {'name': 'Audio'},
            {'name': 'Translation'},
            {'name': 'Pronunciation'}
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Phrase}}<br>{{Audio}}',  # Front of card
                'afmt': '{{FrontSide}}<hr id="answer">{{Translation}}<br>{{Pronunciation}}',  # Back of card
            },
        ],
        css='''
            .card {
             font-family: arial;
             font-size: 20px;
             text-align: center;
             color: black;
             background-color: white;
            }
        '''
    )
    return my_model


def write_deck(deck, audio_files, path):
    package = genanki.Package(deck)
    package.media_files = audio_files
    package.write_to_file(path)
    print(f"Deck with ID {deck.deck_id} has been saved to {path}")

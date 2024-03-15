import unittest
import os
from pathlib import Path
from vocalvocab.util import process_csv
from vocalvocab.anki import create_deck, create_note, get_model
from vocalvocab.tts import generate_speech


class TestVocalVocab(unittest.TestCase):
    def setUp(self):
        self.csv_path = Path("tests") / "csvs" / "arabic.csv"

    def test_process_csv(self):
        # Test that CSV files are processed correctly
        entries = process_csv(self.csv_path)
        self.assertTrue(isinstance(entries, list))
        self.assertTrue(all(isinstance(entry, dict) for entry in entries))

    def test_generate_speech(self):
        # Test that speech generation creates a file
        phrase = "Hello"
        audio_path = generate_speech(phrase)
        self.assertTrue(os.path.exists(audio_path))
        os.remove(audio_path)

    def test_create_deck_and_note(self):
        # Test deck and note creation
        model = get_model()
        deck = create_deck("Test Deck", 123456)
        entry = {"phrase": "Hello", "pronunciation": "", "translation": "Hello"}
        note = create_note(model, entry, "")
        deck.add_note(note)
        self.assertEqual(len(deck.notes), 1)

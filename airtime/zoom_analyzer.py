import re
from collections import defaultdict

SPEECH_REGEX = r'\[(.*?)\] (\d{2}:\d{2}:\d{2})'
TIMESTAMP_REGEX = r'\[.*?\] \d{2}:\d{2}:\d{2}'


def read_transcript(file_name):
    """Reads a transcript file & returns a dictionary with speakers' texts."""
    speaker_texts = defaultdict(str)
    current_speaker = None
    timestamp = None

    try:
        with open(file_name, 'r') as f:
            for line in f:
                match = re.match(SPEECH_REGEX, line)
                if match:
                    current_speaker = match.group(1)
                    timestamp = match.group(2)
                elif line.strip() != '' and current_speaker is not None:
                    speaker_texts[current_speaker] += \
                        f'\n[{current_speaker}] {timestamp}\n{line.strip()}'
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except IsADirectoryError:
        print(f"{file_name} is a directory, not a file.")
    except Exception as e:
        print("An error occurred while analyzing the transcript.")
        print(type(e).__name__)
        print(str(e))
    return speaker_texts


def calculate_word_totals(speaker_texts):
    """Calculates word totals both for each speaker and the overall meeting."""
    word_totals = {}

    for speaker, text in speaker_texts.items():
        cleaned_text = re.sub(TIMESTAMP_REGEX, '', text)
        speaker_texts[speaker] = cleaned_text

        words = cleaned_text.split()
        word_totals[speaker] = len(words)

    overall_total = sum(word_totals.values())
    return word_totals, overall_total


def print_results(word_totals, overall_total):
    """Prints the results."""
    number_of_speakers = len(word_totals)

    print("MEETING TOTALS")
    print("- " + format(overall_total, ',') + " words")
    print("- " + str(number_of_speakers) + " speakers\n")
    print("SPEAKER TOTALS")

    for speaker, total in word_totals.items():
        percentage = (total / overall_total) * 100
        print("- " + speaker + ": " + format(total, ',')
              + " words (" + f"{percentage:.1f}" + "% of meeting)")


def analyze_zoom_transcript(file_name):
    """Processes a Zoom transcript file."""
    try:
        speaker_texts = read_transcript(file_name)
        if speaker_texts is None:
            return
        word_totals, overall_total = calculate_word_totals(speaker_texts)
        print_results(word_totals, overall_total)
    except Exception as e:
        print("An unexpected error occurred while analyzing the transcript.")
        print(f"Exception type: {type(e).__name__}, \
              Exception message: {str(e)}")


analyze_zoom_transcript('../../transcript.txt')

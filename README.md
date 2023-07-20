# Airtime

This package contains Python scripts for analyzing meeting transcripts from Zoom and Microsoft Teams meetings. The scripts read the transcript files, calculate spoken word totals for each speaker, and print out the analyzed results.

The intended purpose of this package is to allow users to determine what percentage of a given meeting was allocated to which speaker(s), with the goal of fostering better collaborative environments among teams in future meetings.

## Version

The latest version of this package is v1.0.0-alpha.

## Installation and requirements

```
pip install airtime
```

This package uses only the Python standard library.
No external dependencies are required to run these scripts.

## Usage

After installing the package, it can be used as follows:

- For analyzing transcripts from Zoom meetings:

```
from airtime import zoom_analzyer

zoom_analzyer.analyze_zoom_transcript('path_to_your_transcript.txt')

```

- For analyzing transcripts from Microsoft Teams meetings:

```
from airtime import teams_analzyer

teams_analzyer.analyze_teams_transcript('path_to_your_transcript.vtt')
```

Note the different file formats for the respective transcript files.

## Output
These scripts print:

- Meeting totals (total words and total speakers)
- Speaker totals (total words per speaker and their contributed percentage to the meeting total)

Example output:

```
MEETING TOTALS
- 1,000 words
- 2 speakers

SPEAKER TOTALS
- Holmes: 900 words (90.0% of meeting)
- Watson: 100 words (10.0% of meeting)
```

## Contributing

Contributions to this package are welcome, and especially in the form of introducing additional transcript formats from other services (e.g., Google Meet). Please open an issue to discuss your idea or submit a Pull Request.

## License

This package is licensed under the terms of the GNU Affero General Public License (GNU AGPL).

## Contact information

Jana M. Perkins, the developer of this package, can be reached via [Twitter (@jcontd)](https://twitter.com/jcontd) or the contact information on her [website](https://jcontd.com).

## Citation

Perkins, J. M. (2023). Airtime. github.com/jcontd/airtime
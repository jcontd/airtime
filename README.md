[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL--3.0-brightgreen.svg)](https://www.gnu.org/licenses/agpl-3.0)
![Version](https://img.shields.io/badge/version-v1.0.2-blue)

# Airtime

This package contains Python scripts for analyzing transcript files from Zoom and Microsoft Teams meetings.

These scripts function by reading in a transcript, calculating the spoken word totals for each of its speakers, and displaying the analyzed results. The intended purpose of this package is to allow users to determine what percentage of a given meeting was allocated to which speaker(s).

## Why this matters

Airtime is a project management tool which operates from the assumption that teams and organizations could only stand to benefit from an increase in perspectives from and participation among their members. The first step, of course, remains to create good teams. Once that’s been accomplished, the second step is to then allow all those involved the necessary time and space to make the contributions for which their expertise was initially sought out.

This tool aims to provide those who regularly undertake collaborative work in fields that base their decisions on statistical findings with the necessary data to foster more genuinely collaborative work environments. It’s one thing, in other words, for a team member to convey to their project lead that they often have their contributions minimized in meetings while others monopolize the floor; it’s quite another for them to be able to demonstrate that the data support their experiences and that there’s room to move forward with a data-driven solution.

## Key features

✅ Ease of use: Just 3 lines of code from installation to analysis.

✅ Privacy and security: All analyses run locally on your machine.

✅ Efficient computing: Lightweight algorithms for fast processing times.

*Coming soon: a step-by-step implementation guide for non-developers with no prior Python experience. If you’d like to be notified when this becomes available, please send me an email.*

## Version

The latest version of this package is v1.0.2.

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

zoom_analzyer.analyze_zoom_transcript("transcript.txt")
```

**Note**: recent releases of Zoom will output several transcript formats, but only one of these formats will preserve the speaker names which are essential to this analysis. To access the required transcript format, *before the meeting ends*, navigate to Captions > View full transcript > Save transcript.

&nbsp;
&nbsp;

- For analyzing transcripts from Microsoft Teams meetings:

```
from airtime import teams_analzyer

teams_analzyer.analyze_teams_transcript("transcript.vtt")
```


## Output
These scripts print:

- Meeting totals (total words and total speakers)
- Speaker totals (total words per speaker and their contributed percentage to the meeting total)

Example output:

```
MEETING TOTALS
- 1,000 words
- 2 speaker(s)

SPEAKER TOTALS
- Holmes: 900 words (90.0% of meeting)
- Watson: 100 words (10.0% of meeting)
```

## Contributing

Contributions to this package are welcome, and especially in the form of introducing additional transcript formats from other services (e.g., Google Meet). Please open an issue to discuss your idea or submit a pull request.

## License

This package is licensed under the terms of the GNU Affero General Public License (GNU AGPL).

## Contact information

Jana M. Perkins, the developer of this package, can be reached via [Twitter (@jcontd)](https://twitter.com/jcontd) or the contact information on her [website](https://jcontd.com).

## Citation

Perkins, J. M. (2023). Airtime. github.com/jcontd/airtime

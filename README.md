# Takosa App

## Core Requirements

- Ability to load/upload two text files (.txt format).
- Ability to import or enter a list of search values/identifiers for bulk searches.
- Search all values from the search list against both text files.
- Extract matching lines, entries, or associated values from each text file.
- Display and process all searched values, including matched and unmatched results.
- Compare values retrieved from both text files and flag mismatches while preserving all search results.
- Support large text files efficiently.

## Search & Comparison logic

- Search Text file 1 for matching entries.
- Search Text file 2 for matching entries.
- Return associated values or matching lines from both files.
- Compare returned values or records between both files.
- Identify missing entries and mismatched values.
- Include results even when data exists in only one file.


## Output requirements (excel report)

- Search value/identifier
- Status (Found in file 1 / file 2 / both / missing)
- Result returned from text file 1
- Result returned from text file 2
- Comparison Status (match / mismatch / missing)
- Highlighted mismatch fields
- Color coded results
    - Green = Match
    - Red = Mismatch
    - Yellow = Missing Records

## Preferred Features

- GUI for easy file selection
- Ability to paste search values or upload a separate search list file
- Export all results into Excel
- Sorting/Filtering capability in the output report
- Error handling for invalid file formats or missing data
- Ability to process large datasets efficiently.

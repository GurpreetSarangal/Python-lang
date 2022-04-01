# Parsing

    To convert data in a certain format into a more usable format
    Application ranges from document parsing to deep learning and NLP (Natural Language Processing)

### Need for parsing

    There are various different formats in which data exits. Some formats are better suited to different applications. An individual program can only be expected to use a selection of these date formats. So, inevitably there is a need to convert data from one format to another for consumption by different programs.

#### Parsing text in standard format

    If data is in a standard format, then we can use an existing package to read the data.
    For Example,

    import pandas as pd
    df = pd.read_csv('data.txt')
    print(df)

    output:
      a b c
    0 1 2 3
    2 4 5 6
    3 7 8 9

#### Parsing text using string methods

    Python provides some string methods which can be used to ex

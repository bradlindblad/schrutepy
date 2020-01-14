import pandas


def load_schrute():
    """
    The entire script transcriptions from The Office in pandas dataframe format.
    """

    full_path = "https://github.com/bradlindblad/schrutepy/raw/master/data/schrute.csv"

    df = pandas.read_csv(full_path)
    df = df.drop("Unnamed: 0", axis=1)

    return df

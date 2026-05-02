
def clean_duration(df):
    df = df.copy()
    df['duration_int'] = (
                        df['duration']
                          .str.replace('min', '', case = False)
                          .str.strip()
                          .astype(float)
                          )
    return df

def clean_categories(df):
    df = df.copy()
    df['categoria'] = (
        df['categoria']
        .str.replace('Movies', '', case = False)
        .str.strip()
        )
    df = df[df['categoria'].notna() & (df['categoria'] != '')]
    return df



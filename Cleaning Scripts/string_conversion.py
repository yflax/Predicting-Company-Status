def change_types_string(df, cols):
    for column in cols:
        if column in df:
            df[column] = df[column].astype(str)

    return df 
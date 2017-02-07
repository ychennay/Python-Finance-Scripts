def adjustment_prorated(path, primary_key_name, writeoutpath):

    df = pd.read_csv(path).set_index(primary_key_name)
    adjustments_dict = {}
    counter = 0
    file = open(writeoutpath, 'w')
    for column in range(1, len(df.columns)):
        adjustments_dict[df.columns[column]] = 0

    for row in df.index:
        if row % 100 == 0:
            print("On Restaurant ID {0}".format(row))
        for column in range(1,len(df.columns)):
            if df.ix[row, column] == 0:
                try:
                    if df.ix[row, column + 1] > 0 and df.ix[row, column + 2] > 0:
                        if df.ix[row, column + 1] != df.ix[row, column + 2]:

                            print("\n\n\n\n", file=file)
                            print("-------------------------------------------------------------------------", file=file)
                            print('{0}|{1} | {2}'.format(df.columns[column], df.columns[column+1],df.columns[column+2]), file=file)
                            print('${0}           | ${1}           | ${2}'.format(df.ix[row, column], df.ix[row, column + 1], df.ix[row, column+2]), file=file)
                            adjustment = df.ix[row, column + 2] - df.ix[row, column + 1]
                            df.ix[row, column + 1] = df.ix[row, column + 2]
                            print("NEW:", file=file)
                            print('${0}           | ***${1}***     | ${2}'.format(df.ix[row, column], df.ix[row, column + 1], df.ix[row, column+2]), file=file)
                            print("\n ID {0} altered at month {1}, adjusted by ${2}".format(row, df.columns[column+1], adjustment), file=file)
                            print("-------------------------------------------------------------------------", file=file)
                            adjustments_dict[df.columns[column]] = adjustments_dict[df.columns[column]] + adjustment
                            counter += 1
                except IndexError:
                    pass

    return df, adjustments_dict

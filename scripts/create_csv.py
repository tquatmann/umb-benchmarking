import os,sys

IMPORT_TIME = "import_time"
EXPORT_TIME = "export_time"

def save_csv(csv, path : str):
    with open(path, 'w') as csv_file:
        for line in csv:
            line_strs = [str(x) for x in line]
            csv_file.write("\t".join(line_strs) + "\n")
    print("Saved results invocations to '{}'.".format(path))


def parse_float(text : str, before : str, after : str):
    start = text.find(before)
    if start == -1:
        return None
    start += len(before)
    end = text.find(after, start)
    if end == -1:
        return None
    value_str = text[start:end].strip()
    try:
        value = float(value_str)
        return value
    except:
        return None

def parse_storm_log(log : str, what : str):
    symb_parsing = parse_float(log, "Time for model input parsing: ", "s.\n")
    construction = parse_float(log, "Time for model construction: ", "s.\n")
    preprocessing = parse_float(log, "Time for model preprocessing: ", "s.\n")
    export = parse_float(log, "Time for model export: ", "s.\n")
    if what == IMPORT_TIME:
        if construction is None:
            return None
        return construction + (preprocessing if preprocessing is not None else 0.0) + (symb_parsing if symb_parsing is not None else 0.0)
    elif what == EXPORT_TIME:
        return export

def create_csv(log_dir : str, what : str, not_available_str : str = "N/A"):
    row_headers = []
    column_headers = []
    contents = dict() # rows -> columns --> values
    for logfile in os.listdir(log_dir):
        if not logfile.endswith(".log"):
            continue
        log_path = os.path.join(log_dir, logfile)
        with open(log_path, "r") as f:
            log_content = f.read()
        parts = logfile[:-4].split("_")
        if len(parts) != 5:
            print("Warning: unexpected log file name format: {}".format(logfile))
            continue
        column = "_".join(parts[0:4])
        row = parts[4]
        if row not in row_headers:
            row_headers.append(row)
        if column not in column_headers:
            column_headers.append(column)
        if row not in contents:
            contents[row] = dict()
        value = parse_storm_log(log_content, what)
        if value is None:
            contents[row][column] = not_available_str
        else:
            contents[row][column] = value
    column_headers.sort()
    row_headers.sort()
    csv_lines = [["Model"] + column_headers]
    for row in row_headers:
        line = [row]
        for column in column_headers:
            if row in contents and column in contents[row]:
                line.append(contents[row][column])
            else:
                line.append(not_available_str)
        csv_lines.append(line)
    return csv_lines

if __name__ == "__main__":
    print("Creates csv files from logs. Usage:\n\tpython {} <log directory>".format(sys.argv[0]))
    if len(sys.argv) != 2:
        print("Invalid number of arguments.")
        sys.exit(1)
    log_dir = sys.argv[1]

    import_csv = create_csv(log_dir, IMPORT_TIME)
    print(import_csv)
    save_csv(import_csv, "import_times.csv")
    export_csv = create_csv(log_dir, EXPORT_TIME)
    save_csv(export_csv, "export_times.csv")





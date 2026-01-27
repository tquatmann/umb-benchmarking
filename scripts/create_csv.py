import os,sys

IMPORT_TIME = "import_time"
EXPORT_TIME = "export_time"
EXPORT_SIZE = "export_size"
WALL_TIME = "wall_time"

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

def parse_prism_log(log : str, what : str):
    if "Return code: None (timeout)" in log:
        return "TO"
    memouts = ["java.lang.OutOfMemoryError", "IllegalArgumentException: Illegal Capacity: -1"]
    if any(memout in log for memout in memouts):
        return "MO"
    if "Error: Currently, the sparse engine cannot handle models with more than 2147483647 states," in log:
        return "ERR"
    if "tra,lab" in log: return "ASDF" # todo
    assert "File does not exist." not in log, "Log indicates missing file: {}".format(log)

def parse_modest_log(log : str, what : str):
    if "Return code: None (timeout)" in log:
        return "TO"
    memouts = ["error: Out of memory."]
    if any(memout in log for memout in memouts):
        return "MO"
    if "oscillators" in log and "Return code: -9" in log:
        return "ERR" # special case for known issue
    if "oscillators" in log and "Return code: -6" in log:
        return "ERR" # special case for known issue
    if "kanban" in log and "Return code: -6" in log:
        return "ERR" # special case for known issue
    if "fms" in log and "Return code: -6" in log:
        return "ERR" # special case for known issue
    if "Complex initial states specifications are not yet supported." in log:
        return "ERR"
    if "cluster.64-2000-20" in log: return "ASDF" # todo
    assert "File does not exist." not in log, "Log indicates missing file: {}".format(log)
    if what == IMPORT_TIME:
        assert "+ State space exploration" in log, "Unexpected modest log format: {}".format(log)
        sublog = log[log.find("+ State space exploration"):]
        sublog = sublog[sublog.find("\n\n")]

    assert False, "Log parsing for modest not yet implemented: {}".format(log)


def parse_storm_log(log : str, what : str):
    if "Return code: None (timeout)" in log:
        return "TO"
    memouts = ["Maximum memory exceeded.", "The message of this exception is: std::bad_alloc"]
    if any(memout in log for memout in memouts):
        return "MO"
    if "Return code: -9" in log and "bluetooth.1" in log:
        return "MO"
    if " does not have an extension to determine the model export format" in log: return "ASDF" # todo
    assert "File does not exist." not in log, "Log indicates missing file: {}".format(log)
    jani_parsing = parse_float(log, "Time for model input parsing: ", "s.\n")
    construction = parse_float(log, "Time for model construction: ", "s.\n")
    preprocessing = parse_float(log, "Time for model preprocessing: ", "s.\n")
    export = parse_float(log, "Time for model export: ", "s.\n")
    if what == IMPORT_TIME:
        if construction is None:
            return None
        return construction + (preprocessing if preprocessing is not None else 0.0) + (jani_parsing if jani_parsing is not None else 0.0)
    elif what == EXPORT_TIME:
        return export

def create_csv(log_dir : str, what : str, not_available_str : str = "N/A"):
    row_headers = []
    column_headers = []
    contents = dict() # rows -> columns --> values
    for logfile in os.listdir(log_dir):
        if not logfile.endswith(".log"):
            continue
        parts = logfile[:-4].split("_")
        if len(parts) != 6:
            print("Warning: unexpected log file name format: {}".format(logfile))
            continue
        tool = parts[0]
        src_format = parts[1]
        task = parts[2]
        cfg = parts[3]
        if what == IMPORT_TIME and task.startswith("to-"):
            continue
        if what == EXPORT_TIME and not task.startswith("to-"):
            continue
        column = "_".join(parts[0:4])
        row = parts[4]
        rep = int(parts[5].replace("rep", "")) - 1
        if row not in row_headers:
            row_headers.append(row)
        if column not in column_headers:
            column_headers.append(column)
        if row not in contents:
            contents[row] = dict()
        if column not in contents[row]:
            contents[row][column] = []
        while len(contents[row][column]) <= rep:
            contents[row][column].append("")
        with open(os.path.join(log_dir, logfile), "r") as f:
            log_content = f.read()
        if tool == "storm":
            value = parse_storm_log(log_content, what)
        elif tool == "prism":
            value = parse_prism_log(log_content, what)
        elif tool == "modest":
            value = parse_modest_log(log_content, what)
        else:
            raise AssertionError("Unexpected tool: {}".format(tool))
        if value is None:
            contents[row][column][rep] = not_available_str
        else:
            contents[row][column][rep] = value
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
    save_csv(import_csv, "import_times.csv")
    export_csv = create_csv(log_dir, EXPORT_TIME)
    save_csv(export_csv, "export_times.csv")





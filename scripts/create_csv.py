import os,sys
from collections import OrderedDict

IMPORT_TIME = "import_time"
EXPORT_TIME = "export_time"
EXPORT_SIZE = "export_size"
FULL_TIME = "full_time"

def save_csv(csv, name : str):
    with open(name + ".csv", 'w') as csv_file:
        for line in csv:
            line_strs = [str(x) for x in line]
            csv_file.write("\t".join(line_strs) + "\n")
    print("Saved results invocations to '{}'.".format(name + ".csv"))

def avg_csv(csv, name : str):
    a = [csv[0]]  # header
    for row in csv[1:]:
        new_row = [row[0]]  # first column is the model name
        for entry in row[1:]:
            if entry == "N/A":
                new_row.append("")
            else:
                values = [float(x) for x in entry if x != "N/A"]
                if len(values) == 0:
                    new_row.append("")
                else:
                    avg_value = sum(values) / len(values)
                    new_row.append(avg_value)
        a.append(new_row)
    save_csv(a, name + "_avg")
    return a

def quantile_csv(csv, name : str, min_value : float = 0.1):
    columns = [[]] * len(csv[0][1:])
    for row in csv[1:]:
        for i, entry in enumerate(row[1:]):
            if entry == "":
                continue
            columns[i] = columns[i] + [entry]
    for i in range(len(columns)):
        columns[i].sort()
    output = [["n"] + csv[0][1:]]
    for n in range(len(csv) - 1):
        line = [n + 1]
        for m in range(len(columns)):
            if n >= len(columns[m]):
                line.append("")
            else:
                line.append(columns[m][n])
        output.append(line)
    save_csv(output, name + "_quantile")

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
def parse_float_or_zero(text : str, before : str, after : str):
    value = parse_float(text, before, after)
    if value is None:
        return 0.0
    return value

def parse_walltime(log : str):
    return parse_float(log, "Wallclock time: ", " seconds")

def parse_prism_log(log : str, what : str):
    if what == FULL_TIME:
        if "Time for model checking" in log:
            return parse_walltime(log)
    if what == IMPORT_TIME:
        return parse_float(log, "Time for model construction: ", "seconds.")
    elif what == EXPORT_TIME:
        return parse_float(log, "Time for exporting: ", "seconds.")
    elif what == EXPORT_SIZE:
        sublog = log
        size = 0
        while "Size of output file is " in sublog:
            size += parse_float(sublog, "Size of output file is ", " bytes")
            sublog = sublog[sublog.find("Size of output file is ") + 1:]
        return size if size > 0 else None

def parse_modest_log(log : str, what : str):
    if what == FULL_TIME:
        pos1 = log.find("+ Property")
        if pos1 != -1 and log.find("Time", pos1) != -1:
            return parse_walltime(log)
    elif what == IMPORT_TIME:
        start_pos = log.find("+ State space")
        if start_pos == -1:
            return None
        sublog = log[start_pos:]
        sublog = sublog[:sublog.find("\n\n")]
        assert "Time" in sublog, "Unexpected modest log format: {}".format(log)
        importtime = parse_float_or_zero(sublog, "Time (exploration): ", " s")
        importtime += parse_float_or_zero(sublog, "Time (merging): ", " s")
        importtime += parse_float_or_zero(sublog, "Time (decompress): ", " s")
        importtime += parse_float_or_zero(sublog, "Time (validate): ", " s")
        importtime += parse_float_or_zero(sublog, "Time (load): ", " s")
        return importtime
    elif what == EXPORT_TIME:
        start_pos = log.find("+ UMB export")
        if start_pos == -1:
            start_pos = log.find("+ Export to ")
        if start_pos == -1:
            return None
        sublog = log[start_pos:]
        exporttime = parse_float(sublog, "Time: ", " s")
        return exporttime
    elif what == EXPORT_SIZE:
        sublog = log
        size = 0
        while "Size of output file is " in sublog:
            size += parse_float(sublog, "Size of output file is ", " bytes")
            sublog = sublog[sublog.find("Size of output file is ") + 1:]
        return size if size > 0 else None


def parse_storm_log(log : str, what : str):
    jani_parsing = parse_float_or_zero(log, "Time for model input parsing: ", "s.\n")
    construction = parse_float(log, "Time for model construction: ", "s.\n")
    preprocessing = parse_float_or_zero(log, "Time for model preprocessing: ", "s.\n")
    export = parse_float(log, "Time for model export: ", "s.\n")
    if what == FULL_TIME:
        if "Time for model checking" in log:
            return parse_walltime(log)
    elif what == IMPORT_TIME:
        if construction is None:
            return None
        else:
            return jani_parsing + construction + preprocessing
    elif what == EXPORT_TIME:
        return export
    elif what == EXPORT_SIZE:
        sublog = log
        size = 0
        while "Size of output file is " in sublog:
            size += parse_float(sublog, "Size of output file is ", " bytes")
            sublog = sublog[sublog.find("Size of output file is ") + 1:]
        return size if size > 0 else None

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
        if what in [IMPORT_TIME, FULL_TIME] and task.startswith("to-"):
            continue
        if what in [EXPORT_TIME, EXPORT_SIZE] and not task.startswith("to-"):
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

    # raw data
    import_csv = create_csv(log_dir, IMPORT_TIME)
    save_csv(import_csv, IMPORT_TIME)
    imp_t = avg_csv(import_csv, IMPORT_TIME)
    full_csv = create_csv(log_dir, FULL_TIME)
    save_csv(full_csv, FULL_TIME)
    full_t = avg_csv(full_csv, FULL_TIME)
    export_csv = create_csv(log_dir, EXPORT_TIME)
    save_csv(export_csv, EXPORT_TIME)
    exp_t = avg_csv(export_csv, EXPORT_TIME)
    size_csv = create_csv(log_dir, EXPORT_SIZE)
    save_csv(size_csv, EXPORT_SIZE)
    size = avg_csv(size_csv, EXPORT_SIZE)

    # quantile
    quantile_csv(imp_t, IMPORT_TIME)
    quantile_csv(full_t, FULL_TIME)
    quantile_csv(exp_t, EXPORT_TIME)
    quantile_csv(size, EXPORT_SIZE,1024)


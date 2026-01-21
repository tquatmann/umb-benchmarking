import os
import sys
import json
from collections import OrderedDict

def save_json(json_data, path : str):
    with open(path, 'w') as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent='\t')

def ensure_directory(path : str):
    if not os.path.exists(path):
        os.makedirs(path)

# File formats
SYMB = "symb"
UMB = "umb"
UMB_XZ = "umb-xz"
UMB_GZ = "umb-gz"
DRN = "drn"
TRA = "tra"

# Command template placeholders:
# %storm = path to storm binary
# %indir = path to model directory
# %outdir = path to output directory

# Storm
STORM = "storm"
storm_configurations = OrderedDict()
storm_configurations["labs"] = "--build-all-labels"
storm_configurations["labs-cudd"] = "--build-all-labels --engine dd-to-sparse --ddlib cudd"
storm_configurations["labs-sylvan"] = "--build-all-labels --engine dd-to-sparse --ddlib sylvan"
def storm_command(input_format : str, output_format : str, configuration : str) -> str:
    cmd = "%storm "
    # input
    if input_format == SYMB:
        cmd += "--jani %indir/model.jani " # note: using prism would require the --prismcompat option for CTMC
    elif input_format == UMB:
        cmd += "--explicit-umb %indir/model.umb "
    elif input_format == UMB_XZ:
        cmd += "--explicit-umb %indir/model.xz.umb "
    elif input_format == UMB_GZ:
        cmd += "--explicit-umb %indir/model.gz.umb "
    elif input_format == DRN:
        cmd += "--explicit-drn %indir/model.drn "
    else:
        raise AssertionError("Unsupported input format: " + input_format)
    # output
    if output_format == UMB:
        cmd += "--exportbuild %outdir/model.umb --compression none "
    elif output_format == UMB_XZ:
        cmd += "--exportbuild %outdir/model.xz.umb --compression xz "
    elif output_format == UMB_GZ:
        cmd += "--exportbuild %outdir/model.gz.umb --compression gzip "
    elif output_format == DRN:
        cmd += "--exportbuild %outdir/model.drn "
    else:
        raise AssertionError("Unsupported output format: " + output_format)
    # configuration
    assert configuration in storm_configurations, "Unknown Storm configuration: " + configuration
    cmd += storm_configurations[configuration] + " "
    # other options
    cmd += "--timemem" # additional time and memory output
    return cmd


if __name__ == "__main__":
    print("Creates invocation files in the current working directory. Usage:\n\tpython {} <bin directory> <model directory> <output directory> <logs directory> <time limit in seconds>".format(sys.argv[0]))
    if len(sys.argv) != 6:
        print("Invalid number of arguments.")
        sys.exit(1)

    # read settings and ensure directories and executables exist
    bin_directory = sys.argv[1]
    input_directory = sys.argv[2]
    output_directory = sys.argv[3]
    logs_directory = sys.argv[4]
    time_limit = int(sys.argv[5])
    for dir_path in [input_directory, output_directory, logs_directory]:
        ensure_directory(dir_path)
    for tool in [STORM]:
        bin_path = os.path.join(bin_directory, tool)
        if not os.path.exists(bin_path):
            print("Warning: {} binary '{}' not found.".format(tool, bin_path))

    # find models in input directory
    models = []
    for model in os.listdir(input_directory):
        model_input_dir = os.path.join(input_directory, model)
        if not os.path.isdir(model_input_dir): continue
        model_ok = True
        for filename in ["model.jani", "model.prism"]:
            if not os.path.exists(os.path.join(model_input_dir, filename)):
                print("Warning: model '{}' does not contain a {} file. Skipping.".format(model, filename))
                model_ok = False
        if model_ok:
            # we use underscores as separators, so they are not allowed in model names
            assert "_" not in model, "Underscores are not allowed in model path names. Got: " + model
            models.append(model)
    print("Found {} models in input directory:\n\t{}".format(len(models), "\n\t".join(models)))

    # Generate command templates
    command_templates = OrderedDict()
    def add_cmd_template(tool : str, input_format : str, output_format : str, configuration : str):
        for s in [tool, input_format, output_format, configuration]:
            # we use underscores as separators, so they are not allowed in identifiers
            assert "_" not in s, "Underscores are not allowed in template identifiers."
        template_id = f"{tool}_{input_format}_{output_format}_{configuration}"
        if tool == STORM:
            command_templates[template_id] = storm_command(input_format, output_format, configuration)
        else:
            raise AssertionError("Unsupported tool: " + tool)
    add_cmd_template(STORM, SYMB, UMB, "labs")
    add_cmd_template(STORM, SYMB, UMB, "labs-cudd")
    add_cmd_template(STORM, SYMB, UMB, "labs-sylvan")
    add_cmd_template(STORM, SYMB, UMB_XZ, "labs")
    add_cmd_template(STORM, SYMB, UMB_GZ, "labs")
    add_cmd_template(STORM, SYMB, DRN, "labs")


# Generate invocations
    invocations = []
    for cmd_id in command_templates:
        print("Command template '{}':\n\t{}".format(cmd_id, command_templates[cmd_id]))
        cmd_invs = []
        for model in os.listdir(input_directory):
            model_input_dir = os.path.join(input_directory, model)
            model_output_dir = os.path.join(output_directory, cmd_id, model)
            ensure_directory(model_output_dir)
            invocation_id = f"{cmd_id}_{model}"
            command = command_templates[cmd_id]
            command = command.replace("%indir", model_input_dir)
            command = command.replace("%outdir", model_output_dir)
            command = command.replace("%storm", os.path.join(bin_directory, STORM))

            invocation = OrderedDict()
            invocation["id"] = invocation_id
            invocation["commands"] = [command]
            invocation["time-limit"] = time_limit
            invocation["log-dir"] = logs_directory
            invocation["log"] = f"{invocation_id}.log"
            cmd_invs.append(invocation)
        cmd_inv_file =  f"inv_{cmd_id}.json"
        save_json(cmd_invs, cmd_inv_file)
        print("\tSaved {} invocations to '{}'.".format(len(cmd_invs), cmd_inv_file))
        invocations += cmd_invs
    # Save invocations to JSON file
    inv_file = "inv.json"
    save_json(invocations, os.path.join(os.getcwd(), inv_file))
    print("Saved {} invocations to '{}'.".format(len(invocations), inv_file))

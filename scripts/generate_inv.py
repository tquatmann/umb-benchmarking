import os
import sys
import json
from collections import OrderedDict

def save_invjson(inv_json, path : str):
    with open(path, 'w') as json_file:
        json.dump(inv_json, json_file, ensure_ascii=False, indent='\t')
    print("Saved {} invocations to '{}'.".format(len(inv_json), path))

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
    if output_format == "":
        pass # nothing to add
    elif output_format == UMB:
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

    def add_cmd_template(templates : OrderedDict,tool : str, input_format : str, output_format : str, configuration : str):
        for s in [tool, input_format, output_format, configuration]:
            # we use underscores as separators, so they are not allowed in identifiers
            assert "_" not in s, "Underscores are not allowed in template identifiers."
        template_id = f"{tool}_{input_format}_{output_format if len(output_format) > 0 else 'none'}_{configuration}"
        if tool == STORM:
            templates[template_id] = storm_command(input_format, output_format, configuration)
        else:
            raise AssertionError("Unsupported tool: " + tool)
    def generate_invocations(cmd_templates):
        invocations = []
        for cmd_id in cmd_templates:
            print("Command template '{}':\n\t{}".format(cmd_id, cmd_templates[cmd_id]))
            for model in os.listdir(input_directory):
                model_input_dir = os.path.join(input_directory, model)
                model_output_dir = os.path.join(output_directory, cmd_id, model)
                ensure_directory(model_output_dir)
                invocation_id = f"{cmd_id}_{model}"
                command = cmd_templates[cmd_id]
                command = command.replace("%indir", model_input_dir)
                command = command.replace("%outdir", model_output_dir)
                command = command.replace("%storm", os.path.join(bin_directory, STORM))

                invocation = OrderedDict()
                invocation["id"] = invocation_id
                invocation["commands"] = [command]
                invocation["time-limit"] = time_limit
                invocation["log-dir"] = logs_directory
                invocation["log"] = f"{invocation_id}.log"
                invocations.append(invocation)
        return invocations

    all_invocations = []

    storm_symb_exprt_templates = OrderedDict()
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, UMB, "labs")
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, UMB, "labs-cudd")
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, UMB, "labs-sylvan")
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, UMB_XZ, "labs")
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, UMB_GZ, "labs")
    add_cmd_template(storm_symb_exprt_templates, STORM, SYMB, DRN, "labs")
    storm_symb_exprt_invs = generate_invocations(storm_symb_exprt_templates)
    all_invocations += storm_symb_exprt_invs
    save_invjson(storm_symb_exprt_invs, "inv_storm_symb_exprt.json")

    storm_symb_templates = OrderedDict()
    add_cmd_template(storm_symb_templates, STORM, SYMB, "", "labs")
    add_cmd_template(storm_symb_templates, STORM, SYMB, "", "labs-cudd")
    add_cmd_template(storm_symb_templates, STORM, SYMB, "", "labs-sylvan")
    storm_symb_invs = generate_invocations(storm_symb_templates)
    all_invocations += storm_symb_invs
    save_invjson(storm_symb_invs, "inv_storm_symb.json")

    storm_drn_templates = OrderedDict()
    add_cmd_template(storm_drn_templates, STORM, DRN, "", "labs")
    storm_drn_invs = generate_invocations(storm_drn_templates)
    all_invocations += storm_drn_invs
    save_invjson(storm_drn_invs, "inv_storm_drn.json")

    storm_umb_templates = OrderedDict()
    add_cmd_template(storm_umb_templates, STORM, UMB, "", "labs")
    add_cmd_template(storm_umb_templates, STORM, UMB_XZ, "", "labs")
    add_cmd_template(storm_umb_templates, STORM, UMB_GZ, "", "labs")
    storm_umb_invs = generate_invocations(storm_umb_templates)
    all_invocations += storm_umb_invs
    save_invjson(storm_umb_invs, "inv_storm_umb.json")

    save_invjson(all_invocations, "inv_all.json")


import os,sys,shutil

if __name__ == "__main__":
    print("Copies generated files to the models folder. Usage:\n\tpython {} <output directory> <model directory>".format(sys.argv[0]))
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        sys.exit(1)

    file_dir = sys.argv[1]
    model_dir = sys.argv[2]
    cfgs_prioritized = [
        "storm_from-prism_to-jani_sparse",
        "storm_symb_umb-gz_labs", # umb gz
        "storm_symb_umb-xz_labs", # umb xz
        "storm_symb_umb_labs", "storm_symb_umb_labs-cudd", "storm_symb_umb_labs-sylvan" # umb
    ]
    for cfg in os.listdir(file_dir):
        if cfg not in cfgs_prioritized and "_none_" not in cfg:
            print("ERROR: unexpected configuration folder {}".format(cfg))
            exit(-1)
    cfgs = []
    for cfg in cfgs_prioritized:
        if cfg in os.listdir(file_dir):
            print("Found config folder {}".format(cfg))
            cfgs.append(cfg)


    for model in os.listdir(model_dir):
        for cfg in cfgs:
            source_path = os.path.join(file_dir, cfg, model)
            for file_name in ["model.umb", "model.umb.xz", "model.umb.gz", "model.drn", "model.drn.xz", "model.drn.gz", "model.jani"]:
                file_path = os.path.join(source_path, file_name)
                dest_path = os.path.join(model_dir, model, file_name)
                if os.path.exists(file_path) and not os.path.exists(dest_path):
                    print("Copying {} to model {}".format(file_path, model))
                    shutil.copyfile(file_path, dest_path)

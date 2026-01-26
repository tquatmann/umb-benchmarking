import os,sys,shutil

if __name__ == "__main__":
    print("Copies generated files to the models folder. Usage:\n\tpython {} <output directory> <model directory>".format(sys.argv[0]))
    if len(sys.argv) != 3:
        print("Invalid number of arguments.")
        sys.exit(1)

    file_dir = sys.argv[1]
    model_dir = sys.argv[2]
    cfgs_prioritized = [
        "modest_from-jani_to-umb-gz_default",
        "modest_from-jani_to-umb-gz_memory",
        "modest_from-jani_to-umb-gz_unsafe",
        "modest_from-jani_to-umb-gz_unsafe-memory",
        "modest_from-jani_to-umb-xz_default",
        "modest_from-jani_to-umb-xz_memory",
        "modest_from-jani_to-umb-xz_unsafe",
        "modest_from-jani_to-umb-xz_unsafe-memory",
        "modest_from-jani_to-umb_default",
        "modest_from-jani_to-umb_memory",
        "modest_from-jani_to-umb_unsafe",
        "modest_from-jani_to-umb_unsafe-memory",
        "prism_from-prism_to-tra_ex",
        "prism_from-prism_to-tra_default",
        "prism_from-prism_to-tra_norewards",
        "prism_from-prism_to-umb-gz_ex",
        "prism_from-prism_to-umb-gz_default",
        "prism_from-prism_to-umb-gz_norewards",
        "prism_from-prism_to-umb_ex",
        "prism_from-prism_to-umb_default",
        "prism_from-prism_to-umb_norewards",
        "storm_from-jani_to-drn-gz_sparse",
        "storm_from-jani_to-drn-xz_sparse",
        "storm_from-jani_to-drn_sparse",
        "storm_from-jani_to-umb-gz_sparse",
        "storm_from-jani_to-umb-xz_sparse",
        "storm_from-jani_to-umb_sparse",
        "storm_from-jani_to-umb_cudd",
        "storm_from-prism_to-jani_sparse"
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
            tool = cfg.split("_")[0]
            source_path = os.path.join(file_dir, cfg, model)
            for file_name in ["model.umb", "model.umb.xz", "model.umb.gz", "model.drn", "model.drn.xz", "model.drn.gz", "model.tra,lab", "model.tra,lab,rew", "umb.properties.txt", "umbxz.properties.txt", "umbgz.properties.txt", "model.jani"]:
                file_path = os.path.join(source_path, file_name)
                dest_path = os.path.join(model_dir, model, tool + "." + file_name)
                if os.path.exists(file_path) and not os.path.exists(dest_path):
                    print("Copying {} to {}".format(file_path, dest_path))
                    shutil.copyfile(file_path, dest_path)

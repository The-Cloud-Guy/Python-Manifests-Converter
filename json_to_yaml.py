import json
import sys
import yaml

in_file = sys.argv[1]
out_file = sys.argv[2]


with open(in_file) as input_content:
    with open(out_file, "w") as output_content:
        json_data = json.loads(input_content.read())
        converted_json_data = json.dumps(json_data)

        yaml_data = yaml.safe_load(converted_json_data)
        converted_yaml_data = yaml.dump(yaml_data)

        output_content.write(converted_yaml_data)
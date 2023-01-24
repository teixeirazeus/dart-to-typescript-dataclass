import fire
from src.dataclass_generator import DataClassGenerator
from src.extractor import ExtractEntities


def main(
    input_folder: str = "input-test-folder", output_folder: str = "output-test-folder"
):
    class_info_list = ExtractEntities.extract_all_entities_names(
        ExtractEntities.get_all_dart_files()
    )

    for class_info in class_info_list:
        if class_info is None:
            print("Found None")
        try:
            converted_class = DataClassGenerator.generate_data_class(class_info)
        except Exception as e:
            print(f"Error converting")
            continue
        file_name = converted_class.file.split("/")[-1].split(".")[0]
        file_name = file_name.replace("_", "-")
        with open(
            f"{output_folder}/{file_name}.ts",
            "w",
        ) as file:
            file.write(converted_class.code)


if __name__ == "__main__":
    fire.Fire(main)

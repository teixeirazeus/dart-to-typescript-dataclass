import fire
from src.dataclass_generator import DataClassGenerator
from src.extractor import ExtractEntities


def main(
    input_folder: str = "input-test-folder", output_folder: str = "output-test-folder"
):
    class_info_list = ExtractEntities.extract_all_entities_names(
        ExtractEntities.get_all_dart_files()
    )
    print(class_info_list)
    class_info_list = [
        DataClassGenerator.generate_data_class(class_info)
        for class_info in class_info_list
    ]
    for converted_class in class_info_list:
        print(converted_class.code)
        with open(
            f"{output_folder}/{converted_class.file.split('/')[-1].split('.')[0]}.ts",
            "w",
        ) as file:
            file.write(converted_class.code)


if __name__ == "__main__":
    fire.Fire(main)
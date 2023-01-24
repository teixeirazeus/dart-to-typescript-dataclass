from pathlib import Path
from typing import List
from src.entities.entities_info import AtributeInfo, EntitieInfo


class ExtractEntities:
    @staticmethod
    def get_all_dart_files():
        files = list(Path(".").rglob(f"*.dart"))
        for ban in ["env", ".env", "git", ".git"]:
            files = [
                x for x in files if ban not in x.parts and ban not in x.parent.parts
            ]
        return files

    @staticmethod
    def filter_files_in_this_path(files, path):
        return [file for file in files if str(file).startswith(path)]

    # @staticmethod
    # def find_type(txt):
    #     if "=" in txt:
    #         return txt.split("=")[0].strip()
    #     return txt

    @staticmethod
    def extract_class_names_in_file(file_path) -> List[EntitieInfo]:
        open_brace = False
        class_info = None
        with open(file_path, "r") as f:
            for line in f:
                if "{" in line:
                    if open_brace:
                        return class_info
                    open_brace = True
                if line.startswith("class"):
                    class_line = line.split(" ")[1].replace("{", "")
                    class_info = EntitieInfo(name=class_line, file=file_path)
                elif ";" in line and "import" not in line:

                    line_split = (
                        line.rstrip()
                        .lstrip()
                        .replace("final", "")
                        .replace("var", "")
                        .replace("?", "")
                        .replace(";", "")
                        .replace("\n", "")
                        .split(" ")
                    )
                    if "late" in line_split:
                        line_split.remove("late")

                    print(line)
                    print(line_split)

                    data_type, name = line_split[0], line_split[1]
                    # data_type = ExtractEntities.find_type(data_type)
                    name = name.rstrip().strip()
                    data_type = (
                        data_type.replace("final", "")
                        .replace("var", "")
                        .replace("?", "")
                        .rstrip()
                        .strip()
                    )
                    class_info.atributes.append(AtributeInfo(name=name, type=data_type))
        return class_info

    @staticmethod
    def extract_all_entities_names(files_in_folder) -> List[EntitieInfo]:
        entities_list = []
        # files_in_folder = ExtractEntities.filter_files_in_this_path(
        #     files, "src/entities"
        # )
        for file in files_in_folder:
            file_path = str(file)
            class_info = ExtractEntities.extract_class_names_in_file(file_path)

            entities_list.append(class_info)
        return entities_list

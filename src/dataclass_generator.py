from src.entities.entities_info import AtributeInfo, EntitieInfo


class DataClassGenerator:
    typescript_datamap = {
        "string": "string",
        "int": "number",
        "double": "number",
        "bool": "boolean",
        "datetime": "Date",
    }

    @staticmethod
    def generate_data_class(class_info: EntitieInfo) -> str:
        atributes = []
        for atribute in class_info.atributes:
            data_type = DataClassGenerator.convert_data_type(atribute.type)
            name = atribute.name
            atributes.append(AtributeInfo(name=name, type=data_type))

        class_info.atributes = atributes
        class_info.code = DataClassGenerator.gen_code(class_info)
        return class_info

    @staticmethod
    def gen_code(class_info) -> str:
        atributes_code = "".join(
            [
                DataClassGenerator.gen_atribute_code(atribute)
                for atribute in class_info.atributes
            ]
        )
        atributes_code = atributes_code[:-1]  # remove last \n
        return (
            'import { Data } from "dataclass";\n\n'
            + f"""
class {class_info.name} extends Data \u007b \n{atributes_code}
\u007d \n
"""
            + f"export \u007b{' '+class_info.name+' '}\u007d;"
        )

    @staticmethod
    def gen_atribute_code(atribute: AtributeInfo) -> str:
        return f"    {atribute.name}: {atribute.type};" + "\n"

    @staticmethod
    def convert_data_type(dart_type: str) -> str:
        if "List" in dart_type:
            inner_type = dart_type.replace("List<", "").replace(">", "").strip().lower()
            return f"Array<{DataClassGenerator.convert_data_type(inner_type)}>"
        if dart_type.lower() in DataClassGenerator.typescript_datamap:
            return DataClassGenerator.typescript_datamap[dart_type.lower()]
        return dart_type

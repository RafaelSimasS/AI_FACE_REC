import shutil as sh

def clear_prompt():
    import os
    os.system('clear') if os.name == 'posix' else os.system("cls")

def get_width() -> int:
    terminal_width, _ = sh.get_terminal_size()
    return terminal_width

def center_title(text: str, pad_symbol: str = "_") -> str:
    screen_width = get_width()
    pad = pad_symbol * ( (screen_width - len(text)) // 2 )
    return pad+text+pad

def center_text(text: str, mask: str = "#################", divisor: int = 2, pad_symbol: str = " " ) -> str:
    screen_width = get_width()
    mask_len = len(mask)
    pad = pad_symbol * ( (screen_width - mask_len) // divisor )
    return pad+text

def prompt_input_select(text:str, input_range: range, prompt_suffix:str = ": "):
    """Prompts a input message 
     :param text: the text to show for the prompt.
     :param input_range: the range of option.
     :param prompt_suffix: a suffix that should be added to the prompt.
       """
    while True:
        try:
            input_value = int(input(f"{text}{prompt_suffix}"))
            if input_value in input_range:
                return input_value
            else:
                print(f"Por favor, selecione uma opção no alcance {input_range.start} - {input_range.stop - 1}.")
        except ValueError:
            print("Valor Inválido. Deve ser um número de seleção.")
           
def load_json(file_path: str):
    import json
    with open(file_path, 'r', encoding="utf=8") as file:
        data_dict = json.load(file)
    return data_dict

def update_json(file_path: str, dict_data: dict):
    import json
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(dict_data, file, indent=4)

def format_option(option_num: int, text: str, max_model_name_width: int):
    # Format number with a zero at left if below 10
    option_num_str = str(option_num).zfill(2)

    text_str_captalized = text.capitalize().ljust(max_model_name_width) 

    formatted_option = f"{option_num_str}. {text_str_captalized}"

    return formatted_option

def show_temp_message(text:str, time: float = 1):
    from time import sleep
    print(text)
    sleep(time)

def get_real_path(symb_path: str) -> str:
    import os
    return os.path.realpath(symb_path)

import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def falar_text(texto: str):
    engine.say(texto)
    engine.runAndWait()

def is_path_exist(file_path) -> bool:
    import os
    return os.path.exists(file_path)

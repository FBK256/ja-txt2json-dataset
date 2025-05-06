import re
import json

class ToDataset:
    def __init__(self, files = None):
        self.files = files

    def is_math_expression(self, text):
        # 数式を判断する: $ で囲まれた部分を数式とみなす
        return bool(re.search(r'\$[^\$]+\$', text))

    def split_sentences(self, text):
        # 指定された句読点で文を分割し、数式部分は分割しない
        pattern = r'(?<!\$)([。！？!?]+)(?![\w\$\d])'
        parts = re.split(pattern, text)

        # 文を組み立てる
        sentences = []
        current_sentence = ''
        for part in parts:
            current_sentence += part
            if re.match(pattern, part):
                sentences.append(current_sentence.strip())
                current_sentence = ''

        if current_sentence:
            sentences.append(current_sentence.strip())

        return sentences

    def process_single_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 文を分割
        sentences = self.split_sentences(content)
        json_data = [{'text': sentence} for sentence in sentences]

        output_file = file_path.replace('.txt', '_processed.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, ensure_ascii=False, indent=4)

        print(f"Processed JSON saved to {output_file}")

    def process_multiple_files(self):
        instructions = []
        inputs = []
        outputs = []

        with open('instruction.txt', 'r', encoding='utf-8') as f:
            instructions = f.read().strip().split('\n')
        with open('input.txt', 'r', encoding='utf-8') as f:
            inputs = f.read().strip().split('\n')
        with open('output.txt', 'r', encoding='utf-8') as f:
            outputs = f.read().strip().split('\n')

        data = []
        for instr, inp, outp in zip(instructions, inputs, outputs):
            entry = {
                "instruction": instr,
                "input": inp,
                "output": outp
            }
            data.append(entry)

        output_file = 'combined_processed.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Processed JSON saved to {output_file}")

    def process(self):
        if len(self.files) == 1:
            # テキストファイルが1つの場合
            self.process_single_file(self.files[0])
        elif len(self.files) == 3 and set(self.files) == {'instruction.txt', 'input.txt', 'output.txt'}:
            # テキストファイルが3つの場合
            self.process_multiple_files()
        else:
            print("Invalid input. Please provide either one text file or exactly three specific files (instruction.txt, input.txt, output.txt).")

# テストデータを含む使用例
files = [input("text file")]
processor = ToDataset(files)
processor.process()
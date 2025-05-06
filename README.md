# ja-txt2json-dataset

Tiny utility to turn Japanese plain-text files **or**  
`instruction.txt / input.txt / output.txt` triples into a clean JSON dataset
ready for LLM fine-tuning.

## ✨ Features
- 📝 Sentence-splitter that keeps LaTeX‐style math `$x^2$` untouched  
- 📦 Single-file mode → `mytext_processed.json`  
- 📦 Triple-file mode → `combined_processed.json`

## Requirements
Python 3.9+ (no external deps).

## Usage
```bash
python todataset.py
# プロンプトが出るのでファイル名を入力

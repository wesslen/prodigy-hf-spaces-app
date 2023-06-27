# Activate venv
source /opt/venv/bin/activate

# Make sure prodigy.json has appropriate environment variables
python scripts/mkconfig.py

# Run command
python -m prodigy ner.manual news_ner blank:en data/dataset.jsonl --label ORG,PERSON,GPE 
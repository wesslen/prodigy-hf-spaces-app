# Activate venv
source /opt/venv/bin/activate

# clone repo
spacy project clone tutorials/spancat_food_ingredients

# cd to folder
cd spancat_food_ingredients

# Make sure prodigy.json has appropriate environment variables
python ../scripts/mkconfig.py

# Run command
python -m spacy project run span_manual
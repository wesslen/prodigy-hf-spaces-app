import prodigy
import itertools as it
from prodigy.util import set_hashes
from prodigy import get_stream


@prodigy.recipe(
    "rlhf.respond",
    dataset=("Dataset to save answers to", "positional", None, str),
    source=("Datafile to load", "positional", None, str),
)
def ranking(dataset, source):
    # Load your own streams from anywhere you want
    stream = get_stream(source)
    
    def prep_stream(stream):
        for ex in stream:
            ex['text'] = ex['instruction']
            del ex['instruction']
            yield ex

    return {
        "dataset": dataset,
        "view_id": "blocks",
        "stream": prep_stream(stream),
        "config":{
            "global_css": ".prodigy-option{font-size: 15px;}",
            "blocks":[
                {"view_id": "text"},
                {"view_id": "text_input", "field_autofocus": True, "field_rows": 4, "field_placeholder": "Try to use 2-3 sentences to answer the question."},
            ],
        }
    }
import streamlit as st

from huggingface_hub import HfApi
from huggingface_hub import create_repo
# from huggingface_hub import duplicate_space
# from huggingface_hub import hf_hub_download

from dotenv import load_dotenv
import os

# create a local .env file with HF_TOKEN (HF Hub Token)
load_dotenv()
HF_TOKEN = os.environ.get("HF_TOKEN")

api = HfApi(token=HF_TOKEN)

personal = api.whoami()

repo_name = st.text_input('Name of new HF Space', 'my-prodigy-repo')
org = personal["name"]
repo_id = org + "/" + repo_name
prodigy_key = st.text_input('Prodigy Key')
auth_user = st.text_input('Prodigy Username')
auth_pass = st.text_input('Prodigy Password')
#repo_dup = "wesslen/prodigy-template-space"

input_file = st.file_uploader("Upload your input (source) file here (`.jsonl`)...", type = ["jsonl"])
sh_file = st.file_uploader("Upload your bash file to run (.sh)", type = ["sh"])


if st.button('Create new HF Space'):

    api.create_repo(repo_id, private=True, space_sdk="docker", repo_type="space")

    if prodigy_key is not None:
        api.add_space_secret(repo_id=repo_id, key="LICENSE_KEY", value=prodigy_key)

    if auth_user is not None:
        api.add_space_secret(repo_id=repo_id, key="PRODIGY_BASIC_AUTH_USER", value=auth_user)

    if auth_pass is not None:
        api.add_space_secret(repo_id=repo_id, key="PRODIGY_BASIC_AUTH_PASS", value=auth_pass)


    api.upload_folder(
        folder_path="template",
        repo_id=repo_id,
        repo_type="space",
    )

    if sh_file is not None:
        api.upload_file(
            path_or_fileobj=sh_file,
            path_in_repo="prodigy.sh",
            repo_id=repo_id,
            repo_type="space",
        )

    if input_file is not None:
        api.upload_file(
            path_or_fileobj=input_file,
            path_in_repo="data/dataset.jsonl",
            repo_id=repo_id,
            repo_type="space",
        )

    st.write("Created HF Space: " + repo_id)

    build = "https://huggingface.co/spaces/" + repo_id + "?session=user1&logs=build"
    st.markdown(build, unsafe_allow_html=True)
    url = "https://huggingface.co/spaces/" + repo_id + "?session=user1"
    st.markdown(url, unsafe_allow_html=True)


if st.button('Delete HF Space'):

    api.delete_repo(repo_id, repo_type = "space")

    st.write("Deleted HF Space: " + repo_id)

FROM python:3.9

#COPY requirements.txt /app/
WORKDIR /app
# # Set up a new user named "user" with user ID 1000
# RUN useradd -m -u 1000 user
# # Switch to the "user" user
# USER user
# # Set home to the user's home directory
# ENV HOME=/home/user \
# 	PATH=/home/user/.local/bin:$PATH

# # Set the working directory to the user's home directory
# WORKDIR $HOME/app

# # Copy the current directory contents into the container at $HOME/app setting the owner to the user
# COPY --chown=user . $HOME/app

RUN --mount=type=secret,id=LICENSE_KEY,mode=0444,required=true \
    pip install --upgrade pip \
    && pip install typing_extensions==4.5.0 \
    && pip install --quiet prodigy -f https://$(cat /run/secrets/LICENSE_KEY)@download.prodi.gy

RUN chmod 777 .

COPY prodigy.json .
COPY data ./data/
COPY recipe.py .
COPY prodigy.sh .

ENV PRODIGY_HOME /app
ENV PRODIGY_LOGGING "verbose"
ENV PRODIGY_ALLOWED_SESSIONS "user1,user2"

EXPOSE 7860

CMD ["bash","prodigy.sh"]
FROM python:3.9

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
COPY .env .

# RUN python -m pip install --upgrade pip && \
#     python -m pip install -r requirements.txt && \
#     export $(cat .env) && python -m pip install --quiet --pre prodigy -f https://${PRODIGY_KEY}@download.prodi.gy

# RUN chmod 777 .
RUN --mount=type=secret,id=LICENSE_KEY,mode=0444,required=true \
    pip install --upgrade pip \
    && pip install typing_extensions==4.5.0 \
    && pip install -r requirements.txt \
    && pip install --quiet --pre prodigy -f https://$(cat /run/secrets/LICENSE_KEY)@download.prodi.gy

# Remove .env from container
RUN rm -rf .env

# Set up a new user named "user" with user ID 1000
RUN useradd -m -u 1000 user
# Switch to the "user" user
USER user
# Set home to the user's home directory
ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

# Set the working directory to the user's home directory
WORKDIR $HOME/app

# Copy the current directory contents into the container at $HOME/app setting the owner to the user
COPY --chown=user . $HOME/app

ENV PRODIGY_HOME /app
ENV PRODIGY_LOGGING "verbose"
ENV PRODIGY_ALLOWED_SESSIONS "user1,user2,user3,user4"
EXPOSE 7860

CMD ["bash","prodigy.sh"]
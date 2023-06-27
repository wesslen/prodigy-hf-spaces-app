FROM python:3.9


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

RUN chmod 777 .

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .

RUN --mount=type=secret,id=LICENSE_KEY,mode=0444,required=true \
    pip install --upgrade pip \
    && pip install typing_extensions==4.5.0 \
    && pip install -r requirements.txt \
    && pip install --quiet --pre prodigy -f https://$(cat /run/secrets/LICENSE_KEY)@download.prodi.gy

COPY prodigy.json .
COPY data ./data/
COPY recipe.py .
COPY prodigy.sh .

ENV PRODIGY_HOME /app
ENV PRODIGY_LOGGING "verbose"
ENV PRODIGY_ALLOWED_SESSIONS "user1,user2,user3,user4,user5,user6,user7,user8,user9,user10,user11,user12,user13,user14,user15,user16,user17,user18,user19,user20,user21,user22,user23,user24,user25,user26,user27,user28,user29,user30,user31,user32,user33,user34,user35,user36,user37,user38,user39,user40,user41,user42,user43,user44,user45,user46,user47,user48,user49,user50,user51,user52,user53,user54,user55,user56,user57,user58,user59,user60,user61,user62,user63,user64,user65,user66,user67,user68,user69,user70,user71,user72,user73,user74,user75,user76,user77,user78,user79,user80,user81,user82,user83,user84,user85,user86,user87,user88,user89,user90,user91,user92,user93,user94,user95,user96,user97,user98,user99,user100"

EXPOSE 7860

CMD ["bash","prodigy.sh"]
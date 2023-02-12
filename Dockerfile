FROM     alpine:3.17
RUN     apk update
RUN     apk add python3
RUN     python3 -m ensurepip
RUN     python3 -m pip install flask
RUN     mkdir /sample-app
WORKDIR /sample-app
COPY    . .
ENTRYPOINT [ "python3", "app.py" ]
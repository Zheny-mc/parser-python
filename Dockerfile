FROM python:3.8.3-alpine

RUN pip install --upgrade pip

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser


COPY --chown=myuser:myuser . .

RUN pip install --user openpyxl
RUN pip install --user -r requirements.txt

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .

CMD [ "python", "./parser.py" ]
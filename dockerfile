FROM ubuntu:22.04

RUN apt update -y && apt install -y python3 python3-pip python3-dev

CMD ["ufw allow 5000"]

COPY myapp.py /app/myflusk/
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install -r requirements.txt



ENTRYPOINT [ "python3" ]
CMD ["/app/myflusk/myapp.py"]
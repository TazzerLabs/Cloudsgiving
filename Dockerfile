FROM python:3.7

ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

RUN mkdir -p /opt/services/instapic/src
WORKDIR /opt/services/instapic/src

# install
RUN pip install gunicorn

COPY . /opt/services/instapic/src

RUN pip install -r requirements.txt

EXPOSE 8080

# CMD to ignite at start
CMD ["gunicorn", "--chdir", "instapic", "--bind", ":8080", "instapic.wsgi:application"]


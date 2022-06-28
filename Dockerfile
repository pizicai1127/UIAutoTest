#FROM dockerhub.tezign.com/library/python3.7_google
FROM dockerhub.tezign.com/library/python3.7_jdk8:2
USER root
WORKDIR /app
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone
ADD requirements.txt requirements.txt
#RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --timeout 30 --no-cache-dir -r requirements.txt -i https://mirrors.huaweicloud.com/repository/pypi/simple/
COPY . /app
EXPOSE 9000
#CMD PLAYWRIGHT_BROWSERS_PATH=/usr/local/lib/python3.7/site-packages/pw-browsers python all.py
CMD python all.py
  
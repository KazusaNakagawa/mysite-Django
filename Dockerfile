FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim

# ref: https://repo.anaconda.com/archive/
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh && \
    sh Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/anaconda3 && \
    # インストール後必要ないから削除
    rm -f Anaconda3-2020.02-Linux-x86_64.sh

# pythonを扱えるようにpathを通す
# /opt/anaconda3/bin 配下に $PATHを通す　
# $PATH 既存のPATHに追加している
ENV PATH /opt/anaconda3/bin:$PATH

# 今後 pip installで追加したいpackageがある時のため
RUN pip install --upgrade pip

# Set entrypoint
# ENTRYPOINT ["/bin/bash", "scripts/init_mysite.sh"]
CMD ["/bin/bash"]
## m1 - python 3.7
- https://stackoverflow.com/questions/70205633/cannot-install-python-3-7-on-osx-arm64
- https://github.com/conda/conda/issues/12206

## create empty environment
conda create -n py37

## activate
conda activate py37

## use x86_64 architecture channel(s)
conda config --env --set subdir osx-64

## install python, numpy, etc. (add more packages here...)
conda install python=3.7
conda install python=3.7 numpy

=========================

### dataset
- https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database

### Start the env from anaconda
- py37
- open terminal
- python3 -V
3.7.16

### run the app
sh start.sh

### postman collection
- spark recommendation

### Matthew effect
- most rating / high rating
- create pool (n=1000)
- random select 20 in the pool 

### 最近邻查找算法
- Brute force: O(KN)
- K-D tree: O(sqart(n))
- K-Means
- LSH (Spark Mllib / FAISS) O(K)
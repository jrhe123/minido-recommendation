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

### 最近邻查找算法 ANN
- Brute force: O(KN)
- K-D tree: O(sqart(n))
- K-Means
- LSH (Spark Mllib / FAISS) O(K)

### tensorflow
- https://playground.tensorflow.org/


### 衡量推荐系统

- 满足商业目标

- 用户维度
  - 准确性 (注意：天气冷推荐衣服，准确性高，但没有创造额外价值)
  - 多样性：覆盖用户不同需求
  - 新颖性：没见过的物品 (iphone -> headset)
  - 惊喜度（男性 -> 推荐birkin包包）


- 平台维度
  - 转化率：曝光到下单的每一步的漏斗
  - 覆盖率：(注意：马太效应)
  信息熵（information entropy）
  基尼系数(英语：Gini coefficient) - 分布不均衡的程度

  - 曝光率：合作方
  ACP(average click price)


### 评估流程
- 模型训练

- 离线评估
1. offline data
2. 灵活性高
3. 多指标评估 (RMSE (imbalance data not good), precision, recall, F-score, logloss, MAP)
- MAP: 平均精度值 (位置敏感)
4. 不影响线上用户

=> cross validation (k subset -> train & test)
=> use replay (测试集晚于训练集)

- 模型上线
- 在线评估
- 收集反馈
- 迭代优化


### A/B testing (在线评估)
- 易于评估复杂情况：播放时长 / conversion rate

分桶：
- 男女生分割不均衡：辛普森悖论

分层：

使用z-score来判断：strategy A or B
=> 如果效果不好，则退回旧的model


### cold start
- retention rate
- registration flow
1. demographics
2. source channel
3. user relationship
4. tags collection
5. top sell items
6. 专家打标 (例如：适合30岁男性)

### 实时性
- UGC：较强 (小红书) content created by users
- PGC：较弱 （电影网）content created by professionals

批处理 / 流处理 (trend & 短时间特征)

- 稀疏性
- FTRL 模型
- 全量更新、增量更新


### Apache Flink

准实时性：
- Kafka -> Flink(简单聚类) -> Redis (保存)
- user call: Redis -> Recall -> Rank

强实时性：
- user call: with last 1 minute history
-> recall -> rank

=> add higher weight to (last 1 minute history)

- 计算窗口
Event time -> kafka -> flink ingestion time (写入时间) -> flink process time (处理时间)


### reinforcement learning

- alpha go
- flappy bird: reward, agent, state, action

s1,a1,r1 => s2,a2,r2 => s3,a3,r3

回报函数
U = r1 + y*r2 + y^2*r3 +...

y = 0 ~ 1

着眼于现在的回报, 未来的回报有衰减函数


### wide & deep

- 女生喜欢裙子
- 不喜欢红色裙子

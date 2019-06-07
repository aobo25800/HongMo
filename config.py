from redis import StrictRedis
class Config:
    DEBUG = True
    # 设置秘钥
    SECRET_KEY = 'Px3gNC9PMay6Tb8SUxmHB0QDHNrPRSmeih66p4uc3p0WrTwByQmuba96Yfufmw45roI='

    # 配置状态保持中的session信息，储存在redis数据库中
    SESSION_TYPE = 'redis'
    # session链接redis数据库实例
    SESSION_REDIS = StrictRedis(host='127.0.0.1', port=6379)
    # session签名
    SESSION_USE_SIGNER = True
    # session有效期
    PERMANENT_SESSION_LIFETIME = 86400
    
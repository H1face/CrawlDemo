# 连接池
# 把他做成单例，写在一个文件里面，import它
import redis

# 拿到一个redis的连接池
Pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10)
redis_conn = redis.Redis(connection_pool=Pool,decode_responses=True)

# redis_conn.flushall()
print(redis_conn.scan())

print(redis_conn.smembers('visited_urls'))
print(redis_conn.scard('visited_urls'))
print(redis_conn.llen('csdn:start_urls'))
print(redis_conn.lrange('csdn:start_urls',0,290))
# print(redis_conn.scard('visited_urls'))

# redis_conn.lpush("csdn:start_urls","https://blog.csdn.net/ycjnx/article/details/81067641")

# redis_conn.lpush("csdn:start_urls","https://blog.csdn.net/dog250/article/details/93397367")
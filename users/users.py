def create_user(user_id, config):
    f = open(f'{user_id}.txt', 'w+')
    for key in config:
        f.write(f'{key}={config[key]}\n')
    f.close()

def read_users(user_id):
    f = open(f'{user_id}.txt', 'r')
    lines = f.readlines()
    result = {}
    for line in lines:
        key, value = line.split('=')
        result[key] = value.strip('\n')
    f.close()
    return result
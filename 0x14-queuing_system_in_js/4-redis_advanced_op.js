import Redis from 'redis';
const cli = Redis.createClient();

const myKey = 'HolbertonSchools'
cli.hset(myKey, "Portland", 50, Redis.print);
cli.hset(myKey, "Seattle", 80, Redis.print);
cli.hset(myKey, "New York", 20, Redis.print);
cli.hset(myKey, "Bogota", 20, Redis.print);
cli.hset(myKey, "Cali", 40, Redis.print);
cli.hset(myKey, "Paris", 2, Redis.print);

cli.hgetall(myKey, function(err, result) {
    console.log(result);
});

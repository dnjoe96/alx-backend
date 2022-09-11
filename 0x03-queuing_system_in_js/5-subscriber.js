import redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', (err) => {
  console.log('Redis client connected to the server');
  if (err) {
    console.log('Redis client not connected to the server: ', err)
  }
});

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  if (channel === 'holberton school channel') console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});

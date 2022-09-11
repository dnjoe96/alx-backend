import { createClient } from 'redis';
const moment = require('moment');

moment.

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));

await client.connect();

await client.set('key', 'value');
const value = await client.get('key');
console.log(value);

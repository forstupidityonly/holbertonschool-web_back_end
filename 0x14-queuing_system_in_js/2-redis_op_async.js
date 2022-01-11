import Redis from 'redis';
const cli = Redis.createClient();
const { promisify } = require('util');
const myAsync = promisify(cli.get).bind(cli);

cli.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
})

cli.on('connect', () => {
    console.log('Redis client connected to the server')
})

const setNewSchool = (schoolName, value) => {
    cli.set(schoolName, value, function(err, reply) {
        console.log(reply);
    });
}

async function displaySchoolValue(schoolName) {
    console.log(await myAsync(schoolName));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

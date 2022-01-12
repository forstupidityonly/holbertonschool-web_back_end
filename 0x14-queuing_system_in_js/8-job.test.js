const queue = require('kue').createQueue();
import { expect } from 'chai';
import createPushNotificationsJobs from './8-job';

before(function() {
  queue.testMode.enter();
});

afterEach(function() {
  queue.testMode.clear();
});

after(function() {
  queue.testMode.exit()
});

it('throw err if jobs not array', function() {
    expect(() => createPushNotificationsJobs(undefined, queue)).to.throw(Error, 'Jobs is not an array');
});

it('create three new jobs', function() {
    const myData = [
        {
            phoneNumber: '1800362-4368',
            message: 'Dirty Deeds Done Dirt Cheap',
        },
        {
            phoneNumber: '1800867-5309',
            message: 'Jenny Ive got your number',
        },
        {
            phoneNumber: '1-800-273-8255',
            message: 'I want you to be alive, I want you to be alive',
        }
    ];
    createPushNotificationsJobs(myData, queue);
    expect(queue.testmode.jobs.length).to.equal(3);
});

import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '1800362-4368',
    message: 'Dirty Deeds Done Dirt Cheap',
}

function sendNotification(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

const job = queue.create('push_notification_code', jobData).save((err) => {
    sendNotification(jobData.phoneNumber, jobData.message);
});

job.on('enqueue', function(id, type) {
    console.log(`Notification job created: ${job.id}`);
})
job.on('complete', function(rez) {
    console.log('Notification job completed');
})
job.on('failed', function(err) {
    console.log('Notification job failed');
})

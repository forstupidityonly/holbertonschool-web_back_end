export default function createPushNotificationsJobs (jobs, queue) {
    if (!Array.isArray(jobs)) {
        throw Error('Jobs is not an array');
    }
    jobs.forEach((job) => makeJobs(job.phoneNumber, job.message, queue))
}

function makeJobs (phoneNumber, message, queue) {
    const jobData = {
        phoneNumber: phoneNumber,
        message: message,
    }
    const job = queue.create('push_notification_code_3', jobData).save();

    job.on('enqueue', function(id, type) {
        console.log(`Notification job created: ${job.id}`);
    })
    job.on('complete', function(rez) {
        console.log(`Notification job ${job.id} completed`);
    })
    job.on('failed', function(err) {
        console.log(`Notification job ${job.id} failed: ${err}`);
    })
    job.on('progress', function(progress, data) {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    })
}
